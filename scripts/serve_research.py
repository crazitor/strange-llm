#!/usr/bin/env python3
"""Web dashboard for browsing the AI philosophy research corpus."""

import json
import os
import sqlite3
import time
import markdown
from flask import Flask, request, jsonify, render_template_string

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')
CHROMA_DIR = os.path.join(RESEARCH_DIR, 'chroma_db')

app = Flask(__name__)

import re as _re
def strip_frontmatter(text):
    """Remove YAML frontmatter (--- ... ---) from markdown content."""
    if text and text.startswith('---'):
        m = _re.match(r'^---\s*\n.*?\n---\s*\n?', text, _re.DOTALL)
        if m:
            return text[m.end():].lstrip()
    return text or ''

def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.row_factory = sqlite3.Row
    return conn

# Try to load ChromaDB at startup
chroma_articles = None
chroma_books = None
chroma_article_chunks = None
try:
    import chromadb
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    chroma_articles = client.get_collection('articles')
    print(f'ChromaDB articles: {chroma_articles.count()} embeddings')
    try:
        chroma_books = client.get_collection('book_chunks')
        print(f'ChromaDB book_chunks: {chroma_books.count()} embeddings')
    except Exception:
        print('ChromaDB book_chunks not available')
    try:
        chroma_article_chunks = client.get_collection('article_chunks')
        print(f'ChromaDB article_chunks: {chroma_article_chunks.count()} embeddings')
    except Exception:
        print('ChromaDB article_chunks not available')
    try:
        chroma_arguments = client.get_collection('arguments')
        print(f'ChromaDB arguments: {chroma_arguments.count()} embeddings')
    except Exception:
        chroma_arguments = None
except Exception as e:
    print(f'ChromaDB not available: {e}')

# Ensure plan_progress table exists at startup
try:
    _conn = sqlite3.connect(DB_PATH, timeout=10)
    _conn.execute('''CREATE TABLE IF NOT EXISTS plan_progress (
        month INTEGER, week INTEGER, task_idx INTEGER,
        done INTEGER DEFAULT 0, updated_at TEXT,
        PRIMARY KEY (month, week, task_idx))''')
    _conn.commit()
    _conn.close()
except Exception:
    pass

# Cross-encoder reranker for RAG
reranker = None
try:
    from sentence_transformers import CrossEncoder
    reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    print('Cross-encoder reranker loaded')
except Exception as e:
    print(f'Reranker not available: {e}')

# DeepSeek client for translation & RAG
deepseek_client = None
try:
    from openai import OpenAI
    ds_key = os.environ.get('DEEPSEEK_API_KEY', 'sk-1556a07369cf474f8e886c130e3584ca')
    deepseek_client = OpenAI(api_key=ds_key, base_url='https://api.deepseek.com')
    print('DeepSeek API available')
except Exception:
    print('DeepSeek API not available (pip install openai)')

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Philosophy Research Corpus</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --bg: #0d1117; --surface: #161b22; --border: #30363d;
  --text: #c9d1d9; --text-dim: #8b949e; --accent: #58a6ff;
  --accent2: #7ee787; --tag-bg: #1f2937;
  --essential: #f97583; --important: #d2a8ff; --useful: #79c0ff; --reference: #8b949e;
  --orange: #f0883e;
}
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       background: var(--bg); color: var(--text); height: 100vh; overflow: hidden; }

.app { display: grid; grid-template-rows: auto 1fr; height: 100vh; }
.header { background: var(--surface); border-bottom: 1px solid var(--border);
           padding: 10px 20px; display: flex; align-items: center; gap: 12px; }
.header h1 { font-size: 15px; color: var(--accent); white-space: nowrap; }
.search-bar { flex: 1; display: flex; gap: 6px; align-items: center; }
.search-bar input { flex: 1; background: var(--bg); border: 1px solid var(--border);
                     color: var(--text); padding: 7px 12px; border-radius: 6px; font-size: 13px; }
.search-bar select { background: var(--bg); border: 1px solid var(--border);
                      color: var(--text); padding: 7px; border-radius: 6px; font-size: 12px; }
.search-bar button { background: var(--accent); color: #000; border: none;
                      padding: 7px 14px; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 12px; }
.btn-stats { background: var(--accent2) !important; }
.btn-zh { background: #d2a8ff !important; }
.btn-ask { background: var(--orange) !important; color: #000 !important; }
.btn-ask.active { box-shadow: 0 0 0 2px var(--orange); }

.main { display: grid; grid-template-columns: 200px 1fr 1fr; overflow: hidden; }

/* Sidebar */
.sidebar { background: var(--surface); border-right: 1px solid var(--border);
           padding: 10px; overflow-y: auto; font-size: 12px; }
.sidebar h3 { color: var(--accent); font-size: 11px; text-transform: uppercase;
              margin: 10px 0 4px; letter-spacing: 0.5px; }
.sidebar h3:first-child { margin-top: 0; }
.filter-item { padding: 3px 6px; cursor: pointer; border-radius: 4px; display: flex;
               justify-content: space-between; align-items: center; }
.filter-item:hover { background: var(--border); }
.filter-item.active { background: var(--accent); color: #000; }
.filter-item .count { color: var(--text-dim); font-size: 10px; }
.filter-item.active .count { color: #000; }

/* Mode tabs */
.mode-tabs { display: flex; gap: 2px; margin-bottom: 8px; }
.mode-tab { flex: 1; padding: 6px; text-align: center; cursor: pointer;
            border-radius: 4px; font-size: 11px; font-weight: 600;
            background: var(--bg); color: var(--text-dim); }
.mode-tab.active { background: var(--accent); color: #000; }
.mode-tab:hover:not(.active) { background: var(--border); }

/* Level badges */
.level-badge { display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px;
               font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
.level-essential { background: var(--essential); color: #000; }
.level-important { background: var(--important); color: #000; }
.level-useful { background: var(--useful); color: #000; }
.level-reference { background: var(--reference); color: #000; }

/* Article list */
.list-panel { border-right: 1px solid var(--border); overflow-y: auto; }
.list-header { padding: 8px 14px; border-bottom: 1px solid var(--border);
               display: flex; justify-content: space-between; align-items: center;
               font-size: 12px; color: var(--text-dim); position: sticky; top: 0;
               background: var(--bg); z-index: 1; }
.article-item { padding: 10px 14px; border-bottom: 1px solid var(--border);
                cursor: pointer; transition: background 0.1s; }
.article-item:hover { background: var(--surface); }
.article-item.selected { background: var(--surface); border-left: 3px solid var(--accent); }
.article-title { font-size: 13px; font-weight: 600; margin-bottom: 3px;
                 display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.article-title-zh { font-size: 12px; color: var(--text-dim); margin-bottom: 3px;
                    display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden; }
.article-meta { font-size: 11px; color: var(--text-dim); display: flex; gap: 6px; flex-wrap: wrap; align-items: center; }
.article-score { background: var(--accent); color: #000; padding: 1px 5px;
                 border-radius: 10px; font-weight: 700; font-size: 10px; }
.article-tags { margin-top: 3px; display: flex; gap: 3px; flex-wrap: wrap; }
.tag { background: var(--tag-bg); color: var(--accent2); padding: 1px 6px;
       border-radius: 10px; font-size: 10px; cursor: pointer; }
.tag:hover { background: var(--accent2); color: #000; }
.article-snippet { font-size: 11px; color: var(--text-dim); margin-top: 3px;
                   display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

/* Book items in list */
.book-item { padding: 10px 14px; border-bottom: 1px solid var(--border);
             cursor: pointer; transition: background 0.1s; }
.book-item:hover { background: var(--surface); }
.book-item.selected { background: var(--surface); border-left: 3px solid var(--orange); }
.book-category { background: var(--orange); color: #000; padding: 1px 5px;
                 border-radius: 10px; font-weight: 700; font-size: 10px; }
.book-lang { padding: 1px 5px; border-radius: 3px; font-size: 10px; font-weight: 600;
             background: var(--border); color: var(--text); }

/* Reading panel */
.reading-panel { overflow-y: auto; padding: 20px 28px; }
.reading-panel h1 { font-size: 20px; margin-bottom: 4px; }
.reading-panel .title-zh { font-size: 16px; color: var(--text-dim); margin-bottom: 8px; }
.reading-panel .meta { color: var(--text-dim); margin-bottom: 12px; font-size: 13px;
                        display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
.reading-panel .meta a { color: var(--accent); }
.toolbar { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
.toolbar button { padding: 6px 14px; border-radius: 6px; border: 1px solid var(--border);
                  background: var(--surface); color: var(--text); cursor: pointer; font-size: 12px; }
.toolbar button:hover { background: var(--border); }
.toolbar button.active { background: var(--accent); color: #000; border-color: var(--accent); }
.toolbar button:disabled { opacity: 0.5; cursor: not-allowed; }
.translate-status { font-size: 12px; color: var(--accent2); padding: 4px 0; }
.reading-panel .content { line-height: 1.7; font-size: 14px; }
.reading-panel .content h1, .reading-panel .content h2, .reading-panel .content h3 {
  margin-top: 20px; margin-bottom: 8px; color: var(--accent); }
.reading-panel .content p { margin-bottom: 10px; }
.reading-panel .content pre { background: var(--surface); padding: 12px; border-radius: 6px;
                               overflow-x: auto; margin-bottom: 12px; font-size: 13px; }
.reading-panel .content code { background: var(--surface); padding: 2px 5px; border-radius: 3px; font-size: 13px; }
.reading-panel .content blockquote { border-left: 3px solid var(--accent); padding-left: 16px;
                                      color: var(--text-dim); margin: 12px 0; }
.reading-panel .content a { color: var(--accent); }
.reading-panel .content img { max-width: 100%; }
.reading-panel .similar-section { margin-top: 24px; padding-top: 12px; border-top: 1px solid var(--border); }
.reading-panel .similar-section h3 { color: var(--accent); font-size: 13px; margin-bottom: 6px; }
.similar-item { padding: 4px 0; font-size: 12px; cursor: pointer; color: var(--accent); }
.similar-item:hover { text-decoration: underline; }
.empty-state { display: flex; align-items: center; justify-content: center;
               height: 100%; color: var(--text-dim); font-size: 15px; }

/* Info box */
.info-box { background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
            padding: 12px 16px; margin-bottom: 16px; font-size: 13px; }
.info-box strong { color: var(--accent); }

/* Stats */
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 12px; }
.stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }
.stat-card h3 { color: var(--accent); font-size: 12px; margin-bottom: 6px; }
.stat-card .number { font-size: 26px; font-weight: 700; }
.stat-bar { display: flex; align-items: center; gap: 6px; margin: 2px 0; font-size: 11px; }
.stat-bar-fill { height: 6px; background: var(--accent); border-radius: 3px; }
.stat-bar-label { min-width: 130px; color: var(--text-dim); }

/* Chapter list */
.chapter-item { padding: 6px 14px; border-bottom: 1px solid var(--border);
                cursor: pointer; font-size: 12px; display: flex; justify-content: space-between; }
.chapter-item:hover { background: var(--surface); }
.chapter-item.selected { background: var(--surface); border-left: 3px solid var(--orange); }
.chapter-item .ch-num { color: var(--text-dim); min-width: 30px; }
.chapter-item .ch-pages { color: var(--text-dim); font-size: 10px; }

/* Chapter nav */
.chapter-nav { display: flex; gap: 8px; margin-bottom: 12px; align-items: center; }
.chapter-nav button { padding: 4px 12px; border-radius: 4px; border: 1px solid var(--border);
                      background: var(--surface); color: var(--text); cursor: pointer; font-size: 12px; }
.chapter-nav button:hover { background: var(--border); }
.chapter-nav select { background: var(--bg); border: 1px solid var(--border);
                      color: var(--text); padding: 4px 8px; border-radius: 4px; font-size: 12px; flex: 1; }

/* Notes */
.notes-section { margin-top: 20px; padding-top: 12px; border-top: 1px solid var(--border); }
.note-input { width: 100%; background: var(--bg); border: 1px solid var(--border); color: var(--text);
              padding: 8px; border-radius: 6px; font-size: 13px; resize: vertical; min-height: 60px; }
.note-item { padding: 8px; margin: 6px 0; background: var(--surface); border-radius: 6px;
             border-left: 3px solid var(--accent2); font-size: 12px; }
.note-item .note-meta { color: var(--text-dim); font-size: 10px; margin-top: 4px; }
.note-highlight { background: rgba(126,231,135,0.15); padding: 2px 4px; border-radius: 2px;
                  font-style: italic; font-size: 11px; color: var(--accent2); margin-bottom: 4px; }

/* Ask AI */
.ask-panel { padding: 20px 28px; }
.ask-input-wrap { display: flex; gap: 8px; margin-bottom: 16px; }
.ask-input-wrap textarea { flex: 1; background: var(--bg); border: 1px solid var(--border);
                            color: var(--text); padding: 10px; border-radius: 6px; font-size: 14px;
                            resize: vertical; min-height: 60px; font-family: inherit; }
.ask-input-wrap button { align-self: flex-end; padding: 10px 20px; }
.ask-templates { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; }
.ask-template { padding: 4px 10px; border-radius: 14px; border: 1px solid var(--border);
                background: var(--surface); color: var(--text-dim); cursor: pointer; font-size: 11px; }
.ask-template:hover { border-color: var(--orange); color: var(--orange); }
.ask-answer { line-height: 1.7; font-size: 14px; }
.ask-answer .source-item { padding: 4px 8px; margin: 4px 0; background: var(--surface);
                           border-radius: 4px; font-size: 12px; cursor: pointer; }
.ask-answer .source-item:hover { background: var(--border); }
.ask-loading { color: var(--orange); font-size: 14px; padding: 20px 0; }

/* Progress bar for books */
.book-progress { height: 3px; background: var(--border); border-radius: 2px; margin-top: 4px; }
.book-progress-fill { height: 100%; background: var(--accent2); border-radius: 2px; transition: width 0.3s; }
.book-progress-text { font-size: 10px; color: var(--text-dim); margin-top: 1px; }

/* Overview card */
.overview-card { background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
                 padding: 16px; margin-bottom: 16px; }
.overview-card h3 { color: var(--accent); font-size: 14px; margin-bottom: 8px; }
.overview-card .overview-content { font-size: 13px; line-height: 1.6; }

/* Compare toggle */
.compare-toggle { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--text-dim); }
.compare-toggle input { accent-color: var(--orange); }

/* Related items */
.related-section { margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border); }
.related-section h3 { color: var(--accent); font-size: 13px; margin-bottom: 8px; }
.related-card { padding: 8px 12px; margin: 6px 0; background: var(--surface); border-radius: 6px;
                border-left: 3px solid var(--accent); cursor: pointer; font-size: 12px; }
.related-card:hover { background: var(--border); }
.related-card .related-source { color: var(--orange); font-size: 10px; }
.related-card .related-snippet { color: var(--text-dim); font-size: 11px; margin-top: 2px; }

/* Learning path */
.learning-path { padding: 12px; }
.learning-path h3 { color: var(--accent); margin-bottom: 8px; }
.path-group { margin-bottom: 16px; }
.path-group-title { font-size: 12px; font-weight: 700; margin-bottom: 6px; padding: 4px 8px;
                    border-radius: 4px; display: inline-block; }
.path-group-title.essential { background: var(--essential); color: #000; }
.path-group-title.important { background: var(--important); color: #000; }
.path-group-title.useful { background: var(--useful); color: #000; }
.path-item { padding: 6px 12px; margin: 4px 0; background: var(--surface); border-radius: 4px;
             cursor: pointer; font-size: 12px; }
.path-item:hover { background: var(--border); }

/* QA History */
.qa-history-item { padding: 12px; margin: 8px 0; background: var(--surface); border-radius: 6px;
                   border-left: 3px solid var(--orange); cursor: pointer; }
.qa-history-item:hover { background: var(--border); }
.qa-history-item .qa-question { font-weight: 600; font-size: 13px; margin-bottom: 4px; }
.qa-history-item .qa-meta { font-size: 10px; color: var(--text-dim); }
.qa-history-item .qa-preview { font-size: 12px; color: var(--text-dim); margin-top: 4px;
                                display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

/* Learning plan */
.plan-container { padding: 20px; overflow-y: auto; }
.plan-month { margin-bottom: 24px; background: var(--surface); border-radius: 8px; border: 1px solid var(--border); }
.plan-month-header { padding: 12px 16px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.plan-month-header h2 { font-size: 15px; margin: 0; }
.plan-month-header .month-progress { font-size: 12px; color: var(--text-dim); }
.plan-month-body { padding: 0 16px 16px; }
.plan-week { margin-top: 12px; padding: 10px 12px; background: var(--bg); border-radius: 6px; border-left: 3px solid var(--accent); }
.plan-week h4 { font-size: 13px; color: var(--accent); margin-bottom: 6px; }
.plan-week .pw-book { font-size: 12px; color: var(--accent2); cursor: pointer; margin-bottom: 4px; }
.plan-week .pw-book:hover { text-decoration: underline; }
.plan-week .pw-tasks { list-style: none; padding: 0; }
.plan-week .pw-tasks li { font-size: 12px; padding: 3px 0; display: flex; align-items: center; gap: 6px; }
.plan-week .pw-tasks input[type=checkbox] { accent-color: var(--accent2); }
.plan-week .pw-tasks .done { text-decoration: line-through; color: var(--text-dim); }
.plan-search-btn { display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 11px;
                   background: var(--tag-bg); color: var(--accent); cursor: pointer; border: 1px solid var(--border); margin: 2px; }
.plan-search-btn:hover { background: var(--border); }
.plan-progress-bar { height: 4px; background: var(--border); border-radius: 2px; margin-top: 4px; overflow: hidden; }
.plan-progress-fill { height: 100%; background: var(--accent2); border-radius: 2px; transition: width 0.3s; }
.plan-sidebar-month { padding: 4px 8px; cursor: pointer; border-radius: 4px; font-size: 12px; display: flex; justify-content: space-between; }
.plan-sidebar-month:hover { background: var(--border); }
.plan-sidebar-month.current { color: var(--accent2); font-weight: 600; }

/* Ask tabs */
.ask-tabs { display: flex; gap: 2px; margin-bottom: 12px; }
.ask-tab { padding: 6px 14px; border-radius: 4px; cursor: pointer; font-size: 12px; font-weight: 600;
           background: var(--surface); color: var(--text-dim); border: 1px solid var(--border); }
.ask-tab.active { background: var(--orange); color: #000; border-color: var(--orange); }
.ask-tab:hover:not(.active) { background: var(--border); }

/* Follow-up suggestions */
.followup-section { margin-top: 16px; padding-top: 12px; border-top: 1px solid var(--border); }
.followup-item { padding: 4px 10px; margin: 4px 0; border-radius: 14px; border: 1px solid var(--border);
                 background: var(--surface); color: var(--text-dim); cursor: pointer; font-size: 11px;
                 display: inline-block; }
.followup-item:hover { border-color: var(--orange); color: var(--orange); }

/* Knowledge Graph */
.graph-container { position: relative; width: 100%; height: 100%; overflow: hidden; }
.graph-container svg { width: 100%; height: 100%; }
.graph-controls { position: absolute; top: 10px; left: 10px; right: 10px;
                  display: flex; gap: 8px; align-items: center; flex-wrap: wrap;
                  background: rgba(13,17,23,0.9); padding: 8px 12px; border-radius: 8px;
                  border: 1px solid var(--border); z-index: 10; }
.graph-controls label { font-size: 11px; color: var(--text-dim); display: flex; align-items: center; gap: 4px; }
.graph-controls input[type="range"] { width: 80px; accent-color: var(--accent); }
.graph-controls input[type="text"] { background: var(--bg); border: 1px solid var(--border);
                                      color: var(--text); padding: 4px 8px; border-radius: 4px;
                                      font-size: 11px; width: 140px; }
.graph-controls select { background: var(--bg); border: 1px solid var(--border);
                          color: var(--text); padding: 4px; border-radius: 4px; font-size: 11px; }
.graph-node { cursor: pointer; }
.graph-node circle { stroke: var(--border); stroke-width: 1.5px; transition: r 0.2s; }
.graph-node:hover circle { stroke: #fff; stroke-width: 2px; }
.graph-node text { fill: var(--text); font-size: 10px; pointer-events: none; }
.graph-edge { stroke: var(--border); stroke-opacity: 0.4; }
.graph-edge.highlight { stroke: var(--accent); stroke-opacity: 0.8; }
.graph-node.highlight circle { stroke: var(--accent); stroke-width: 3px; }
.graph-node.dimmed { opacity: 0.2; }
.graph-edge.dimmed { stroke-opacity: 0.05; }
.concept-detail { position: absolute; top: 60px; right: 10px; width: 300px; max-height: calc(100% - 80px);
                  background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
                  padding: 16px; overflow-y: auto; z-index: 10; font-size: 13px; }
.concept-detail h2 { font-size: 16px; color: var(--accent); margin-bottom: 4px; }
.concept-detail .concept-zh { color: var(--text-dim); font-size: 13px; margin-bottom: 8px; }
.concept-detail .concept-desc { margin-bottom: 12px; color: var(--text); line-height: 1.5; }
.concept-detail .concept-meta { font-size: 11px; color: var(--text-dim); margin-bottom: 12px; }
.concept-detail .concept-source { padding: 4px 0; border-bottom: 1px solid var(--border);
                                   cursor: pointer; font-size: 12px; }
.concept-detail .concept-source:hover { color: var(--accent); }
.concept-detail h3 { font-size: 12px; color: var(--accent); margin: 12px 0 6px; }
.bubble-map { width: 100%; height: 300px; }
.bubble-map circle { cursor: pointer; stroke: var(--border); stroke-width: 1px; }
.bubble-map circle:hover { stroke: #fff; }
.bubble-map text { fill: var(--text); font-size: 9px; pointer-events: none; text-anchor: middle; }
</style>
<script src="https://d3js.org/d3.v7.min.js"></script>
</head>
<body>
<div class="app">
  <div class="header">
    <h1>AI Philosophy Corpus</h1>
    <div class="search-bar">
      <input type="text" id="searchInput" placeholder="Search (English or Chinese)..." autofocus>
      <select id="searchMode">
        <option value="fts">Keyword</option>
        <option value="semantic">Semantic</option>
      </select>
      <button onclick="doSearch()">Search</button>
      <button class="btn-ask" id="btnAskMode" onclick="toggleAskMode()">Ask AI</button>
      <button class="btn-stats" onclick="showStats()">Stats</button>
      <label style="display:flex;align-items:center;gap:4px;font-size:12px;color:var(--text-dim)">
        <input type="checkbox" id="showZh" onchange="reRenderList()"> ZH
      </label>
    </div>
  </div>
  <div class="main">
    <div class="sidebar" id="sidebar"></div>
    <div class="list-panel" id="listPanel">
      <div class="empty-state">Search or browse to find articles</div>
    </div>
    <div class="reading-panel" id="readingPanel">
      <div class="empty-state">Select an article to read</div>
    </div>
  </div>
</div>

<script>
let currentFilters = {};
let allArticles = [];
let currentArticle = null;
let viewingZh = false;
let browseMode = 'articles'; // 'articles' or 'books'
let askMode = false;
let currentBook = null;
let bookChapters = [];
let currentChapterIdx = -1;
const topicZh = {
  'consciousness': '意识', 'alignment': 'AI对齐', 'ethics': '伦理',
  'philosophy-of-mind': '心灵哲学', 'language-understanding': '语言理解',
  'embodiment': '具身认知', 'functionalism': '功能主义', 'chinese-room': '中文房间',
  'hard-problem': '困难问题', 'turing-test': '图灵测试', 'ai-safety': 'AI安全',
  'sentience': '感知力', 'free-will': '自由意志', 'qualia': '感质',
  'superintelligence': '超级智能', 'phenomenology': '现象学', 'ontology': '本体论',
  'epistemology': '认识论', 'existentialism': '存在主义', 'causality': '因果关系',
  'evolution': '进化', 'self-reference': '自指', 'computation': '计算',
  'philosophy-of-science': '科学哲学', 'falsificationism': '证伪主义',
  'ai-critique': 'AI批判', 'philosophy-of-technology': '技术哲学',
  'cognitive-science': '认知科学', 'psychology': '心理学', 'decision-making': '决策',
  'philosophy-of-language': '语言哲学', 'virtue-ethics': '美德伦理',
  'rationalism': '理性主义', 'political-philosophy': '政治哲学',
  'writing': '写作', 'style': '风格', 'argumentation': '论证',
  'critical-thinking': '批判性思维', 'absurdism': '荒诞主义',
  'drama': '戏剧', 'storytelling': '叙事', 'logic': '逻辑', 'communication': '沟通'
};
const categoryZh = {
  'philosophy': '哲学', 'ai': '人工智能', 'epistemology': '认识论',
  'psychology': '心理学', 'writing': '写作'
};

async function init() {
  const resp = await fetch('/api/filters');
  const data = await resp.json();
  renderSidebar(data);
  loadArticles({sort: 'importance'});
}

function renderSidebar(data) {
  // Mode tabs
  let html = '<div class="mode-tabs">';
  html += `<div class="mode-tab ${browseMode==='articles'?'active':''}" onclick="switchMode('articles')">Articles</div>`;
  html += `<div class="mode-tab ${browseMode==='books'?'active':''}" onclick="switchMode('books')">Books</div>`;
  html += `<div class="mode-tab" onclick="showMyNotes()" style="background:var(--tag-bg)">Notes</div>`;
  html += `<div class="mode-tab ${browseMode==='graph'?'active':''}" onclick="switchMode('graph')">Graph</div>`;
  html += `<div class="mode-tab" onclick="showDebates()" style="background:var(--tag-bg)">Debates</div>`;
  html += `<div class="mode-tab ${browseMode==='plan'?'active':''}" onclick="switchMode('plan')" style="${browseMode==='plan'?'':'background:var(--tag-bg)'}">Plan</div>`;
  html += '</div>';

  if (browseMode === 'plan') {
    // Plan sidebar is handled below
  } else if (browseMode === 'books') {
    html += '<h3>Category</h3>';
    const cats = ['philosophy', 'ai', 'epistemology', 'psychology', 'writing'];
    cats.forEach(c => {
      html += `<div class="filter-item" onclick="toggleFilter('category','${c}')">${categoryZh[c]||c} ${c} </div>`;
    });
    html += '<h3>Language</h3>';
    html += `<div class="filter-item" onclick="toggleFilter('language','en')">English</div>`;
    html += `<div class="filter-item" onclick="toggleFilter('language','zh')">中文</div>`;
  } else {
    html += '<h3>Level</h3>';
    const levels = [
      {name: 'essential', label: '必读 Essential', cls: 'level-essential'},
      {name: 'important', label: '重要 Important', cls: 'level-important'},
      {name: 'useful', label: '有用 Useful', cls: 'level-useful'},
      {name: 'reference', label: '参考 Reference', cls: 'level-reference'}
    ];
    levels.forEach(l => {
      const cnt = data.levels?.[l.name] || 0;
      html += `<div class="filter-item" onclick="toggleFilter('level','${l.name}')">
        <span class="level-badge ${l.cls}">${l.label}</span>
        <span class="count">${cnt}</span></div>`;
    });

    html += '<h3>Sources</h3>';
    data.sources.forEach(s => {
      html += `<div class="filter-item" onclick="toggleFilter('source','${s.name}')">${s.name} <span class="count">${s.count}</span></div>`;
    });
    html += '<h3>Topics</h3>';
    data.topics.forEach(t => {
      const zh = topicZh[t.name] || t.name;
      html += `<div class="filter-item" style="gap:4px">
        <span onclick="toggleFilter('topic','${t.name}')" style="flex:1;cursor:pointer">${zh} #${t.name}</span>
        <span class="count" onclick="event.stopPropagation();showLearningPath('${t.name}')" style="cursor:pointer;color:var(--accent)" title="Learning path">&#x1F4DA;</span>
        <span class="count">${t.count}</span>
      </div>`;
    });
  }

  if (browseMode === 'graph') {
    html += '<h3>Concepts by Topic</h3>';
    html += '<div id="conceptBubbles"><div style="color:var(--text-dim);font-size:12px">Loading...</div></div>';
  }
  if (browseMode === 'plan') {
    html += '<h3>Month Navigation</h3>';
    const months = ['1: Writing Precision', '2: Argument Analysis', '3: Structured Thinking', '4: Philosophy Reading', '5: Prompt Engineering', '6: Capstone Project'];
    months.forEach((m, i) => {
      html += `<div class="plan-sidebar-month" onclick="scrollToPlanMonth(${i+1})">M${i+1} ${m.split(': ')[1]}</div>`;
    });
    html += '<h3 style="margin-top:12px">Quick Actions</h3>';
    html += '<div class="filter-item" onclick="planAsk()">Ask AI about plan</div>';
    html += '<div id="planOverallProgress" style="margin-top:12px"></div>';
  }
  document.getElementById('sidebar').innerHTML = html;
}

async function switchMode(mode) {
  browseMode = mode;
  currentFilters = {};
  const resp = await fetch('/api/filters');
  const data = await resp.json();
  renderSidebar(data);
  if (mode === 'graph') {
    loadGraph();
  } else if (mode === 'plan') {
    loadLearningPlan();
  } else {
    document.getElementById('listPanel').style.display = '';
    document.getElementById('readingPanel').style.gridColumn = '';
    if (mode === 'books') {
      loadBooks({});
    } else {
      loadArticles({sort: 'importance'});
    }
  }
}

function toggleFilter(key, val) {
  if (currentFilters[key] === val) delete currentFilters[key];
  else currentFilters[key] = val;

  document.querySelectorAll('.filter-item').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.filter-item').forEach(el => {
    const text = el.textContent.trim();
    for (const [k, v] of Object.entries(currentFilters)) {
      if (text.includes(v)) el.classList.add('active');
    }
  });
  if (browseMode === 'books') {
    loadBooks(currentFilters);
  } else {
    loadArticles({...currentFilters, sort: 'importance'});
  }
}

let articleTotal = 0;
let articleOffset = 0;
const PAGE_SIZE = 50;

async function loadArticles(params, append) {
  if (!append) articleOffset = 0;
  params.limit = PAGE_SIZE;
  params.offset = articleOffset;
  const qs = new URLSearchParams(params).toString();
  const resp = await fetch('/api/articles?' + qs);
  const data = await resp.json();
  articleTotal = data.total;
  if (append) {
    allArticles = allArticles.concat(data.articles);
  } else {
    allArticles = data.articles;
  }
  renderList(allArticles);
}

async function loadBooks(params) {
  const qs = new URLSearchParams(params).toString();
  const resp = await fetch('/api/books?' + qs);
  const books = await resp.json();
  renderBookList(books);
}

function getReadProgress(bookId) {
  try {
    const key = 'readProgress_' + bookId;
    return JSON.parse(localStorage.getItem(key)) || {lastChapter: 0, readChapters: []};
  } catch(e) { return {lastChapter: 0, readChapters: []}; }
}

function saveReadProgress(bookId, chapterIdx, totalChapters) {
  const prog = getReadProgress(bookId);
  prog.lastChapter = chapterIdx;
  if (!prog.readChapters.includes(chapterIdx)) prog.readChapters.push(chapterIdx);
  localStorage.setItem('readProgress_' + bookId, JSON.stringify(prog));
  // Sync to server
  fetch('/api/reading-progress', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({book_id: bookId, last_chapter: chapterIdx, read_chapters: prog.readChapters})
  }).catch(() => {});
}

function renderBookList(books) {
  if (!books.length) {
    document.getElementById('listPanel').innerHTML = '<div class="empty-state">No books</div>';
    return;
  }
  let html = `<div class="list-header"><span>${books.length} books</span></div>`;
  books.forEach(b => {
    const cat = categoryZh[b.category] || b.category || '';
    const prog = getReadProgress(b.id);
    const totalCh = b.chapter_count || 0;
    const readCh = prog.readChapters.length;
    const pct = totalCh > 0 ? Math.round(readCh / totalCh * 100) : 0;
    html += `<div class="book-item" onclick="loadBook(${b.id},this)">
      <div class="article-title">
        <span class="book-category">${cat}</span>
        <span class="book-lang">${b.language||''}</span>
        ${escHtml(b.title)}
      </div>
      ${b.title_zh && b.title_zh !== b.title ? '<div class="article-title-zh">' + escHtml(b.title_zh) + '</div>' : ''}
      <div class="article-meta">
        <span>${escHtml(b.author||'')}</span>
        <span>${b.year||''}</span>
        <span>${b.page_count||'?'} pages</span>
        ${totalCh ? '<span>' + totalCh + ' ch</span>' : ''}
        ${b.linked_title ? '<span style="color:var(--orange)">has ' + (b.language==='en'?'ZH':'EN') + ' version</span>' : ''}
      </div>
      ${totalCh > 0 ? '<div class="book-progress"><div class="book-progress-fill" style="width:'+pct+'%"></div></div><div class="book-progress-text">'+readCh+'/'+totalCh+' chapters read ('+pct+'%)</div>' : ''}
    </div>`;
  });
  document.getElementById('listPanel').innerHTML = html;
}

async function doSearch() {
  const q = document.getElementById('searchInput').value.trim();
  if (!q) return;

  if (askMode) {
    doAsk(q);
    return;
  }

  const mode = document.getElementById('searchMode').value;
  const resp = await fetch(`/api/search?q=${encodeURIComponent(q)}&mode=${mode}&limit=50`);
  allArticles = await resp.json();
  renderList(allArticles);
}

document.getElementById('searchInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') doSearch();
});

function reRenderList() { renderList(allArticles); }

function renderList(articles) {
  const showZh = document.getElementById('showZh').checked;
  if (!articles.length) {
    document.getElementById('listPanel').innerHTML = '<div class="empty-state">No results</div>';
    return;
  }
  let html = `<div class="list-header"><span>${articles.length}${articleTotal > articles.length ? '/' + articleTotal : ''} articles</span></div>`;
  articles.forEach(a => {
    const score = a.importance ? a.importance.toFixed(1) : '?';
    const levelCls = a.level ? 'level-' + a.level : '';
    const tags = a.topics ? JSON.parse(a.topics).map(t =>
      `<span class="tag" onclick="event.stopPropagation();toggleFilter('topic','${t}')">${topicZh[t]||t}</span>`
    ).join('') : '';
    const titleDisplay = showZh && a.title_zh ? escHtml(a.title_zh) : escHtml(a.title);
    const zhSub = showZh && a.title_zh ? '' : (a.title_zh ? `<div class="article-title-zh">${escHtml(a.title_zh)}</div>` : '');

    html += `<div class="article-item" onclick="loadArticle(${a.id},this)">
      <div class="article-title"><span class="article-score">${score}</span>
        ${a.level ? '<span class="level-badge ' + levelCls + '" style="margin-right:4px">' + ({essential:'必',important:'重',useful:'用',reference:'参'}[a.level]||a.level[0].toUpperCase()) + '</span>' : ''}
        ${titleDisplay}</div>
      ${zhSub}
      <div class="article-meta">
        <span>${escHtml(a.author || '')}</span>
        <span>${a.source}</span>
        ${a.date ? '<span>' + a.date + '</span>' : ''}
      </div>
      ${tags ? '<div class="article-tags">' + tags + '</div>' : ''}
    </div>`;
  });
  if (articleTotal > articles.length) {
    html += `<div style="text-align:center;padding:12px">
      <button onclick="loadMoreArticles()" style="background:var(--accent);color:#000;border:none;padding:6px 16px;border-radius:4px;cursor:pointer">
        Load more (${articles.length}/${articleTotal})
      </button></div>`;
  }
  document.getElementById('listPanel').innerHTML = html;
}

function loadMoreArticles() {
  articleOffset = allArticles.length;
  loadArticles({...currentFilters, sort: 'importance'}, true);
}

async function loadArticle(id, el) {
  document.querySelectorAll('.article-item').forEach(e => e.classList.remove('selected'));
  if (el) el.classList.add('selected');

  const resp = await fetch(`/api/article/${id}`);
  currentArticle = await resp.json();
  viewingZh = false;
  renderArticle();
}

function renderArticle() {
  const a = currentArticle;
  if (!a) return;

  const levelCls = a.level ? 'level-' + a.level : '';
  let html = `<h1>${escHtml(a.title)}</h1>`;
  if (a.title_zh) html += `<div class="title-zh">${escHtml(a.title_zh)}</div>`;

  html += `<div class="meta">
    ${a.level ? '<span class="level-badge ' + levelCls + '">' + ({essential:'必读',important:'重要',useful:'有用',reference:'参考'}[a.level]||a.level) + '</span>' : ''}
    ${a.author ? '<strong>' + escHtml(a.author) + '</strong>' : ''}
    <span>${a.source}</span>
    ${a.date ? '<span>' + a.date : ''}
    ${a.url ? '<a href="' + a.url + '" target="_blank">Original</a>' : ''}
    ${a.importance ? '<span>Score: ' + a.importance.toFixed(1) + '/10</span>' : ''}
  </div>`;

  // Toolbar
  html += '<div class="toolbar">';
  html += `<button onclick="toggleLang()" id="btnLang">${viewingZh ? 'View English' : 'View Chinese'}</button>`;
  if (!a.content_zh && a.content_html) {
    html += `<button onclick="translateFull(${a.id})" id="btnTranslate">Translate Full Text</button>`;
  }
  if (a.content_zh) {
    html += `<span style="color:var(--accent2);font-size:12px">Chinese translation available</span>`;
  }
  html += '</div>';
  html += '<div id="translateStatus"></div>';

  // Summary / abstract
  if (a.summary) {
    html += `<div class="info-box"><strong>Summary:</strong> ${escHtml(a.summary)}</div>`;
  }
  if (viewingZh && a.abstract_zh) {
    html += `<div class="info-box"><strong>Abstract (ZH):</strong> ${escHtml(a.abstract_zh)}</div>`;
  } else if (a.abstract && !viewingZh) {
    html += `<div class="info-box"><strong>Abstract:</strong> ${escHtml(a.abstract).substring(0, 500)}</div>`;
  }

  // Tags
  if (a.topics) {
    try {
      const tags = JSON.parse(a.topics);
      html += '<div style="margin-bottom:12px">' + tags.map(t =>
        `<span class="tag" style="font-size:12px;padding:3px 10px">${topicZh[t]||t}</span>`
      ).join(' ') + '</div>';
    } catch(e) {}
  }

  // Content
  if (viewingZh && a.content_zh_html) {
    html += `<div class="content">${a.content_zh_html}</div>`;
  } else if (viewingZh && a.abstract_zh) {
    html += `<div class="content"><p style="color:var(--text-dim)">Full Chinese translation not yet available. Click "Translate Full Text" to translate.</p></div>`;
  } else if (a.content_html) {
    html += `<div class="content">${a.content_html}</div>`;
  } else if (a.abstract) {
    html += `<div class="content"><p>${escHtml(a.abstract)}</p></div>`;
  } else {
    html += '<div class="content"><p style="color:var(--text-dim)">No content (PDF only)</p></div>';
  }

  // Notes section
  html += `<div style="margin:8px 0"><a href="/api/export/article/${a.id}" style="padding:3px 10px;border-radius:4px;border:1px solid var(--text-dim);color:var(--text-dim);font-size:11px;text-decoration:none">Export Markdown</a></div>`;
  html += renderNotesSection('article', a.id);

  // Similar
  if (a.similar && a.similar.length) {
    html += '<div class="similar-section"><h3>Similar Articles</h3>';
    a.similar.forEach(s => {
      html += `<div class="similar-item" onclick="loadArticle(${s.id})">${escHtml(s.title)} <span style="color:var(--text-dim)">[${s.source}]</span></div>`;
    });
    html += '</div>';
  }

  document.getElementById('readingPanel').innerHTML = html;
  document.getElementById('readingPanel').scrollTop = 0;
  loadNotes('article', a.id);
}

function toggleLang() {
  viewingZh = !viewingZh;
  renderArticle();
}

async function translateFull(id) {
  const btn = document.getElementById('btnTranslate');
  const status = document.getElementById('translateStatus');
  if (btn) btn.disabled = true;
  status.innerHTML = '<div class="translate-status">Translating... this may take a moment...</div>';

  try {
    const resp = await fetch(`/api/translate/${id}`, {method: 'POST'});
    const data = await resp.json();
    if (data.success) {
      status.innerHTML = '<div class="translate-status">Translation complete!</div>';
      const resp2 = await fetch(`/api/article/${id}`);
      currentArticle = await resp2.json();
      viewingZh = true;
      renderArticle();
    } else {
      status.innerHTML = `<div style="color:var(--essential)">${data.error || 'Translation failed'}</div>`;
      if (btn) btn.disabled = false;
    }
  } catch(e) {
    status.innerHTML = `<div style="color:var(--essential)">Error: ${e.message}</div>`;
    if (btn) btn.disabled = false;
  }
}

// ─── Books ───────────────────────────────────────────────────

async function loadBook(id, el) {
  document.querySelectorAll('.book-item').forEach(e => e.classList.remove('selected'));
  if (el) el.classList.add('selected');

  const resp = await fetch(`/api/book/${id}`);
  currentBook = await resp.json();
  bookChapters = currentBook.chapters || [];
  currentChapterIdx = -1;
  renderBookDetail();
}

function renderBookDetail() {
  const b = currentBook;
  if (!b) return;

  // Show chapters in list panel
  let listHtml = `<div class="list-header"><span>${b.title}</span></div>`;
  bookChapters.forEach((ch, i) => {
    listHtml += `<div class="chapter-item" onclick="loadChapter(${i}, this)">
      <span class="ch-num">${ch.chapter_num}.</span>
      <span style="flex:1">${escHtml(ch.title)}</span>
      <span class="ch-pages">p${ch.start_page}-${ch.end_page}</span>
    </div>`;
  });
  document.getElementById('listPanel').innerHTML = listHtml;

  // Book detail in reading panel
  let html = `<h1>${escHtml(b.title)}</h1>`;
  if (b.title_zh && b.title_zh !== b.title) html += `<div class="title-zh">${escHtml(b.title_zh)}</div>`;
  html += `<div class="meta">
    <strong>${escHtml(b.author||'')}</strong>
    <span>${b.year||''}</span>
    <span>${b.page_count||'?'} pages</span>
    <span class="book-category">${categoryZh[b.category]||b.category||''}</span>
    <span class="book-lang">${b.language||''}</span>
  </div>`;

  if (b.topics) {
    try {
      const tags = JSON.parse(b.topics);
      html += '<div style="margin:8px 0">' + tags.map(t =>
        `<span class="tag" style="font-size:12px;padding:3px 10px">${topicZh[t]||t}</span>`
      ).join(' ') + '</div>';
    } catch(e) {}
  }

  if (b.linked_book_id) {
    html += `<div style="margin:8px 0"><button class="toolbar button" onclick="loadBook(${b.linked_book_id})" style="padding:4px 12px;border-radius:4px;border:1px solid var(--orange);background:var(--surface);color:var(--orange);cursor:pointer;font-size:12px">View ${b.language==='en'?'Chinese':'English'} version</button></div>`;
  }

  // Overview section
  if (b.overview) {
    html += `<div class="overview-card"><h3>AI Overview</h3><div class="overview-content">${b.overview}</div></div>`;
  } else {
    html += `<div style="margin:8px 0"><button onclick="generateOverview(${b.id})" id="btnOverview" style="padding:6px 14px;border-radius:6px;border:1px solid var(--accent);background:var(--surface);color:var(--accent);cursor:pointer;font-size:12px">Generate AI Overview</button></div>`;
    html += '<div id="overviewStatus"></div>';
  }

  const prog = getReadProgress(b.id);
  const readCh = prog.readChapters.length;
  const pct = bookChapters.length > 0 ? Math.round(readCh / bookChapters.length * 100) : 0;
  html += `<div class="info-box"><strong>Chapters:</strong> ${bookChapters.length} &nbsp; <strong>Progress:</strong> ${readCh}/${bookChapters.length} (${pct}%)
    ${prog.lastChapter > 0 ? '&nbsp; <button onclick="loadChapter('+prog.lastChapter+')" style="padding:2px 8px;border-radius:4px;border:1px solid var(--accent);background:var(--surface);color:var(--accent);cursor:pointer;font-size:11px">Resume chapter '+(prog.lastChapter+1)+'</button>' : ''}
  </div>`;

  html += renderNotesSection('book', b.id);

  document.getElementById('readingPanel').innerHTML = html;
  document.getElementById('readingPanel').scrollTop = 0;
  loadNotes('book', b.id);
}

async function loadChapter(idx, el) {
  if (idx < 0 || idx >= bookChapters.length) return;
  currentChapterIdx = idx;
  const ch = bookChapters[idx];

  // Save reading progress
  if (currentBook) saveReadProgress(currentBook.id, idx, bookChapters.length);

  document.querySelectorAll('.chapter-item').forEach(e => e.classList.remove('selected'));
  if (el) el.classList.add('selected');
  // Highlight in chapter list
  if (!el) {
    const items = document.querySelectorAll('.chapter-item');
    if (items[idx]) items[idx].classList.add('selected');
  }

  const resp = await fetch(`/api/chapter/${ch.id}`);
  const data = await resp.json();
  renderChapter(data);
}

function renderChapter(ch) {
  let html = '';

  // Nav
  html += '<div class="chapter-nav">';
  html += `<button onclick="loadChapter(${currentChapterIdx-1})" ${currentChapterIdx<=0?'disabled':''}>← Prev</button>`;
  html += `<select onchange="loadChapter(parseInt(this.value))">`;
  bookChapters.forEach((c, i) => {
    html += `<option value="${i}" ${i===currentChapterIdx?'selected':''}>${c.chapter_num}. ${escHtml(c.title).substring(0,50)}</option>`;
  });
  html += '</select>';
  html += `<button onclick="loadChapter(${currentChapterIdx+1})" ${currentChapterIdx>=bookChapters.length-1?'disabled':''}>Next →</button>`;
  html += '</div>';

  html += `<h1>${escHtml(ch.title)}</h1>`;
  html += `<div class="meta">
    <span>Chapter ${ch.chapter_num}</span>
    <span>Pages ${ch.start_page}-${ch.end_page}</span>
    <span>${ch.word_count||'?'} words</span>
  </div>`;

  // Summarize button
  html += `<div class="toolbar">
    <button onclick="summarizeChapter(${ch.id})" id="btnSummarize">Summarize this chapter</button>
  </div>`;
  if (ch.summary) {
    html += `<div class="info-box"><strong>Summary:</strong> ${escHtml(ch.summary)}</div>`;
  }
  html += '<div id="chapterSummaryStatus"></div>';

  // Content
  if (ch.content) {
    html += `<div class="content"><pre style="white-space:pre-wrap;font-family:inherit;background:transparent;padding:0">${escHtml(ch.content)}</pre></div>`;
  } else {
    html += '<div class="content"><p style="color:var(--text-dim)">No text content (scanned PDF)</p></div>';
  }

  // Related content from other sources
  html += '<div class="related-section" id="relatedContent"><h3>Related from other sources</h3><div style="color:var(--text-dim);font-size:12px">Loading...</div></div>';

  // Notes
  html += renderNotesSection('chapter', ch.id);

  document.getElementById('readingPanel').innerHTML = html;
  document.getElementById('readingPanel').scrollTop = 0;
  loadNotes('chapter', ch.id);
  loadRelatedContent(ch.id, currentBook ? currentBook.id : null);
}

async function summarizeChapter(chapterId) {
  const btn = document.getElementById('btnSummarize');
  const status = document.getElementById('chapterSummaryStatus');
  if (btn) btn.disabled = true;
  status.innerHTML = '<div class="translate-status">Summarizing...</div>';

  try {
    const resp = await fetch(`/api/chapter/${chapterId}/summarize`, {method: 'POST'});
    const data = await resp.json();
    if (data.summary) {
      status.innerHTML = `<div class="info-box"><strong>Summary:</strong> ${escHtml(data.summary)}</div>`;
    } else {
      status.innerHTML = `<div style="color:var(--essential)">${data.error || 'Failed'}</div>`;
      if (btn) btn.disabled = false;
    }
  } catch(e) {
    status.innerHTML = `<div style="color:var(--essential)">Error: ${e.message}</div>`;
    if (btn) btn.disabled = false;
  }
}

// ─── Ask AI (RAG) ────────────────────────────────────────────

function toggleAskMode() {
  askMode = !askMode;
  document.getElementById('btnAskMode').classList.toggle('active', askMode);
  if (askMode) {
    showAskPanel();
  } else {
    document.getElementById('readingPanel').innerHTML = '<div class="empty-state">Select an article to read</div>';
  }
}

function showAskPanel() {
  const templates = [
    "What is the Chinese Room argument?",
    "Compare Dennett and Chalmers on consciousness",
    "Summarize Kuhn\\u0027s paradigm shifts",
    "How does Hofstadter define strange loops?",
    "What are the main critiques of AI?",
  ];

  let html = '<div class="ask-panel">';
  html += '<h1 style="margin-bottom:12px">Ask AI</h1>';

  // Tabs: Ask / History
  html += '<div class="ask-tabs">';
  html += `<div class="ask-tab ${askTab==='ask'?'active':''}" onclick="askTab='ask';showAskPanel()">Ask</div>`;
  html += `<div class="ask-tab ${askTab==='history'?'active':''}" onclick="askTab='history';showAskPanel();showQAHistory()">History</div>`;
  html += '</div>';

  if (askTab === 'history') {
    html += '<div id="askResult"><div style="color:var(--text-dim)">Loading...</div></div></div>';
    document.getElementById('readingPanel').innerHTML = html;
    showQAHistory();
    return;
  }

  html += '<p style="color:var(--text-dim);font-size:13px;margin-bottom:12px">Ask questions across all articles and books. AI will find relevant sources and answer.</p>';

  html += '<div class="ask-templates">';
  templates.forEach(t => {
    html += `<span class="ask-template" onclick="document.getElementById(&quot;askInput&quot;).value=this.textContent;doAsk(this.textContent)">${t}</span>`;
  });
  html += '</div>';

  html += '<div class="ask-input-wrap">';
  html += `<textarea id="askInput" placeholder="Ask a question about your research corpus..." onkeydown="if(event.key===&quot;Enter&quot;&&!event.shiftKey){event.preventDefault();doAsk(this.value)}"></textarea>`;
  html += `<button class="btn-ask" onclick="doAsk(document.getElementById(&quot;askInput&quot;).value)">Ask</button>`;
  html += '</div>';

  // Compare toggle
  html += '<div class="compare-toggle"><label><input type="checkbox" id="compareMode"> Compare &amp; contrast mode (multi-source analysis)</label></div>';

  html += '<div id="askResult"></div>';
  html += '</div>';

  document.getElementById('readingPanel').innerHTML = html;
}

async function doAsk(question) {
  if (!question || !question.trim()) return;

  if (!askMode) {
    askMode = true;
    askTab = 'ask';
    document.getElementById('btnAskMode').classList.add('active');
    showAskPanel();
    document.getElementById('askInput').value = question;
  }

  const compareMode = document.getElementById('compareMode') && document.getElementById('compareMode').checked;
  const askResult = document.getElementById('askResult');
  askResult.innerHTML = '<div class="ask-loading">Searching and thinking...</div>';

  try {
    const resp = await fetch('/api/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question: question.trim(), mode: compareMode ? 'compare' : 'normal', conversation_id: window._conversationId || null})
    });
    const data = await resp.json();
    if (data.conversation_id) window._conversationId = data.conversation_id;

    let html = '<div class="ask-answer">';
    html += `<div class="content" style="margin-bottom:16px">${data.answer_html || escHtml(data.answer || 'No answer')}</div>`;

    // Follow-up suggestions
    if (data.followups && data.followups.length) {
      html += '<div class="followup-section"><strong style="font-size:12px;color:var(--text-dim)">Follow-up questions:</strong><div style="margin-top:6px">';
      data.followups.forEach(f => {
        html += `<span class="followup-item" onclick="document.getElementById('askInput').value=this.textContent;doAsk(this.textContent)">${escHtml(f)}</span> `;
      });
      html += '</div></div>';
    }

    // Concept graph panel
    if (data.concepts && data.concepts.length) {
      html += '<div style="margin-top:12px;padding:8px 12px;background:rgba(255,165,0,0.08);border-radius:8px;border:1px solid rgba(255,165,0,0.2)">';
      html += '<strong style="font-size:11px;color:var(--orange)">Related Concepts</strong><div style="margin-top:4px;display:flex;flex-wrap:wrap;gap:4px">';
      data.concepts.forEach(c => {
        let tags = c.related.map(r => escHtml(r.name || r)).join(', ');
        html += `<span style="padding:2px 8px;border-radius:10px;background:rgba(255,165,0,0.15);font-size:11px;cursor:pointer" title="Related: ${tags}" onclick="document.getElementById('askInput').value='What is ${escHtml(c.name)}?';doAsk('What is ${escHtml(c.name)}?')">${escHtml(c.name)}</span>`;
      });
      html += '</div></div>';
    }

    // Arguments panel
    if (data.arguments && data.arguments.length) {
      html += '<div style="margin-top:8px;padding:8px 12px;background:rgba(100,200,255,0.08);border-radius:8px;border:1px solid rgba(100,200,255,0.2)">';
      html += '<strong style="font-size:11px;color:var(--accent)">Key Arguments from Corpus</strong>';
      data.arguments.forEach(a => {
        html += `<div style="margin-top:4px;font-size:11px;color:var(--text-dim)"><span style="color:var(--text)">&#x2022; ${escHtml(a.claim)}</span>`;
        if (a.author) html += ` <span style="font-style:italic">- ${escHtml(a.author)}</span>`;
        html += '</div>';
      });
      html += '</div>';
    }

    if (data.sources && data.sources.length) {
      html += '<h3 style="color:var(--accent);margin-bottom:8px;margin-top:16px">Sources</h3>';
      data.sources.forEach(s => {
        const onclick = s.type === 'article'
          ? `loadArticle(${s.id})`
          : s.type === 'book_chunk'
          ? `loadBook(${s.book_id})`
          : '';
        html += `<div class="source-item" onclick="${onclick}">
          <span style="color:var(--orange);font-size:10px">${s.type}</span>
          <strong>${escHtml(s.title||'')}</strong>
          ${s.author ? '<span style="color:var(--text-dim)"> - ' + escHtml(s.author) + '</span>' : ''}
          <div style="color:var(--text-dim);font-size:11px;margin-top:2px">${escHtml((s.snippet||'').substring(0,150))}</div>
        </div>`;
      });
    }
    html += '</div>';
    askResult.innerHTML = html;
  } catch(e) {
    askResult.innerHTML = `<div style="color:var(--essential)">Error: ${e.message}</div>`;
  }
}

// ─── Notes ───────────────────────────────────────────────────

function renderNotesSection(type, id) {
  const idField = type === 'article' ? 'article_id' : type === 'book' ? 'book_id' : 'chapter_id';
  return `<div class="notes-section">
    <h3 style="color:var(--accent2);font-size:13px;margin-bottom:8px">Notes</h3>
    <div id="notesList_${type}_${id}"></div>
    <textarea class="note-input" id="noteInput_${type}_${id}" placeholder="Add a note..."></textarea>
    <div style="margin-top:4px">
      <button onclick="saveNote('${type}',${id})" style="padding:4px 12px;border-radius:4px;border:1px solid var(--accent2);background:var(--surface);color:var(--accent2);cursor:pointer;font-size:12px">Save Note</button>
    </div>
  </div>`;
}

async function loadNotes(type, id) {
  const idField = type === 'article' ? 'article_id' : type === 'book' ? 'book_id' : 'chapter_id';
  try {
    const resp = await fetch(`/api/notes?${idField}=${id}`);
    const notes = await resp.json();
    const container = document.getElementById(`notesList_${type}_${id}`);
    if (!container) return;
    if (!notes.length) { container.innerHTML = ''; return; }
    let html = '';
    notes.forEach(n => {
      html += `<div class="note-item">`;
      if (n.highlight_text) html += `<div class="note-highlight">"${escHtml(n.highlight_text)}"</div>`;
      html += `<div>${escHtml(n.content)}</div>`;
      html += `<div class="note-meta">${n.created_at}${n.tags ? ' | ' + n.tags : ''}</div>`;
      html += `</div>`;
    });
    container.innerHTML = html;
  } catch(e) {}
}

async function saveNote(type, id) {
  const input = document.getElementById(`noteInput_${type}_${id}`);
  if (!input || !input.value.trim()) return;

  const body = {content: input.value.trim()};
  if (type === 'article') body.article_id = id;
  else if (type === 'book') body.book_id = id;
  else if (type === 'chapter') body.chapter_id = id;

  try {
    await fetch('/api/notes', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    });
    input.value = '';
    loadNotes(type, id);
  } catch(e) {}
}

async function showMyNotes() {
  const resp = await fetch('/api/notes');
  const notes = await resp.json();

  let html = '<h1 style="margin-bottom:12px">My Notes</h1>';
  html += '<div style="margin-bottom:12px;display:flex;gap:8px">';
  html += '<a href="/api/export/notes" style="padding:4px 12px;border-radius:4px;border:1px solid var(--accent);color:var(--accent);font-size:11px;text-decoration:none">Export Notes (MD)</a>';
  html += '<a href="/api/export/qa-history" style="padding:4px 12px;border-radius:4px;border:1px solid var(--orange);color:var(--orange);font-size:11px;text-decoration:none">Export Q&A History (MD)</a>';
  html += '</div>';
  if (!notes.length) {
    html += '<p style="color:var(--text-dim)">No notes yet. Add notes while reading articles or books.</p>';
  }
  notes.forEach(n => {
    html += `<div class="note-item">`;
    if (n.highlight_text) html += `<div class="note-highlight">"${escHtml(n.highlight_text)}"</div>`;
    html += `<div>${escHtml(n.content)}</div>`;
    let ref = '';
    if (n.article_id) ref = `<span onclick="loadArticle(${n.article_id})" style="color:var(--accent);cursor:pointer">Article #${n.article_id}</span>`;
    if (n.book_id) ref = `<span onclick="loadBook(${n.book_id})" style="color:var(--orange);cursor:pointer">Book #${n.book_id}</span>`;
    html += `<div class="note-meta">${n.created_at} ${ref} ${n.tags ? ' | ' + n.tags : ''}</div>`;
    html += `</div>`;
  });
  document.getElementById('readingPanel').innerHTML = html;
}

async function showStats() {
  const resp = await fetch('/api/stats');
  const s = await resp.json();

  let html = '<h1 style="margin-bottom:4px">Corpus Statistics</h1>';
  html += '<div class="stats-grid">';
  html += `<div class="stat-card"><h3>Total Articles</h3><div class="number">${s.total}</div></div>`;
  html += `<div class="stat-card"><h3>With Full Text</h3><div class="number">${s.with_content}</div></div>`;
  html += `<div class="stat-card"><h3>Books</h3><div class="number">${s.books||0}</div></div>`;
  html += `<div class="stat-card"><h3>Book Chapters</h3><div class="number">${s.book_chapters||0}</div></div>`;
  html += `<div class="stat-card"><h3>Chinese Titles</h3><div class="number">${s.translated_titles}</div></div>`;
  html += `<div class="stat-card"><h3>Chinese Full Text</h3><div class="number">${s.translated_full}</div></div>`;
  html += '</div>';

  // Levels
  html += '<h3 style="color:var(--accent);margin-top:20px">Article Levels</h3>';
  const levelColors = {essential: 'var(--essential)', important: 'var(--important)', useful: 'var(--useful)', reference: 'var(--reference)'};
  const maxLev = Math.max(...Object.values(s.levels));
  for (const [lev, cnt] of Object.entries(s.levels)) {
    const w = (cnt / maxLev * 100).toFixed(0);
    const levZh = {essential:'必读',important:'重要',useful:'有用',reference:'参考'}[lev]||lev;
    html += `<div class="stat-bar"><span class="stat-bar-label"><span class="level-badge level-${lev}">${levZh} ${lev}</span></span>
      <div class="stat-bar-fill" style="width:${w}%;background:${levelColors[lev]}"></div><span>${cnt}</span></div>`;
  }

  const maxSrc = Math.max(...s.sources.map(x => x.count));
  html += '<h3 style="color:var(--accent);margin-top:20px">Sources</h3>';
  s.sources.forEach(x => {
    const w = (x.count / maxSrc * 100).toFixed(0);
    html += `<div class="stat-bar"><span class="stat-bar-label">${x.name}</span>
      <div class="stat-bar-fill" style="width:${w}%"></div><span>${x.count}</span></div>`;
  });

  if (s.topics.length) {
    const maxTop = Math.max(...s.topics.map(x => x.count));
    html += '<h3 style="color:var(--accent);margin-top:20px">Topics</h3>';
    s.topics.forEach(x => {
      const w = (x.count / maxTop * 100).toFixed(0);
      html += `<div class="stat-bar"><span class="stat-bar-label">${topicZh[x.name]||x.name} #${x.name}</span>
        <div class="stat-bar-fill" style="width:${w}%;background:var(--accent2)"></div><span>${x.count}</span></div>`;
    });
  }

  // Research Dashboard
  try {
    const dashResp = await fetch('/api/dashboard');
    const dash = await dashResp.json();

    html += '<h2 style="color:var(--orange);margin-top:24px;border-top:1px solid var(--border);padding-top:16px">Research Dashboard</h2>';

    // Category coverage
    if (dash.categories.length) {
      html += '<h3 style="color:var(--accent);margin-top:12px">Coverage by Category</h3>';
      const maxCat = Math.max(...dash.categories.map(c => c.count));
      dash.categories.forEach(c => {
        const w = (c.count / maxCat * 100).toFixed(0);
        html += `<div class="stat-bar"><span class="stat-bar-label">${c.name} <span style="color:var(--text-dim)">(avg imp: ${c.avg_importance})</span></span>
          <div class="stat-bar-fill" style="width:${w}%;background:var(--orange)"></div><span>${c.count}</span></div>`;
      });
    }

    // Knowledge density
    if (dash.knowledge_density.length) {
      html += '<h3 style="color:var(--accent);margin-top:16px">Knowledge Density (concepts per category)</h3>';
      const maxD = Math.max(...dash.knowledge_density.map(d => d.concepts));
      dash.knowledge_density.forEach(d => {
        const w = (d.concepts / maxD * 100).toFixed(0);
        html += `<div class="stat-bar"><span class="stat-bar-label">${d.category}</span>
          <div class="stat-bar-fill" style="width:${w}%;background:var(--accent2)"></div><span>${d.concepts} concepts</span></div>`;
      });
    }

    // Argument topics
    if (dash.argument_topics.length) {
      html += '<h3 style="color:var(--accent);margin-top:16px">Arguments by Topic</h3>';
      const maxA = Math.max(...dash.argument_topics.map(a => a.count));
      dash.argument_topics.forEach(a => {
        const w = (a.count / maxA * 100).toFixed(0);
        html += `<div class="stat-bar"><span class="stat-bar-label">${a.topic}</span>
          <div class="stat-bar-fill" style="width:${w}%;background:#64c8ff"></div><span>${a.count}</span></div>`;
      });
    }

    // Reading progress
    if (dash.reading_progress.length) {
      html += '<h3 style="color:var(--accent);margin-top:16px">Reading Progress</h3>';
      dash.reading_progress.forEach(p => {
        html += `<div class="stat-bar"><span class="stat-bar-label">${p.book}</span>
          <div class="stat-bar-fill" style="width:${p.pct}%;background:var(--accent)"></div><span>${p.read}/${p.total} (${p.pct}%)</span></div>`;
      });
    }

    html += `<div class="stats-grid" style="margin-top:16px">
      <div class="stat-card"><h3>Q&A Sessions</h3><div class="number">${dash.qa_count}</div></div>
      <div class="stat-card"><h3>Notes</h3><div class="number">${dash.notes_count}</div></div>
    </div>`;
  } catch(e) {}

  document.getElementById('listPanel').innerHTML = '';
  document.getElementById('readingPanel').innerHTML = html;
}

async function showDebates() {
  const panel = document.getElementById('readingPanel');
  panel.innerHTML = '<div style="padding:20px"><h1>Loading debates...</h1></div>';
  const resp = await fetch('/api/contradictions?limit=30');
  const data = await resp.json();

  let html = '<h1 style="margin-bottom:4px">Academic Debates & Counterarguments</h1>';
  html += '<p style="color:var(--text-dim);font-size:12px;margin-bottom:16px">Claims paired with their counterarguments from the corpus.</p>';

  // Group by topic
  const byTopic = {};
  data.forEach(d => {
    const t = d.topic || 'General';
    if (!byTopic[t]) byTopic[t] = [];
    byTopic[t].push(d);
  });

  for (const [topic, items] of Object.entries(byTopic)) {
    html += `<h3 style="color:var(--orange);margin-top:16px;margin-bottom:8px">${escHtml(topic)}</h3>`;
    items.forEach(item => {
      html += `<div style="margin-bottom:12px;padding:10px;background:var(--surface);border-radius:8px;border-left:3px solid var(--accent)">
        <div style="font-size:13px;margin-bottom:6px"><strong>Claim:</strong> ${escHtml(item.claim)}</div>
        <div style="font-size:13px;color:var(--orange);margin-bottom:4px"><strong>Counter:</strong> ${escHtml(item.counterargument)}</div>
        <div style="font-size:10px;color:var(--text-dim)">${escHtml(item.source)}</div>
      </div>`;
    });
  }

  if (!data.length) html += '<p style="color:var(--text-dim)">No counterarguments found yet. Run argument extraction to populate.</p>';
  panel.innerHTML = html;
  document.getElementById('listPanel').innerHTML = '';
}

function escHtml(s) {
  if (!s) return '';
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

// ─── Generate Book Overview ──────────────────────────────
async function generateOverview(bookId) {
  const btn = document.getElementById('btnOverview');
  const status = document.getElementById('overviewStatus');
  if (btn) btn.disabled = true;
  if (status) status.innerHTML = '<div class="translate-status">Generating overview... this may take a moment...</div>';
  try {
    const resp = await fetch(`/api/book/${bookId}/overview`, {method: 'POST'});
    const data = await resp.json();
    if (data.overview) {
      currentBook.overview = data.overview;
      renderBookDetail();
    } else {
      if (status) status.innerHTML = `<div style="color:var(--essential)">${data.error || 'Failed'}</div>`;
      if (btn) btn.disabled = false;
    }
  } catch(e) {
    if (status) status.innerHTML = `<div style="color:var(--essential)">Error: ${e.message}</div>`;
    if (btn) btn.disabled = false;
  }
}

// ─── Related Content ─────────────────────────────────────
async function loadRelatedContent(chapterId, excludeBookId) {
  try {
    const resp = await fetch(`/api/chapter/${chapterId}/related?exclude_book=${excludeBookId||''}`);
    const data = await resp.json();
    const container = document.getElementById('relatedContent');
    if (!container) return;
    if (!data.length) {
      container.innerHTML = '<h3>Related from other sources</h3><div style="color:var(--text-dim);font-size:12px">No related content found</div>';
      return;
    }
    let html = '<h3>Related from other sources</h3>';
    data.forEach(r => {
      const onclick = r.type === 'article' ? `loadArticle(${r.id})` : `loadBook(${r.book_id})`;
      html += `<div class="related-card" onclick="${onclick}">
        <span class="related-source">${r.type === 'article' ? 'Article' : 'Book'}</span>
        <strong>${escHtml(r.title)}</strong>
        ${r.author ? ' <span style="color:var(--text-dim)">- '+escHtml(r.author)+'</span>' : ''}
        ${r.chapter ? '<div style="color:var(--accent);font-size:11px">Ch: '+escHtml(r.chapter)+'</div>' : ''}
        <div class="related-snippet">${escHtml((r.snippet||'').substring(0,150))}</div>
      </div>`;
    });
    container.innerHTML = html;
  } catch(e) {}
}

// ─── Learning Path ───────────────────────────────────────
async function showLearningPath(topic) {
  const resp = await fetch(`/api/learning-path?topic=${encodeURIComponent(topic)}`);
  const data = await resp.json();
  const groups = {essential: [], important: [], useful: []};
  data.forEach(item => {
    const g = groups[item.level] || groups.useful;
    g.push(item);
  });

  const groupLabels = {essential: 'Core Reading', important: 'Important', useful: 'Useful Background'};
  let html = `<div class="learning-path"><h1>Learning Path: ${topicZh[topic]||topic}</h1>`;
  for (const [level, items] of Object.entries(groups)) {
    if (!items.length) continue;
    html += `<div class="path-group"><div class="path-group-title ${level}">${groupLabels[level]} (${items.length})</div>`;
    items.forEach(item => {
      const onclick = item.type === 'book' ? `loadBook(${item.id})` : `loadArticle(${item.id})`;
      html += `<div class="path-item" onclick="${onclick}">
        <strong>${escHtml(item.title)}</strong>
        <span style="color:var(--text-dim)"> - ${escHtml(item.author||'')}</span>
        <span style="color:var(--orange);font-size:10px;margin-left:6px">${item.type}</span>
        ${item.description ? '<div style="color:var(--text-dim);font-size:11px;margin-top:2px">'+escHtml(item.description)+'</div>' : ''}
      </div>`;
    });
    html += '</div>';
  }
  if (!data.length) html += '<p style="color:var(--text-dim)">No content found for this topic.</p>';
  html += '</div>';
  document.getElementById('readingPanel').innerHTML = html;
}

// ─── QA History ──────────────────────────────────────────
let askTab = 'ask'; // 'ask' or 'history'

async function showQAHistory() {
  const resp = await fetch('/api/qa-history');
  const items = await resp.json();
  const container = document.getElementById('askResult') || document.getElementById('readingPanel');
  if (!items.length) {
    container.innerHTML = '<p style="color:var(--text-dim);padding:12px">No questions asked yet.</p>';
    return;
  }
  let html = '';
  items.forEach(item => {
    html += `<div class="qa-history-item" onclick="expandQAHistory(${item.id})">
      <div class="qa-question">${escHtml(item.question)}</div>
      <div class="qa-meta">${item.created_at || ''} ${item.mode === 'compare' ? '<span style="color:var(--orange)">[compare]</span>' : ''}</div>
      <div class="qa-preview">${(item.answer_preview||'').substring(0,200)}</div>
    </div>`;
  });
  container.innerHTML = html;
}

async function expandQAHistory(id) {
  const resp = await fetch(`/api/qa-history/${id}`);
  const item = await resp.json();
  const container = document.getElementById('askResult') || document.getElementById('readingPanel');
  let html = `<div class="ask-answer">
    <div style="margin-bottom:8px"><button onclick="showAskPanel()" style="padding:4px 10px;border-radius:4px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font-size:11px">Back</button>
    <span style="color:var(--text-dim);font-size:11px;margin-left:8px">${item.created_at||''}</span></div>
    <h3 style="margin-bottom:8px">${escHtml(item.question)}</h3>
    <div class="content" style="margin-bottom:16px">${item.answer_html || ''}</div>`;
  if (item.sources && item.sources.length) {
    html += '<h3 style="color:var(--accent);margin-bottom:8px">Sources</h3>';
    item.sources.forEach(s => {
      html += `<div class="source-item"><strong>${escHtml(s.title||'')}</strong></div>`;
    });
  }
  html += '</div>';
  container.innerHTML = html;
}

// ─── Knowledge Graph ─────────────────────────────────────
let graphSimulation = null;
let graphData = null;

async function loadGraph() {
  document.getElementById('listPanel').innerHTML = '';
  document.getElementById('listPanel').style.display = 'none';

  const panel = document.getElementById('readingPanel');
  panel.style.gridColumn = '2 / -1';
  panel.innerHTML = `
    <div class="graph-container" id="graphContainer">
      <div class="graph-controls">
        <label>Min mentions: <input type="range" id="graphMinMentions" min="1" max="20" value="3"
               oninput="this.nextElementSibling.textContent=this.value;refreshGraph()"><span>3</span></label>
        <label>Category: <select id="graphCategory" onchange="refreshGraph()">
          <option value="">All</option>
          <option value="philosophy">Philosophy</option>
          <option value="ai">AI</option>
          <option value="science">Science</option>
          <option value="methodology">Methodology</option>
          <option value="ethics">Ethics</option>
        </select></label>
        <label><input type="text" id="graphSearch" placeholder="Search concept..."
               oninput="highlightConcept(this.value)"></label>
      </div>
      <svg id="graphSvg"></svg>
    </div>`;

  await refreshGraph();
  loadConceptMap();
}

async function refreshGraph() {
  const min = document.getElementById('graphMinMentions')?.value || 3;
  const cat = document.getElementById('graphCategory')?.value || '';

  const params = new URLSearchParams({min_mentions: min});
  if (cat) params.set('category', cat);

  const resp = await fetch('/api/graph?' + params.toString());
  graphData = await resp.json();
  renderGraph(graphData);
}

const categoryColors = {
  philosophy: '#58a6ff', ai: '#f0883e', science: '#7ee787',
  methodology: '#d2a8ff', ethics: '#f97583'
};

function renderGraph(data) {
  const container = document.getElementById('graphContainer');
  if (!container) return;
  const svg = d3.select('#graphSvg');
  svg.selectAll('*').remove();

  const width = container.clientWidth;
  const height = container.clientHeight - 50;

  svg.attr('viewBox', [0, 0, width, height]);

  const g = svg.append('g');

  svg.call(d3.zoom().scaleExtent([0.2, 5]).on('zoom', (e) => g.attr('transform', e.transform)));

  const maxMentions = Math.max(...data.nodes.map(n => n.mention_count), 1);
  const sizeScale = d3.scaleSqrt().domain([1, maxMentions]).range([5, 30]);

  const edgeMap = {};
  data.edges.forEach(e => {
    edgeMap[e.source + '-' + e.target] = e;
    edgeMap[e.target + '-' + e.source] = e;
  });

  const links = g.append('g')
    .selectAll('line')
    .data(data.edges)
    .join('line')
    .attr('class', 'graph-edge')
    .attr('stroke-width', d => Math.max(1, d.strength * 3))
    .attr('stroke-dasharray', d => {
      if (d.relation === 'critiques') return '4,4';
      if (d.relation === 'requires') return '2,2';
      return null;
    });

  const nodeGroup = g.append('g')
    .selectAll('g')
    .data(data.nodes)
    .join('g')
    .attr('class', 'graph-node')
    .call(d3.drag()
      .on('start', (e, d) => { if (!e.active) graphSimulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; })
      .on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; })
      .on('end', (e, d) => { if (!e.active) graphSimulation.alphaTarget(0); d.fx = null; d.fy = null; })
    );

  nodeGroup.append('circle')
    .attr('r', d => sizeScale(d.mention_count))
    .attr('fill', d => categoryColors[d.category] || '#8b949e');

  nodeGroup.append('text')
    .attr('dy', d => sizeScale(d.mention_count) + 12)
    .attr('text-anchor', 'middle')
    .text(d => d.name);

  nodeGroup.on('mouseover', function(e, d) {
    const connected = new Set();
    data.edges.forEach(edge => {
      if (edge.source.id === d.id || edge.source === d.id) connected.add(edge.target.id || edge.target);
      if (edge.target.id === d.id || edge.target === d.id) connected.add(edge.source.id || edge.source);
    });
    connected.add(d.id);

    nodeGroup.classed('dimmed', n => !connected.has(n.id));
    links.classed('dimmed', l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return s !== d.id && t !== d.id;
    });
    links.classed('highlight', l => {
      const s = l.source.id || l.source;
      const t = l.target.id || l.target;
      return s === d.id || t === d.id;
    });
  }).on('mouseout', function() {
    nodeGroup.classed('dimmed', false);
    links.classed('dimmed', false).classed('highlight', false);
  });

  nodeGroup.on('click', (e, d) => showConceptDetail(d.id));

  graphSimulation = d3.forceSimulation(data.nodes)
    .force('link', d3.forceLink(data.edges).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-200))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide().radius(d => sizeScale(d.mention_count) + 5))
    .on('tick', () => {
      links
        .attr('x1', d => d.source.x).attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x).attr('y2', d => d.target.y);
      nodeGroup.attr('transform', d => `translate(${d.x},${d.y})`);
    });
}

async function showConceptDetail(conceptId) {
  document.querySelector('.concept-detail')?.remove();

  const resp = await fetch(`/api/concept/${conceptId}`);
  const c = await resp.json();

  let html = `<div class="concept-detail">
    <button onclick="this.parentElement.remove()" style="float:right;background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:16px">&times;</button>
    <h2>${escHtml(c.name)}</h2>
    ${c.name_zh ? '<div class="concept-zh">' + escHtml(c.name_zh) + '</div>' : ''}
    ${c.description ? '<div class="concept-desc">' + escHtml(c.description) + '</div>' : ''}
    <div class="concept-meta">
      <span>${c.mention_count} mentions</span>
      ${c.category ? ' &middot; <span>' + c.category + '</span>' : ''}
      ${c.first_seen_year ? ' &middot; <span>Since ' + c.first_seen_year + '</span>' : ''}
    </div>`;

  if (c.related && c.related.length) {
    html += '<h3>Related Concepts</h3>';
    c.related.forEach(r => {
      html += `<div class="concept-source" onclick="showConceptDetail(${r.id})">
        ${escHtml(r.name)} <span style="color:var(--text-dim)">(${r.relation}, ${r.mention_count})</span></div>`;
    });
  }

  if (c.sources && c.sources.length) {
    html += '<h3>Sources (' + c.sources.length + ')</h3>';
    c.sources.slice(0, 15).forEach(s => {
      const onclick = s.source_type === 'article' ? `loadArticle(${s.source_id})` : `loadBook(${s.source_id})`;
      html += `<div class="concept-source" onclick="switchMode('${s.source_type === 'article' ? 'articles' : 'books'}');${onclick}">
        <span style="color:var(--orange);font-size:10px">${s.source_type}</span>
        ${escHtml(s.title || '')} <span style="color:var(--text-dim)">- ${escHtml(s.author || '')}</span>
      </div>`;
    });
    if (c.sources.length > 15) {
      html += `<div style="color:var(--text-dim);font-size:11px">...and ${c.sources.length - 15} more</div>`;
    }
  }

  html += '</div>';
  document.getElementById('graphContainer').insertAdjacentHTML('beforeend', html);
}

function highlightConcept(query) {
  if (!graphData) return;
  query = query.toLowerCase().trim();
  if (!query) {
    // Reset: show all
    d3.selectAll('.graph-node').classed('highlight', false).style('opacity', 1);
    d3.selectAll('.graph-link').style('opacity', 0.3);
    return;
  }
  // Find matching nodes
  const matchIds = new Set();
  graphData.nodes.forEach(n => {
    if (n.name.includes(query) || (n.name_zh && n.name_zh.includes(query))) matchIds.add(n.id);
  });
  // Find neighbor nodes (connected to matches)
  const neighborIds = new Set(matchIds);
  graphData.edges.forEach(e => {
    const src = typeof e.source === 'object' ? e.source.id : e.source;
    const tgt = typeof e.target === 'object' ? e.target.id : e.target;
    if (matchIds.has(src)) neighborIds.add(tgt);
    if (matchIds.has(tgt)) neighborIds.add(src);
  });
  // Highlight matches, dim non-neighbors
  d3.selectAll('.graph-node')
    .classed('highlight', d => matchIds.has(d.id))
    .style('opacity', d => neighborIds.has(d.id) ? 1 : 0.1);
  d3.selectAll('.graph-link')
    .style('opacity', d => {
      const src = typeof d.source === 'object' ? d.source.id : d.source;
      const tgt = typeof d.target === 'object' ? d.target.id : d.target;
      return (matchIds.has(src) || matchIds.has(tgt)) ? 0.6 : 0.03;
    });
}

async function loadConceptMap() {
  const resp = await fetch('/api/concept-map');
  const data = await resp.json();
  const container = document.getElementById('conceptBubbles');
  if (!container) return;

  let html = '';
  data.slice(0, 15).forEach(t => {
    const zh = topicZh[t.topic] || t.topic;
    html += `<div style="margin-bottom:8px">
      <div class="filter-item" onclick="document.getElementById('graphCategory').value='';document.getElementById('graphSearch').value='${t.topic}';highlightConcept('${t.topic}')">
        <strong>${zh}</strong> <span class="count">${t.count}</span>
      </div>`;
    t.concepts.slice(0, 5).forEach(c => {
      html += `<div style="padding:1px 6px 1px 16px;font-size:11px;color:var(--text-dim);cursor:pointer"
                   onclick="showConceptDetail(${c.id})">
        ${escHtml(c.name)} <span style="font-size:9px">(${c.mention_count})</span></div>`;
    });
    html += '</div>';
  });
  container.innerHTML = html;
}

// ── Learning Plan ──────────────────────────────────────
let planData = null;
let planExpandedMonths = new Set();

async function loadLearningPlan() {
  document.getElementById('listPanel').style.display = 'none';
  document.getElementById('readingPanel').style.gridColumn = '2 / -1';
  const panel = document.getElementById('readingPanel');
  panel.innerHTML = '<div style="padding:20px"><h1>Loading learning plan...</h1></div>';

  const resp = await fetch('/api/plan');
  planData = await resp.json();
  renderPlan();
}

function renderPlan() {
  const panel = document.getElementById('readingPanel');
  let totalTasks = 0, doneTasks = 0;
  planData.forEach(m => m.weeks.forEach(w => {
    w.progress.forEach(p => { totalTasks++; if (p) doneTasks++; });
  }));
  const overallPct = totalTasks ? Math.round(doneTasks / totalTasks * 100) : 0;

  let html = '<div class="plan-container">';
  html += '<h1 style="margin-bottom:4px">6-Month Learning Plan</h1>';
  html += '<p style="color:var(--text-dim);font-size:13px;margin-bottom:4px">AI Philosophy + Writing + Structured Thinking</p>';
  html += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:16px">
    <div style="flex:1;height:6px;background:var(--border);border-radius:3px;overflow:hidden">
      <div style="height:100%;width:${overallPct}%;background:var(--accent2);border-radius:3px"></div>
    </div>
    <span style="font-size:12px;color:var(--accent2);font-weight:600">${doneTasks}/${totalTasks} (${overallPct}%)</span>
  </div>`;

  planData.forEach(m => {
    let mTotal = 0, mDone = 0;
    m.weeks.forEach(w => w.progress.forEach(p => { mTotal++; if (p) mDone++; }));
    const mPct = mTotal ? Math.round(mDone / mTotal * 100) : 0;
    const monthColor = mPct === 100 ? 'var(--accent2)' : mPct > 0 ? 'var(--accent)' : 'var(--orange)';

    html += `<div class="plan-month" id="plan-month-${m.month}">`;
    html += `<div class="plan-month-header" onclick="togglePlanMonth(${m.month})">
      <h2 style="color:${monthColor}">M${m.month}: ${m.title_zh} ${m.title}</h2>
      <div class="month-progress">
        <span>${mDone}/${mTotal}</span>
        <div class="plan-progress-bar" style="width:80px;display:inline-block;vertical-align:middle;margin-left:6px">
          <div class="plan-progress-fill" style="width:${mPct}%"></div>
        </div>
      </div>
    </div>`;
    html += `<div class="plan-month-body" id="plan-body-${m.month}" style="display:${planExpandedMonths.has(m.month)?'':'none'}">`;
    html += `<p style="color:var(--text-dim);font-size:12px;margin-bottom:8px;font-style:italic">${escHtml(m.theme)}</p>`;

    m.weeks.forEach(w => {
      html += '<div class="plan-week">';
      html += `<h4>W${w.week}: ${escHtml(w.title)}</h4>`;

      // Book link
      if (w.book_id && w.book_in_corpus) {
        html += `<div class="pw-book" onclick="openPlanBook(${w.book_id})">&#x1F4D6; ${escHtml(w.book_title)} <span style="color:var(--accent);font-size:10px">[in corpus]</span></div>`;
      } else {
        html += `<div style="font-size:12px;color:var(--text-dim);margin-bottom:4px">&#x1F4D6; ${escHtml(w.book_title)}</div>`;
      }

      // Tasks
      html += '<ul class="pw-tasks">';
      w.tasks.forEach((t, i) => {
        const done = w.progress[i];
        html += `<li>
          <input type="checkbox" ${done ? 'checked' : ''} onchange="togglePlanTask(${m.month},${w.week},${i})">
          <span class="${done ? 'done' : ''}">${escHtml(t)}</span>
        </li>`;
      });
      html += '</ul>';

      // Search shortcuts
      if (w.searches && w.searches.length) {
        html += '<div style="margin-top:6px">';
        w.searches.forEach((s, si) => {
          html += `<span class="plan-search-btn" data-month="${m.month}" data-week="${w.week}" data-si="${si}" onclick="planSearch(this.textContent)">${escHtml(s)}</span>`;
        });
        html += '</div>';
      }

      html += '</div>'; // plan-week
    });

    html += '</div></div>'; // plan-month-body, plan-month
  });

  html += '</div>';
  panel.innerHTML = html;

  // Update sidebar progress
  const progEl = document.getElementById('planOverallProgress');
  if (progEl) {
    progEl.innerHTML = `<h3>Overall Progress</h3>
      <div style="font-size:20px;font-weight:700;color:var(--accent2);margin:4px 0">${overallPct}%</div>
      <div class="plan-progress-bar"><div class="plan-progress-fill" style="width:${overallPct}%"></div></div>
      <div style="font-size:11px;color:var(--text-dim);margin-top:4px">${doneTasks} of ${totalTasks} tasks done</div>`;
  }
}

function togglePlanMonth(month) {
  const body = document.getElementById('plan-body-' + month);
  if (body.style.display === 'none') {
    body.style.display = '';
    planExpandedMonths.add(month);
  } else {
    body.style.display = 'none';
    planExpandedMonths.delete(month);
  }
}

function scrollToPlanMonth(month) {
  const body = document.getElementById('plan-body-' + month);
  if (body) { body.style.display = ''; planExpandedMonths.add(month); }
  const el = document.getElementById('plan-month-' + month);
  if (el) el.scrollIntoView({behavior: 'smooth', block: 'start'});
}

async function togglePlanTask(month, week, taskIdx) {
  const resp = await fetch('/api/plan/toggle', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({month, week, task_idx: taskIdx})
  });
  const result = await resp.json();
  // Update local data
  const m = planData.find(m => m.month === month);
  if (m) {
    const w = m.weeks.find(w => w.week === week);
    if (w) w.progress[taskIdx] = result.done;
  }
  renderPlan();
}

function planSearch(query) {
  // Switch to search mode and execute
  document.getElementById('searchInput').value = query;
  document.getElementById('searchMode').value = 'semantic';
  browseMode = 'articles';
  doSearch();
}

async function openPlanBook(bookId) {
  await switchMode('books');
  loadBook(bookId);
}

function planAsk() {
  askMode = true;
  document.getElementById('btnAskMode').classList.add('active');
  showAskPanel();
}

init();
</script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/filters')
def api_filters():
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT source, count(*) as cnt FROM articles GROUP BY source ORDER BY cnt DESC')
    sources = [{'name': r['source'], 'count': r['cnt']} for r in c.fetchall()]

    c.execute('SELECT topics FROM articles WHERE topics IS NOT NULL')
    topic_counts = {}
    for r in c.fetchall():
        try:
            for t in json.loads(r['topics']):
                topic_counts[t] = topic_counts.get(t, 0) + 1
        except (json.JSONDecodeError, TypeError):
            pass
    topics = [{'name': t, 'count': cnt} for t, cnt in sorted(topic_counts.items(), key=lambda x: -x[1])]

    c.execute('SELECT level, count(*) as cnt FROM articles GROUP BY level ORDER BY cnt DESC')
    levels = {r['level']: r['cnt'] for r in c.fetchall() if r['level']}

    conn.close()
    return jsonify({'sources': sources, 'topics': topics, 'levels': levels})

@app.route('/api/articles')
def api_articles():
    conn = get_db()
    c = conn.cursor()

    where = []
    params = []

    source = request.args.get('source')
    if source:
        where.append('source = ?')
        params.append(source)

    topic = request.args.get('topic')
    if topic:
        where.append('topics LIKE ?')
        params.append(f'%"{topic}"%')

    min_imp = request.args.get('min_importance')
    if min_imp:
        where.append('importance >= ?')
        params.append(float(min_imp))

    level = request.args.get('level')
    if level:
        where.append('level = ?')
        params.append(level)

    limit = int(request.args.get('limit', 50))
    offset = int(request.args.get('offset', 0))
    where_clause = 'WHERE ' + ' AND '.join(where) if where else ''
    sort = request.args.get('sort', 'importance')
    order = 'importance DESC NULLS LAST' if sort == 'importance' else 'date DESC'

    # Get total count for pagination
    c.execute(f'SELECT count(*) FROM articles {where_clause}', params)
    total = c.fetchone()[0]

    c.execute(f'''SELECT id, title, title_zh, author, date, source, importance, topics, level,
                         abstract as snippet
                  FROM articles {where_clause}
                  ORDER BY {order} LIMIT ? OFFSET ?''', params + [limit, offset])

    results = []
    for r in c.fetchall():
        results.append({
            'id': r['id'], 'title': r['title'], 'title_zh': r['title_zh'],
            'author': r['author'], 'date': r['date'], 'source': r['source'],
            'importance': r['importance'], 'topics': r['topics'], 'level': r['level'],
            'snippet': strip_frontmatter(r['snippet'] or '')[:200]
        })

    conn.close()
    return jsonify({'articles': results, 'total': total, 'offset': offset, 'limit': limit})

@app.route('/api/search')
def api_search():
    q = request.args.get('q', '')
    mode = request.args.get('mode', 'fts')
    limit = int(request.args.get('limit', 50))

    if mode == 'semantic' and chroma_articles:
        results_chroma = chroma_articles.query(
            query_texts=[q], n_results=limit
        )
        article_ids = []
        for id_str in results_chroma['ids'][0]:
            try:
                article_ids.append(int(id_str.replace('a_', '')))
            except ValueError:
                article_ids.append(int(id_str))
        if not article_ids:
            return jsonify([])

        conn = get_db()
        c = conn.cursor()
        placeholders = ','.join('?' * len(article_ids))
        c.execute(f'''SELECT id, title, title_zh, author, date, source, importance, topics, level,
                             abstract as snippet
                      FROM articles WHERE id IN ({placeholders})''', article_ids)
        rows = {r['id']: dict(r) for r in c.fetchall()}
        conn.close()

        results = []
        for aid in article_ids:
            if aid in rows:
                r = rows[aid]
                r['snippet'] = strip_frontmatter(r['snippet'] or '')[:200]
                results.append(r)
        return jsonify(results)

    # FTS search
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('''SELECT a.id, a.title, a.title_zh, a.author, a.date, a.source,
                            a.importance, a.topics, a.level,
                            snippet(articles_fts, 2, '<b>', '</b>', '...', 30) as snippet
                     FROM articles_fts
                     JOIN articles a ON a.id = articles_fts.rowid
                     WHERE articles_fts MATCH ?
                     ORDER BY bm25(articles_fts)
                     LIMIT ?''', (q, limit))
    except Exception:
        conn.close()
        return jsonify([])

    results = []
    for r in c.fetchall():
        results.append({
            'id': r['id'], 'title': r['title'], 'title_zh': r['title_zh'],
            'author': r['author'], 'date': r['date'], 'source': r['source'],
            'importance': r['importance'], 'topics': r['topics'], 'level': r['level'],
            'snippet': r['snippet'] or ''
        })

    conn.close()
    return jsonify(results)

@app.route('/api/article/<int:article_id>')
def api_article(article_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'not found'}), 404

    result = dict(row)
    # Strip frontmatter from text fields
    if result.get('abstract'):
        result['abstract'] = strip_frontmatter(result['abstract'])
    if result.get('abstract_zh'):
        result['abstract_zh'] = strip_frontmatter(result['abstract_zh'])
    # Convert markdown to HTML
    if result.get('content'):
        try:
            result['content_html'] = markdown.markdown(
                strip_frontmatter(result['content'])[:100000],
                extensions=['fenced_code', 'tables', 'toc']
            )
        except Exception:
            result['content_html'] = f'<pre>{result["content"][:50000]}</pre>'
        del result['content']
    else:
        result['content_html'] = None

    # Convert Chinese content to HTML
    if result.get('content_zh'):
        try:
            result['content_zh_html'] = markdown.markdown(
                strip_frontmatter(result['content_zh'])[:100000],
                extensions=['fenced_code', 'tables', 'toc']
            )
        except Exception:
            result['content_zh_html'] = f'<pre>{result["content_zh"][:50000]}</pre>'
        del result['content_zh']
    else:
        result['content_zh_html'] = None

    # Similar articles — use article_chunks for better precision
    result['similar'] = []
    search_col = chroma_article_chunks or chroma_articles
    if search_col:
        try:
            query_text = result['title'] + ' ' + (result.get('abstract') or '')[:300]
            similar = search_col.query(query_texts=[query_text], n_results=20)
            seen_ids = {article_id}
            for sid, meta in zip(similar['ids'][0], similar['metadatas'][0]):
                aid = meta.get('article_id') if chroma_article_chunks else None
                if aid is None:
                    try:
                        aid = int(sid.replace('a_', '').replace('ac_', ''))
                    except ValueError:
                        continue
                if aid not in seen_ids:
                    seen_ids.add(aid)
                    result['similar'].append({
                        'id': aid,
                        'title': meta.get('title', ''),
                        'source': meta.get('source', '')
                    })
                if len(result['similar']) >= 5:
                    break
        except Exception:
            pass

    return jsonify(result)

@app.route('/api/translate/<int:article_id>', methods=['POST'])
def api_translate(article_id):
    if not deepseek_client:
        return jsonify({'success': False, 'error': 'DeepSeek API not configured.'})

    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT title, content, content_zh FROM articles WHERE id = ?', (article_id,))
    row = c.fetchone()

    if not row:
        conn.close()
        return jsonify({'success': False, 'error': 'Article not found'})

    if row['content_zh']:
        conn.close()
        return jsonify({'success': True, 'message': 'Already translated'})

    if not row['content']:
        conn.close()
        return jsonify({'success': False, 'error': 'No content to translate (PDF only)'})

    content = row['content']

    MAX_CHUNK = 6000
    chunks = []
    if len(content) <= MAX_CHUNK:
        chunks = [content]
    else:
        paragraphs = content.split('\n\n')
        current = ''
        for p in paragraphs:
            if len(current) + len(p) > MAX_CHUNK and current:
                chunks.append(current)
                current = p
            else:
                current = current + '\n\n' + p if current else p
        if current:
            chunks.append(current)

    translated_parts = []
    try:
        for chunk in chunks:
            r = deepseek_client.chat.completions.create(
                model='deepseek-chat',
                max_tokens=8192,
                messages=[{'role': 'user', 'content':
                    'Translate this article text into Chinese. Maintain markdown formatting. '
                    'Translate naturally and accurately. Keep code blocks, URLs, and proper nouns unchanged.\n\n'
                    + chunk}]
            )
            translated_parts.append(r.choices[0].message.content.strip())
            time.sleep(0.3)

        content_zh = '\n\n'.join(translated_parts)
        c.execute('UPDATE articles SET content_zh = ? WHERE id = ?', (content_zh, article_id))
        conn.commit()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        conn.close()
        return jsonify({'success': False, 'error': str(e)})

# ─── Book API endpoints ──────────────────────────────────────────

@app.route('/api/books')
def api_books():
    conn = get_db()
    c = conn.cursor()

    where = []
    params = []

    category = request.args.get('category')
    if category:
        where.append('b.category = ?')
        params.append(category)

    language = request.args.get('language')
    if language:
        where.append('b.language = ?')
        params.append(language)

    where_clause = 'WHERE ' + ' AND '.join(where) if where else ''

    c.execute(f'''SELECT b.id, b.title, b.title_zh, b.author, b.year, b.language,
                         b.page_count, b.category, b.importance, b.topics, b.level,
                         b.linked_book_id,
                         lb.title as linked_title,
                         (SELECT COUNT(*) FROM book_chapters WHERE book_id = b.id) as chapter_count
                  FROM books b
                  LEFT JOIN books lb ON b.linked_book_id = lb.id
                  {where_clause}
                  ORDER BY b.importance DESC''', params)

    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(results)

@app.route('/api/book/<int:book_id>')
def api_book(book_id):
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        return jsonify({'error': 'not found'}), 404

    result = dict(row)

    c.execute('''SELECT id, chapter_num, title, start_page, end_page, word_count, summary
                 FROM book_chapters WHERE book_id = ? ORDER BY chapter_num''', (book_id,))
    result['chapters'] = [dict(r) for r in c.fetchall()]

    conn.close()
    return jsonify(result)

@app.route('/api/chapter/<int:chapter_id>')
def api_chapter(chapter_id):
    conn = get_db()
    c = conn.cursor()

    c.execute('''SELECT bc.*, b.title as book_title, b.author as book_author
                 FROM book_chapters bc
                 JOIN books b ON bc.book_id = b.id
                 WHERE bc.id = ?''', (chapter_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        return jsonify({'error': 'not found'}), 404

    return jsonify(dict(row))

@app.route('/api/chapter/<int:chapter_id>/summarize', methods=['POST'])
def api_summarize_chapter(chapter_id):
    if not deepseek_client:
        return jsonify({'error': 'DeepSeek API not configured'})

    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT content, summary, title FROM book_chapters WHERE id = ?', (chapter_id,))
    row = c.fetchone()

    if not row:
        conn.close()
        return jsonify({'error': 'Chapter not found'})

    if row['summary']:
        conn.close()
        return jsonify({'summary': row['summary']})

    if not row['content'] or len(row['content'].strip()) < 50:
        conn.close()
        return jsonify({'error': 'Not enough text to summarize'})

    try:
        text = row['content'][:8000]
        r = deepseek_client.chat.completions.create(
            model='deepseek-chat',
            max_tokens=1000,
            messages=[{'role': 'user', 'content':
                f'Summarize this book chapter in 3-5 sentences. Title: {row["title"]}\n\n{text}'}]
        )
        summary = r.choices[0].message.content.strip()
        c.execute('UPDATE book_chapters SET summary = ? WHERE id = ?', (summary, chapter_id))
        conn.commit()
        conn.close()
        return jsonify({'summary': summary})
    except Exception as e:
        conn.close()
        return jsonify({'error': str(e)})

# ─── RAG Ask endpoint ────────────────────────────────────────────

@app.route('/api/ask', methods=['POST'])
def api_ask():
    if not deepseek_client:
        return jsonify({'error': 'DeepSeek API not configured'})

    data = request.get_json()
    question = data.get('question', '').strip()
    if not question:
        return jsonify({'error': 'No question provided'})

    conversation_id = data.get('conversation_id')
    if not conversation_id:
        import uuid
        conversation_id = str(uuid.uuid4())[:8]

    sources = []
    context_parts = []
    CONTEXT_BUDGET = 16000  # total chars for RAG context

    # ── Step 0: Chinese query detection & translation ──
    import re as _re
    has_chinese = bool(_re.search(r'[\u4e00-\u9fff]', question))
    english_query = question
    if has_chinese:
        try:
            tr_resp = deepseek_client.chat.completions.create(
                model='deepseek-chat',
                messages=[{'role': 'user', 'content': f'Translate this question to English. Output ONLY the translation, nothing else:\n{question}'}],
                max_tokens=200, temperature=0.1
            )
            english_query = tr_resp.choices[0].message.content.strip()
        except Exception:
            pass

    # ── Step 0.5: Concept-aware query expansion ──
    expanded_terms = []
    concept_context_data = []  # For A3: concept injection
    try:
        conn_c = get_db()
        # Extract words from query, find matching concepts
        query_words = [w.lower() for w in english_query.split() if len(w) > 3]
        found_concepts = []
        for w in query_words:
            rows = conn_c.execute(
                'SELECT id, name, description, category FROM concepts WHERE LOWER(name) LIKE ? ORDER BY mention_count DESC LIMIT 2',
                (f'%{w}%',)
            ).fetchall()
            for r in rows:
                if r['id'] not in [fc['id'] for fc in found_concepts]:
                    found_concepts.append(dict(r))
        # Also try full phrase match
        phrase_rows = conn_c.execute(
            'SELECT id, name, description, category FROM concepts WHERE LOWER(name) LIKE ? ORDER BY mention_count DESC LIMIT 3',
            (f'%{english_query.lower()[:50]}%',)
        ).fetchall()
        for r in phrase_rows:
            if r['id'] not in [fc['id'] for fc in found_concepts]:
                found_concepts.append(dict(r))

        # Get related concepts for expansion
        for concept in found_concepts[:5]:
            related = conn_c.execute(
                '''SELECT c.name, cr.relation FROM concept_relations cr
                   JOIN concepts c ON (CASE WHEN cr.concept_a = ? THEN cr.concept_b ELSE cr.concept_a END) = c.id
                   WHERE (cr.concept_a = ? OR cr.concept_b = ?) AND cr.strength >= 0.7
                   ORDER BY cr.strength DESC LIMIT 4''',
                (concept['id'], concept['id'], concept['id'])
            ).fetchall()
            for rel in related:
                if rel['name'].lower() not in english_query.lower():
                    expanded_terms.append(rel['name'])
            concept_context_data.append({
                'name': concept['name'],
                'description': concept.get('description', ''),
                'category': concept.get('category', ''),
                'related': [{'name': r['name'], 'relation': r['relation']} for r in related]
            })
        conn_c.close()
    except Exception:
        pass

    # ── Step 1: Dual-path retrieval (original + HyDE) ──
    hyde_query = english_query
    try:
        hyde_resp = deepseek_client.chat.completions.create(
            model='deepseek-chat',
            messages=[{'role': 'user', 'content': f'Write a 200-word academic paragraph answering: {english_query}'}],
            max_tokens=300, temperature=0.7
        )
        hyde_query = hyde_resp.choices[0].message.content.strip()
    except Exception:
        pass

    # ── Step 2: Collect candidates from all query paths ──
    candidates = []
    seen_chunk_ids = set()

    def _strip_chunk_prefix(text):
        """Remove [Title by Author] prefix from chunk for cleaner reranking."""
        if text and text.startswith('['):
            nl = text.find('\n')
            if nl != -1 and nl < 200:
                return text[nl + 1:]
        return text

    def _search_article_chunks(query_text, n=15):
        if not chroma_article_chunks:
            return
        try:
            results = chroma_article_chunks.query(query_texts=[query_text], n_results=n, include=['metadatas', 'documents', 'distances'])
            for sid, meta, doc, dist in zip(results['ids'][0], results['metadatas'][0], results['documents'][0], results['distances'][0]):
                cid = meta.get('chunk_id', sid)
                if cid in seen_chunk_ids:
                    continue
                seen_chunk_ids.add(cid)
                candidates.append({
                    'type': 'article', 'id': meta.get('article_id', 0), 'distance': dist,
                    'title': meta.get('title', ''), 'author': meta.get('author', ''),
                    'full_text': doc or '', 'clean_text': _strip_chunk_prefix(doc or ''),
                    'importance': 0  # filled later
                })
        except Exception:
            pass

    def _search_book_chunks(query_text, n=10):
        if not chroma_books:
            return
        try:
            results = chroma_books.query(query_texts=[query_text], n_results=n, include=['metadatas', 'documents', 'distances'])
            conn2 = get_db()
            c2 = conn2.cursor()
            for sid, meta, doc, dist in zip(results['ids'][0], results['metadatas'][0], results['documents'][0], results['distances'][0]):
                chunk_id = int(sid.replace('bc_', ''))
                if chunk_id in seen_chunk_ids:
                    continue
                seen_chunk_ids.add(chunk_id)
                c2.execute('SELECT content FROM book_chunks WHERE id = ?', (chunk_id,))
                row = c2.fetchone()
                full_text = (row['content'] if row else doc)
                candidates.append({
                    'type': 'book_chunk', 'id': chunk_id, 'distance': dist,
                    'book_id': meta.get('book_id'),
                    'title': meta.get('book_title', ''), 'chapter': meta.get('chapter_title', ''),
                    'author': meta.get('author', ''),
                    'full_text': full_text, 'clean_text': full_text
                })
            conn2.close()
        except Exception:
            pass

    # Argument-level search results (structured claims)
    argument_results = []
    def _search_arguments(query_text, n=6):
        if not chroma_arguments:
            return
        try:
            results = chroma_arguments.query(query_texts=[query_text], n_results=n, include=['metadatas', 'distances'])
            conn_a = get_db()
            for meta, dist in zip(results['metadatas'][0], results['distances'][0]):
                aid = meta.get('argument_id', 0)
                row = conn_a.execute(
                    'SELECT claim, evidence, counterargument, topic FROM arguments WHERE id = ?', (aid,)
                ).fetchone()
                if row and dist < 0.6:  # Only include reasonably close matches
                    argument_results.append({
                        'claim': row['claim'],
                        'evidence': row['evidence'],
                        'counter': row['counterargument'],
                        'topic': row['topic'],
                        'source_title': meta.get('title', ''),
                        'source_author': meta.get('author', ''),
                        'distance': dist
                    })
            conn_a.close()
        except Exception:
            pass

    # Path A: original query (captures exact-match style results)
    _search_article_chunks(english_query, n=12)
    _search_book_chunks(english_query, n=8)
    # Path B: HyDE query (captures semantic/conceptual results)
    if hyde_query != english_query:
        _search_article_chunks(hyde_query, n=12)
        _search_book_chunks(hyde_query, n=8)
    # Path C: concept-expanded queries (captures related concepts)
    for term in expanded_terms[:4]:
        _search_article_chunks(term, n=4)
        _search_book_chunks(term, n=3)
    # Path D: argument search
    _search_arguments(english_query, n=6)

    # ── Step 3: Deduplicate by source ──
    # Keep best candidate per article_id / (book_id+chapter)
    deduped = {}
    for c in candidates:
        if c['type'] == 'article':
            key = ('article', c['id'])
        else:
            key = ('book', c.get('book_id', 0), c.get('chapter', ''))
        if key not in deduped or c['distance'] < deduped[key]['distance']:
            deduped[key] = c
    candidates = list(deduped.values())

    # ── Step 3.5: Lookup importance scores ──
    article_ids = [c['id'] for c in candidates if c['type'] == 'article' and c['id']]
    if article_ids:
        try:
            conn_imp = get_db()
            placeholders = ','.join('?' * len(article_ids))
            rows = conn_imp.execute(
                f'SELECT id, importance FROM articles WHERE id IN ({placeholders})', article_ids
            ).fetchall()
            imp_map = {r['id']: r['importance'] or 0 for r in rows}
            for c in candidates:
                if c['type'] == 'article':
                    c['importance'] = imp_map.get(c['id'], 0)
        except Exception:
            pass

    # ── Step 4: Cross-encoder reranking ──
    # Use clean_text (no prefix) so reranker sees actual content
    if candidates and reranker:
        try:
            pairs = [(english_query, c['clean_text'][:512]) for c in candidates]
            scores = reranker.predict(pairs)
            for c, s in zip(candidates, scores):
                # Importance boost: up to +0.5 for importance=10
                imp_boost = (c.get('importance', 0) or 0) * 0.05
                c['rerank_score'] = float(s) + imp_boost
            candidates.sort(key=lambda x: x.get('rerank_score', 0), reverse=True)
        except Exception:
            candidates.sort(key=lambda x: x['distance'])
    else:
        candidates.sort(key=lambda x: x['distance'])

    # ── Step 5: Source diversity enforcement ──
    # Ensure at least 2 different authors in top results
    final = []
    seen_authors = {}
    for c in candidates:
        author = c.get('author', 'unknown')
        author_count = seen_authors.get(author, 0)
        if author_count >= 3:  # max 3 sources from same author
            continue
        seen_authors[author] = author_count + 1
        final.append(c)
        if len(final) >= 10:
            break
    candidates = final

    # ── Step 6: Build structured context for LLM ──
    budget_remaining = CONTEXT_BUDGET
    for rank, cand in enumerate(candidates):
        # Top-ranked sources get more budget
        if rank < 3:
            max_alloc = 3000
        elif rank < 6:
            max_alloc = 2000
        else:
            max_alloc = 1000
        alloc = min(len(cand['clean_text']), max_alloc, budget_remaining)
        snippet = cand['clean_text'][:alloc]
        budget_remaining -= len(snippet)

        src_num = len(sources) + 1
        # Include relevance indicator for LLM
        relevance = 'HIGH' if rank < 3 else ('MED' if rank < 6 else 'LOW')

        if cand['type'] == 'article':
            sources.append({
                'type': 'article', 'id': cand['id'],
                'title': cand['title'], 'author': cand['author'],
                'snippet': snippet[:300], 'relevance': relevance
            })
            context_parts.append(
                f"[{src_num}] (Relevance: {relevance}) Article: \"{cand['title']}\" by {cand['author']}\n{snippet}")
        else:
            sources.append({
                'type': 'book_chunk', 'book_id': cand.get('book_id'),
                'title': cand['title'], 'chapter': cand.get('chapter', ''),
                'author': cand['author'], 'snippet': snippet[:300], 'relevance': relevance
            })
            context_parts.append(
                f"[{src_num}] (Relevance: {relevance}) Book: \"{cand['title']}\" Ch: \"{cand.get('chapter','')}\" by {cand['author']}\n{snippet}")

        if budget_remaining <= 0:
            break

    if not context_parts:
        return jsonify({'answer': 'No relevant sources found.', 'sources': []})

    context = '\n\n---\n\n'.join(context_parts)
    mode = data.get('mode', 'normal')

    # ── Concept graph context ──
    concept_section = ''
    if concept_context_data:
        parts = []
        for cd in concept_context_data[:3]:
            desc = cd.get('description', '')[:150]
            rels = ', '.join(f"{r['relation']}→{r['name']}" for r in cd.get('related', [])[:5])
            parts.append(f"• {cd['name']} ({cd.get('category','')}) — {desc}" + (f"\n  Relations: {rels}" if rels else ''))
        concept_section = '\n\nKey concepts from knowledge graph:\n' + '\n'.join(parts) + '\n'

    # ── Structured arguments context ──
    argument_section = ''
    if argument_results:
        # Dedup by claim similarity (simple: skip if claim starts same)
        seen_claims = set()
        arg_parts = []
        for ar in sorted(argument_results, key=lambda x: x['distance'])[:5]:
            claim_key = ar['claim'][:50].lower()
            if claim_key in seen_claims:
                continue
            seen_claims.add(claim_key)
            arg_parts.append(
                f"• CLAIM: {ar['claim']}\n  EVIDENCE: {ar['evidence']}\n  COUNTER: {ar['counter']}\n  Source: {ar['source_title'][:50]} by {ar['source_author']}"
            )
        if arg_parts:
            argument_section = '\n\nExtracted arguments from corpus:\n' + '\n'.join(arg_parts) + '\n'

    # Multi-turn: include conversation history
    history = data.get('history', [])
    history_text = ''
    if not history and conversation_id:
        # Load from DB
        try:
            conn_h = get_db()
            prev = conn_h.execute(
                "SELECT question, answer_html FROM qa_history WHERE conversation_id = ? ORDER BY id DESC LIMIT 2",
                (conversation_id,)
            ).fetchall()
            history = [{'question': r['question'], 'answer': r['answer_html'][:500]} for r in reversed(prev)]
        except Exception:
            pass
    if history:
        history_parts = []
        for h in history[-2:]:
            history_parts.append(f"Q: {h.get('question', '')}\nA: {h.get('answer', '')[:500]}")
        history_text = '\n\nPrevious conversation:\n' + '\n---\n'.join(history_parts) + '\n'

    # ── Build final prompt ──
    enrichment = concept_section + argument_section + history_text

    if mode == 'compare':
        prompt = f"""Compare and contrast what these sources say about the following question.
For each source, summarize its position clearly. Then highlight key agreements and disagreements.
Answer in the same language as the question. Cite sources using [Author, Title] format.
{enrichment}
Sources:
{context}

Question: {question}

After your answer, on a new line starting with "FOLLOWUPS:", suggest 3 follow-up questions (one per line)."""
    else:
        prompt = f"""Based on the following sources, answer the question. Cite sources using [Author, Title] format.
Answer in the same language as the question. Be thorough but concise.
If relevant arguments are provided, integrate them into your analysis showing different positions.
{enrichment}
Sources:
{context}

Question: {question}

After your answer, on a new line starting with "FOLLOWUPS:", suggest 3 follow-up questions (one per line)."""

    try:
        r = deepseek_client.chat.completions.create(
            model='deepseek-chat',
            max_tokens=2500,
            messages=[{'role': 'user', 'content': prompt}]
        )
        raw_answer = r.choices[0].message.content.strip()

        # Extract follow-ups
        followups = []
        answer = raw_answer
        if 'FOLLOWUPS:' in raw_answer:
            parts = raw_answer.split('FOLLOWUPS:', 1)
            answer = parts[0].strip()
            followup_lines = parts[1].strip().split('\n')
            for line in followup_lines:
                line = line.strip().lstrip('0123456789.-) ')
                if line and len(line) > 5:
                    followups.append(line)
            followups = followups[:3]

        answer_html = markdown.markdown(answer, extensions=['fenced_code', 'tables'])

        # Save to qa_history
        try:
            conn2 = get_db()
            # Ensure conversation_id column exists
            try:
                conn2.execute("ALTER TABLE qa_history ADD COLUMN conversation_id TEXT")
            except Exception:
                pass
            conn2.execute(
                "INSERT INTO qa_history (question, answer_html, sources_json, mode, conversation_id, created_at) VALUES (?,?,?,?,?,datetime('now'))",
                (question, answer_html, json.dumps(sources), mode, conversation_id))
            conn2.commit()
            conn2.close()
        except Exception:
            pass

        # Build concept/argument metadata for frontend
        concepts_used = []
        for cd in concept_context_data[:5]:
            concepts_used.append({
                'name': cd['name'],
                'related': cd.get('related', [])[:5]
            })
        arguments_used = []
        for ar in sorted(argument_results, key=lambda x: x['distance'])[:5]:
            arguments_used.append({
                'claim': ar['claim'][:200],
                'topic': ar.get('topic', ''),
                'title': ar.get('title', ''),
                'author': ar.get('author', ''),
            })

        return jsonify({
            'answer': answer, 'answer_html': answer_html,
            'sources': sources, 'followups': followups,
            'concepts': concepts_used, 'arguments': arguments_used,
            'conversation_id': conversation_id
        })
    except Exception as e:
        return jsonify({'answer': f'Error: {str(e)}', 'sources': sources, 'followups': []})

# ─── Book Overview endpoint ───────────────────────────────────────

@app.route('/api/book/<int:book_id>/overview', methods=['POST'])
def api_book_overview(book_id):
    if not deepseek_client:
        return jsonify({'error': 'DeepSeek API not configured'})

    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT overview, title, author FROM books WHERE id = ?', (book_id,))
    book = c.fetchone()
    if not book:
        conn.close()
        return jsonify({'error': 'Book not found'})

    if book['overview']:
        conn.close()
        return jsonify({'overview': book['overview']})

    # Get first 5 chapters content
    c.execute('SELECT title, content FROM book_chapters WHERE book_id = ? ORDER BY chapter_num LIMIT 5', (book_id,))
    chapters = c.fetchall()
    if not chapters:
        conn.close()
        return jsonify({'error': 'No chapters found'})

    ch_texts = []
    for ch in chapters:
        text = (ch['content'] or '')[:2000]
        ch_texts.append(f"Chapter: {ch['title']}\n{text}")
    all_text = '\n\n---\n\n'.join(ch_texts)

    # Count related articles
    related_count = 0
    if chroma_articles:
        try:
            results = chroma_articles.query(query_texts=[book['title']], n_results=10)
            related_count = len(results['ids'][0])
        except Exception:
            pass

    try:
        prompt = f"""Based on these excerpts from "{book['title']}" by {book['author']}, generate a concise book overview in the SAME language as the book content:

1. Core arguments (3-5 sentences)
2. Chapter structure guide (one sentence per chapter shown)
3. Recommended key chapters to focus on

{all_text}"""

        r = deepseek_client.chat.completions.create(
            model='deepseek-chat',
            max_tokens=1500,
            messages=[{'role': 'user', 'content': prompt}]
        )
        overview = r.choices[0].message.content.strip()
        overview_html = markdown.markdown(overview, extensions=['fenced_code', 'tables'])

        if related_count > 0:
            overview_html += f'<p style="color:var(--accent);margin-top:12px">This book relates to {related_count} articles in the corpus.</p>'

        c.execute('UPDATE books SET overview = ? WHERE id = ?', (overview_html, book_id))
        conn.commit()
        conn.close()
        return jsonify({'overview': overview_html})
    except Exception as e:
        conn.close()
        return jsonify({'error': str(e)})

# ─── Chapter Related Content endpoint ────────────────────────────

@app.route('/api/chapter/<int:chapter_id>/related')
def api_chapter_related(chapter_id):
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT content, book_id FROM book_chapters WHERE id = ?', (chapter_id,))
    row = c.fetchone()
    if not row or not row['content']:
        conn.close()
        return jsonify([])

    query_text = row['content'][:500]
    exclude_book = request.args.get('exclude_book', type=int) or row['book_id']
    results_list = []

    # Search articles
    if chroma_articles:
        try:
            results = chroma_articles.query(query_texts=[query_text], n_results=5, include=['metadatas', 'documents', 'distances'])
            for sid, meta, dist in zip(results['ids'][0], results['metadatas'][0], results['distances'][0]):
                try:
                    aid = int(sid.replace('a_', ''))
                except ValueError:
                    aid = int(sid)
                results_list.append({
                    'type': 'article', 'id': aid, 'distance': dist,
                    'title': meta.get('title', ''), 'author': meta.get('author', ''),
                    'snippet': (results['documents'][0][results['ids'][0].index(sid)] or '')[:150]
                })
        except Exception:
            pass

    # Search other books
    if chroma_books:
        try:
            results = chroma_books.query(query_texts=[query_text], n_results=8, include=['metadatas', 'documents', 'distances'])
            for sid, meta, dist in zip(results['ids'][0], results['metadatas'][0], results['distances'][0]):
                book_id = meta.get('book_id')
                if book_id == exclude_book:
                    continue
                results_list.append({
                    'type': 'book', 'id': meta.get('chunk_id'), 'book_id': book_id,
                    'distance': dist,
                    'title': meta.get('book_title', ''), 'chapter': meta.get('chapter_title', ''),
                    'author': meta.get('author', ''),
                    'snippet': (results['documents'][0][results['ids'][0].index(sid)] or '')[:150]
                })
        except Exception:
            pass

    results_list.sort(key=lambda x: x['distance'])
    conn.close()
    return jsonify(results_list[:8])

# ─── Learning Path endpoint ──────────────────────────────────────

@app.route('/api/learning-path')
def api_learning_path():
    topic = request.args.get('topic', '').strip()
    if not topic:
        return jsonify([])

    conn = get_db()
    c = conn.cursor()

    items = []

    # Books matching topic
    c.execute('SELECT id, title, author, topics, importance, level FROM books')
    for row in c.fetchall():
        topics = json.loads(row['topics'] or '[]')
        if topic in topics:
            items.append({
                'type': 'book', 'id': row['id'],
                'title': row['title'], 'author': row['author'],
                'level': row['level'] or 'useful',
                'importance': row['importance'] or 0,
                'description': f"Book, {row['author']}"
            })

    # Articles matching topic
    c.execute('SELECT id, title, author, topics, importance, level, abstract FROM articles WHERE topics IS NOT NULL')
    for row in c.fetchall():
        try:
            topics = json.loads(row['topics'] or '[]')
        except (json.JSONDecodeError, TypeError):
            continue
        if topic in topics:
            desc = (row['abstract'] or '')[:80]
            items.append({
                'type': 'article', 'id': row['id'],
                'title': row['title'], 'author': row['author'] or '',
                'level': row['level'] or 'useful',
                'importance': row['importance'] or 0,
                'description': desc
            })

    # Sort by importance within each level
    items.sort(key=lambda x: (-x['importance'],))
    conn.close()
    return jsonify(items)

# ─── QA History endpoints ────────────────────────────────────────

@app.route('/api/qa-history')
def api_qa_history():
    conn = get_db()
    c = conn.cursor()
    try:
        c.execute('''SELECT id, question, mode, created_at,
                     substr(answer_html, 1, 300) as answer_preview
                     FROM qa_history ORDER BY id DESC LIMIT 50''')
        results = [dict(r) for r in c.fetchall()]
    except Exception:
        results = []
    conn.close()
    return jsonify(results)

@app.route('/api/qa-history/<int:qa_id>')
def api_qa_history_detail(qa_id):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM qa_history WHERE id = ?', (qa_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return jsonify({'error': 'not found'}), 404
    result = dict(row)
    try:
        result['sources'] = json.loads(result.get('sources_json') or '[]')
    except Exception:
        result['sources'] = []
    return jsonify(result)

# ─── Concept Graph API ────────────────────────────────────────────

@app.route('/api/graph')
def api_graph():
    conn = get_db()
    c = conn.cursor()

    min_mentions = request.args.get('min_mentions', 3, type=int)
    category = request.args.get('category')
    year_start = request.args.get('year_start')
    year_end = request.args.get('year_end')

    where = ['mention_count >= ?']
    params = [min_mentions]

    if category:
        where.append('category = ?')
        params.append(category)
    if year_start:
        where.append("(first_seen_year IS NULL OR first_seen_year >= ?)")
        params.append(year_start)
    if year_end:
        where.append("(first_seen_year IS NULL OR first_seen_year <= ?)")
        params.append(year_end)

    where_clause = ' AND '.join(where)

    c.execute(f'''SELECT id, name, name_zh, category, mention_count,
                         first_seen_year, peak_year, description
                  FROM concepts WHERE {where_clause}
                  ORDER BY mention_count DESC''', params)
    nodes = [dict(r) for r in c.fetchall()]
    node_ids = {n['id'] for n in nodes}

    # Get edges between visible nodes
    edges = []
    if node_ids:
        placeholders = ','.join('?' * len(node_ids))
        c.execute(f'''SELECT concept_a as source, concept_b as target, relation, strength
                      FROM concept_relations
                      WHERE concept_a IN ({placeholders}) AND concept_b IN ({placeholders})''',
                  list(node_ids) + list(node_ids))
        edges = [dict(r) for r in c.fetchall()]

    conn.close()
    return jsonify({'nodes': nodes, 'edges': edges})


@app.route('/api/concepts')
def api_concepts():
    conn = get_db()
    c = conn.cursor()

    sort = request.args.get('sort', 'mention_count')
    category = request.args.get('category')
    limit = request.args.get('limit', 100, type=int)

    where = []
    params = []
    if category:
        where.append('category = ?')
        params.append(category)

    where_clause = 'WHERE ' + ' AND '.join(where) if where else ''
    order = 'mention_count DESC' if sort == 'mention_count' else 'name ASC'

    c.execute(f'''SELECT id, name, name_zh, category, mention_count, first_seen_year
                  FROM concepts {where_clause}
                  ORDER BY {order} LIMIT ?''', params + [limit])
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(results)


@app.route('/api/concept/<int:concept_id>')
def api_concept_detail(concept_id):
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT * FROM concepts WHERE id = ?', (concept_id,))
    concept = c.fetchone()
    if not concept:
        conn.close()
        return jsonify({'error': 'not found'}), 404

    result = dict(concept)

    # Sources
    c.execute('''SELECT cs.source_type, cs.source_id, cs.relevance, cs.context,
                        CASE WHEN cs.source_type = 'article' THEN a.title
                             WHEN cs.source_type = 'book' THEN b.title END as title,
                        CASE WHEN cs.source_type = 'article' THEN a.author
                             WHEN cs.source_type = 'book' THEN b.author END as author
                 FROM concept_sources cs
                 LEFT JOIN articles a ON cs.source_type = 'article' AND cs.source_id = a.id
                 LEFT JOIN books b ON cs.source_type = 'book' AND cs.source_id = b.id
                 WHERE cs.concept_id = ?
                 ORDER BY cs.relevance DESC''', (concept_id,))
    result['sources'] = [dict(r) for r in c.fetchall()]

    # Related concepts
    c.execute('''SELECT c2.id, c2.name, c2.name_zh, c2.mention_count, cr.relation, cr.strength
                 FROM concept_relations cr
                 JOIN concepts c2 ON (cr.concept_b = c2.id AND cr.concept_a = ?)
                                  OR (cr.concept_a = c2.id AND cr.concept_b = ?)
                 ORDER BY cr.strength DESC''', (concept_id, concept_id))
    result['related'] = [dict(r) for r in c.fetchall()]

    conn.close()
    return jsonify(result)


@app.route('/api/concept-map')
def api_concept_map():
    """Return topic -> concept aggregation for sidebar bubble chart."""
    conn = get_db()
    c = conn.cursor()

    # Get topics with their article/book counts
    topic_data = {}

    for row in c.execute('SELECT topics FROM articles WHERE topics IS NOT NULL'):
        try:
            for t in json.loads(row['topics']):
                if t not in topic_data:
                    topic_data[t] = {'count': 0, 'concepts': {}}
                topic_data[t]['count'] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    for row in c.execute('SELECT topics FROM books WHERE topics IS NOT NULL'):
        try:
            for t in json.loads(row['topics']):
                if t not in topic_data:
                    topic_data[t] = {'count': 0, 'concepts': {}}
                topic_data[t]['count'] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    # Map concepts to topics via their sources
    c.execute('''
        SELECT c.id, c.name, c.name_zh, c.mention_count,
               cs.source_type, cs.source_id
        FROM concepts c
        JOIN concept_sources cs ON c.id = cs.concept_id
        WHERE c.mention_count >= 2
    ''')
    for row in c.fetchall():
        if row['source_type'] == 'article':
            src = conn.execute('SELECT topics FROM articles WHERE id = ?', (row['source_id'],)).fetchone()
        else:
            src = conn.execute('SELECT topics FROM books WHERE id = ?', (row['source_id'],)).fetchone()
        if src and src['topics']:
            try:
                for t in json.loads(src['topics']):
                    if t in topic_data:
                        cname = row['name']
                        if cname not in topic_data[t]['concepts']:
                            topic_data[t]['concepts'][cname] = {
                                'id': row['id'], 'name': row['name'],
                                'name_zh': row['name_zh'],
                                'mention_count': row['mention_count']
                            }
            except (json.JSONDecodeError, TypeError):
                pass

    # Format result
    result = []
    for topic, data in sorted(topic_data.items(), key=lambda x: -x[1]['count']):
        result.append({
            'topic': topic,
            'count': data['count'],
            'concepts': sorted(data['concepts'].values(), key=lambda x: -x['mention_count'])[:10]
        })

    conn.close()
    return jsonify(result)


# ─── Notes API ────────────────────────────────────────────────────

@app.route('/api/notes', methods=['GET'])
def api_notes_get():
    conn = get_db()
    c = conn.cursor()

    article_id = request.args.get('article_id')
    book_id = request.args.get('book_id')
    chapter_id = request.args.get('chapter_id')

    if article_id:
        c.execute('SELECT * FROM notes WHERE article_id = ? ORDER BY created_at DESC', (article_id,))
    elif book_id:
        c.execute('SELECT * FROM notes WHERE book_id = ? ORDER BY created_at DESC', (book_id,))
    elif chapter_id:
        c.execute('SELECT * FROM notes WHERE chapter_id = ? ORDER BY created_at DESC', (chapter_id,))
    else:
        c.execute('SELECT * FROM notes ORDER BY created_at DESC LIMIT 100')

    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return jsonify(results)

@app.route('/api/notes', methods=['POST'])
def api_notes_post():
    data = request.get_json()
    content = data.get('content', '').strip()
    if not content:
        return jsonify({'error': 'No content'}), 400

    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO notes (content, article_id, book_id, chapter_id, highlight_text, tags)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (content, data.get('article_id'), data.get('book_id'),
               data.get('chapter_id'), data.get('highlight_text'), data.get('tags')))
    conn.commit()
    note_id = c.lastrowid
    conn.close()
    return jsonify({'id': note_id, 'success': True})

# ─── Reading Progress API ─────────────────────────────────────────

@app.route('/api/reading-progress', methods=['GET'])
def api_reading_progress_get():
    conn = get_db()
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS reading_progress (
            id INTEGER PRIMARY KEY, book_id INTEGER UNIQUE,
            last_chapter INTEGER, read_chapters TEXT, updated_at TEXT
        )''')
        conn.commit()
    except Exception:
        pass
    book_id = request.args.get('book_id')
    if book_id:
        row = conn.execute('SELECT * FROM reading_progress WHERE book_id = ?', (book_id,)).fetchone()
        if row:
            return jsonify(dict(row))
        return jsonify({})
    rows = conn.execute('SELECT * FROM reading_progress').fetchall()
    return jsonify([dict(r) for r in rows])

@app.route('/api/reading-progress', methods=['POST'])
def api_reading_progress_post():
    data = request.get_json()
    conn = get_db()
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS reading_progress (
            id INTEGER PRIMARY KEY, book_id INTEGER UNIQUE,
            last_chapter INTEGER, read_chapters TEXT, updated_at TEXT
        )''')
    except Exception:
        pass
    conn.execute('''INSERT OR REPLACE INTO reading_progress (book_id, last_chapter, read_chapters, updated_at)
                    VALUES (?, ?, ?, datetime('now'))''',
                 (data['book_id'], data['last_chapter'], json.dumps(data.get('read_chapters', []))))
    conn.commit()
    return jsonify({'success': True})

# ─── Export API ───────────────────────────────────────────────────

@app.route('/api/export/notes')
def api_export_notes():
    conn = get_db()
    notes = conn.execute('''SELECT n.*, a.title as article_title, b.title as book_title, ch.title as chapter_title
                           FROM notes n
                           LEFT JOIN articles a ON n.article_id = a.id
                           LEFT JOIN books b ON n.book_id = b.id
                           LEFT JOIN book_chapters ch ON n.chapter_id = ch.id
                           ORDER BY n.created_at DESC''').fetchall()
    lines = ['# Research Notes\n']
    for n in notes:
        source = n['article_title'] or n['book_title'] or 'General'
        if n['chapter_title']:
            source += f" / {n['chapter_title']}"
        lines.append(f"## {source}")
        lines.append(f"*{n['created_at']}*\n")
        if n['highlight_text']:
            lines.append(f"> {n['highlight_text']}\n")
        lines.append(n['content'] + '\n')
        if n['tags']:
            lines.append(f"Tags: {n['tags']}\n")
        lines.append('---\n')
    from flask import Response
    return Response('\n'.join(lines), mimetype='text/markdown',
                    headers={'Content-Disposition': 'attachment; filename=research_notes.md'})

@app.route('/api/export/article/<int:article_id>')
def api_export_article(article_id):
    conn = get_db()
    a = conn.execute('SELECT * FROM articles WHERE id = ?', (article_id,)).fetchone()
    if not a:
        return jsonify({'error': 'not found'}), 404
    lines = [f"# {a['title']}\n"]
    if a['author']:
        lines.append(f"**Author:** {a['author']}")
    if a['date']:
        lines.append(f"**Date:** {a['date']}")
    if a['source']:
        lines.append(f"**Source:** {a['source']}")
    lines.append('')
    if a['abstract']:
        lines.append(f"## Abstract\n{a['abstract']}\n")
    if a['content']:
        lines.append(f"## Content\n{a['content']}")
    from flask import Response
    safe_title = (a['title'] or 'article')[:50].replace('/', '-').replace(' ', '_')
    return Response('\n'.join(lines), mimetype='text/markdown',
                    headers={'Content-Disposition': f'attachment; filename={safe_title}.md'})

@app.route('/api/export/qa-history')
def api_export_qa_history():
    conn = get_db()
    rows = conn.execute('SELECT question, answer_html, created_at FROM qa_history ORDER BY id DESC LIMIT 100').fetchall()
    lines = ['# Q&A History\n']
    for r in rows:
        lines.append(f"## Q: {r['question']}")
        lines.append(f"*{r['created_at']}*\n")
        # Strip HTML tags for markdown
        import re
        answer_text = re.sub(r'<[^>]+>', '', r['answer_html'] or '')
        lines.append(answer_text + '\n---\n')
    from flask import Response
    return Response('\n'.join(lines), mimetype='text/markdown',
                    headers={'Content-Disposition': 'attachment; filename=qa_history.md'})

# ─── Contradiction Detection API ──────────────────────────────────

@app.route('/api/contradictions')
def api_contradictions():
    """Find potentially contradicting arguments in the corpus."""
    conn = get_db()
    topic = request.args.get('topic', '')
    limit = int(request.args.get('limit', '20'))

    # Get arguments, optionally filtered by topic
    if topic:
        args_rows = conn.execute(
            "SELECT id, claim, evidence, counterargument, topic, source_type, source_id FROM arguments WHERE topic LIKE ? LIMIT 200",
            (f'%{topic}%',)
        ).fetchall()
    else:
        args_rows = conn.execute(
            "SELECT id, claim, evidence, counterargument, topic, source_type, source_id FROM arguments WHERE counterargument IS NOT NULL AND counterargument != '' LIMIT 200"
        ).fetchall()

    # Group by topic, find claims with counterarguments
    contradictions = []
    for row in args_rows:
        if row['counterargument'] and len(row['counterargument']) > 20:
            # Look for other arguments that align with the counterargument
            source_title = ''
            if row['source_type'] == 'article':
                src = conn.execute('SELECT title, author FROM articles WHERE id = ?', (row['source_id'],)).fetchone()
                if src:
                    source_title = f"{src['title'][:60]} by {src['author'] or 'unknown'}"
            contradictions.append({
                'claim': row['claim'],
                'counterargument': row['counterargument'],
                'topic': row['topic'],
                'source': source_title,
                'argument_id': row['id']
            })

    # Sort by topic for grouping
    contradictions.sort(key=lambda x: x['topic'])
    return jsonify(contradictions[:limit])

# ─── Research Dashboard API ───────────────────────────────────────

@app.route('/api/dashboard')
def api_dashboard():
    conn = get_db()
    c = conn.cursor()

    # Coverage by category
    categories = c.execute(
        "SELECT category, count(*) as n, avg(importance) as avg_imp FROM articles WHERE category IS NOT NULL GROUP BY category ORDER BY n DESC"
    ).fetchall()

    # Reading progress summary
    progress = []
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS reading_progress (
            id INTEGER PRIMARY KEY, book_id INTEGER UNIQUE,
            last_chapter INTEGER, read_chapters TEXT, updated_at TEXT
        )''')
        rows = c.execute('''SELECT rp.book_id, rp.read_chapters, b.title,
                            (SELECT count(*) FROM book_chapters WHERE book_id = rp.book_id) as total_chapters
                           FROM reading_progress rp JOIN books b ON rp.book_id = b.id''').fetchall()
        for r in rows:
            read_ch = json.loads(r['read_chapters'] or '[]')
            progress.append({
                'book': r['title'][:40],
                'read': len(read_ch),
                'total': r['total_chapters'],
                'pct': round(len(read_ch) / r['total_chapters'] * 100) if r['total_chapters'] else 0
            })
    except Exception:
        pass

    # Knowledge density: concepts per category
    density = c.execute('''
        SELECT a.category, count(DISTINCT cs.concept_id) as concept_count
        FROM concept_sources cs
        JOIN articles a ON cs.source_type = 'article' AND cs.source_id = a.id
        WHERE a.category IS NOT NULL
        GROUP BY a.category ORDER BY concept_count DESC
    ''').fetchall()

    # Arguments per topic
    arg_topics = c.execute(
        "SELECT topic, count(*) as n FROM arguments GROUP BY topic ORDER BY n DESC LIMIT 15"
    ).fetchall()

    # QA activity
    qa_count = c.execute('SELECT count(*) FROM qa_history').fetchone()[0]

    # Notes count
    notes_count = c.execute('SELECT count(*) FROM notes').fetchone()[0]

    return jsonify({
        'categories': [{'name': r['category'], 'count': r['n'], 'avg_importance': round(r['avg_imp'] or 0, 1)} for r in categories],
        'reading_progress': progress,
        'knowledge_density': [{'category': r['category'], 'concepts': r['concept_count']} for r in density],
        'argument_topics': [{'topic': r['topic'], 'count': r['n']} for r in arg_topics],
        'qa_count': qa_count,
        'notes_count': notes_count,
    })

# ─── Stats ────────────────────────────────────────────────────────

@app.route('/api/stats')
def api_stats():
    conn = get_db()
    c = conn.cursor()

    c.execute('SELECT count(*) FROM articles')
    total = c.fetchone()[0]
    c.execute('SELECT count(*) FROM articles WHERE content IS NOT NULL')
    with_content = c.fetchone()[0]
    c.execute('SELECT count(*) FROM articles WHERE title_zh IS NOT NULL')
    translated_titles = c.fetchone()[0]
    c.execute('SELECT count(*) FROM articles WHERE content_zh IS NOT NULL')
    translated_full = c.fetchone()[0]

    # Book stats
    books = 0
    book_chapters = 0
    try:
        c.execute('SELECT count(*) FROM books')
        books = c.fetchone()[0]
        c.execute('SELECT count(*) FROM book_chapters')
        book_chapters = c.fetchone()[0]
    except Exception:
        pass

    c.execute('SELECT source, count(*) as cnt FROM articles GROUP BY source ORDER BY cnt DESC')
    sources = [{'name': r['source'], 'count': r['cnt']} for r in c.fetchall()]

    c.execute('SELECT topics FROM articles WHERE topics IS NOT NULL')
    topic_counts = {}
    for r in c.fetchall():
        try:
            for t in json.loads(r['topics']):
                topic_counts[t] = topic_counts.get(t, 0) + 1
        except (json.JSONDecodeError, TypeError):
            pass
    topics = [{'name': t, 'count': cnt} for t, cnt in sorted(topic_counts.items(), key=lambda x: -x[1])]

    c.execute('SELECT level, count(*) as cnt FROM articles WHERE level IS NOT NULL GROUP BY level')
    levels = {r['level']: r['cnt'] for r in c.fetchall()}

    conn.close()
    return jsonify({
        'total': total, 'with_content': with_content,
        'translated_titles': translated_titles, 'translated_full': translated_full,
        'books': books, 'book_chapters': book_chapters,
        'sources': sources, 'topics': topics, 'levels': levels
    })

# ── Learning Plan ──────────────────────────────────────────────

LEARNING_PLAN = [
    {
        'month': 1, 'title': 'Writing Precision', 'title_zh': '写作精度',
        'theme': 'Learn to write with surgical precision',
        'weeks': [
            {'week': 1, 'title': 'Elements of Style', 'book_id': 23,
             'book_title': 'The Elements of Style (Strunk & White)',
             'tasks': [
                 'Read chapters 1-5, highlight every rule',
                 'Rewrite 3 paragraphs from your own writing using the rules',
                 'Use Ask AI: "According to Strunk & White, how can I improve this paragraph?"',
             ],
             'searches': ['omit needless words', 'active voice clarity', 'parallel construction']},
            {'week': 2, 'title': 'Style: Clarity and Grace', 'book_id': 22,
             'book_title': 'Style: Lessons in Clarity and Grace (Williams)',
             'tasks': [
                 'Read Williams on diagnosis (subject-verb-object pattern)',
                 'Compare Williams vs Strunk: Ask AI "How do Williams and Strunk differ on active voice?"',
                 'Rewrite 5 sentences using the subject-verb diagnosis method',
             ],
             'searches': ['subject verb diagnosis clarity', 'cohesion coherence writing', 'nominalizations']},
            {'week': 3, 'title': 'Economist Practice', 'book_id': None,
             'book_title': 'The Economist (daily reading)',
             'tasks': [
                 'Read 1 Economist Leaders article daily',
                 'Identify the thesis sentence and argument skeleton in each article',
                 'Write a 100-word summary of each article',
             ],
             'searches': ['concise writing journalistic style', 'argument structure editorial']},
            {'week': 4, 'title': 'Synthesis & Review', 'book_id': None,
             'book_title': 'Review & integrate',
             'tasks': [
                 'Write a 500-word essay applying all writing principles learned',
                 'Self-review using Strunk & Williams checklists',
                 'Record 3 most impactful writing rules in your notes',
             ],
             'searches': ['writing style self-editing checklist']},
        ]
    },
    {
        'month': 2, 'title': 'Argument Analysis', 'title_zh': '论证拆解',
        'theme': 'Master the structure of arguments',
        'weeks': [
            {'week': 1, 'title': 'Rulebook for Arguments', 'book_id': 21,
             'book_title': 'A Rulebook for Arguments (Weston)',
             'tasks': [
                 'Read all chapters, take notes on argument patterns',
                 'Use corpus arguments search to find real examples of each pattern',
                 'Identify 5 common fallacies in the corpus arguments',
             ],
             'searches': ['argument fallacy', 'deductive reasoning premises', 'inductive argument evidence']},
            {'week': 2, 'title': 'Euthyphro (Plato)', 'book_id': None,
             'book_title': 'Euthyphro (Plato) — not yet in corpus',
             'tasks': [
                 'Read the full dialogue (short, ~30 pages)',
                 'Map the argument structure: what is Socrates trying to define?',
                 'Search corpus for "Euthyphro dilemma" in related articles',
             ],
             'searches': ['Euthyphro dilemma definition piety', 'Socratic method definition']},
            {'week': 3, 'title': 'Meno (Plato)', 'book_id': None,
             'book_title': 'Meno (Plato) — not yet in corpus',
             'tasks': [
                 'Read the full dialogue (~30 pages)',
                 'Analyze the "Meno paradox" of learning',
                 'Search corpus for articles discussing Meno and knowledge',
             ],
             'searches': ['Meno paradox learning knowledge', 'recollection theory Plato']},
            {'week': 4, 'title': 'Thinking, Fast and Slow', 'book_id': 16,
             'book_title': 'Thinking, Fast and Slow (Kahneman)',
             'tasks': [
                 'Read Part 1 on System 1 vs System 2',
                 'Search corpus for cognitive bias arguments',
                 'Write analysis: how do cognitive biases affect AI alignment arguments?',
             ],
             'searches': ['cognitive bias anchoring', 'System 1 System 2 heuristic', 'Kahneman prospect theory']},
        ]
    },
    {
        'month': 3, 'title': 'Structured Thinking', 'title_zh': '结构化思维',
        'theme': 'Build frameworks for clear reasoning',
        'weeks': [
            {'week': 1, 'title': 'Pyramid Principle', 'book_id': 25,
             'book_title': 'The Pyramid Principle (Minto)',
             'tasks': [
                 'Read first 3 chapters on MECE and pyramid structure',
                 'Restructure one of your previous essays using pyramid structure',
                 'Practice: classify 10 concepts from the Knowledge Graph into MECE categories',
             ],
             'searches': ['MECE mutually exclusive collectively exhaustive', 'pyramid principle structure']},
            {'week': 2, 'title': 'MECE Practice', 'book_id': 25,
             'book_title': 'The Pyramid Principle (continued)',
             'tasks': [
                 'Use Knowledge Graph to check your MECE classifications',
                 'Write a structured brief on "Problems of AI consciousness" using pyramid structure',
                 'Review the Research Dashboard category distribution as a MECE example',
             ],
             'searches': ['classification taxonomy AI problems', 'structured analysis framework']},
            {'week': 3, 'title': 'Prompt Engineering Basics', 'book_id': None,
             'book_title': 'Prompt practice with Ask AI',
             'tasks': [
                 'Write 5 different prompts for the same question, compare results',
                 'Test structured vs unstructured prompts in Ask AI',
                 'Document which prompt patterns get better RAG results',
             ],
             'searches': ['prompt engineering structured output', 'chain of thought reasoning']},
            {'week': 4, 'title': 'Integration Week', 'book_id': None,
             'book_title': 'Review & synthesize',
             'tasks': [
                 'Rewrite a complex prompt using pyramid principle structure',
                 'Test the improved prompt in Ask AI and compare with original',
                 'Write a 300-word reflection on structured thinking lessons learned',
             ],
             'searches': ['structured thinking meta-cognition', 'writing framework analysis']},
        ]
    },
    {
        'month': 4, 'title': 'Philosophy Reading', 'title_zh': '哲学阅读',
        'theme': 'Deep engagement with primary philosophical texts',
        'weeks': [
            {'week': 1, 'title': 'Meditations (Descartes)', 'book_id': 19,
             'book_title': 'Meditations on First Philosophy (Descartes)',
             'tasks': [
                 'Read Meditations 1-3',
                 'Map the doubt method: what does Descartes doubt and why?',
                 'Ask AI: "How does Descartes\' doubt method relate to AI uncertainty?"',
             ],
             'searches': ['Descartes methodological doubt cogito', 'skepticism certainty knowledge', 'Cartesian dualism AI']},
            {'week': 2, 'title': 'Nicomachean Ethics I', 'book_id': 18,
             'book_title': 'Nicomachean Ethics (Aristotle)',
             'tasks': [
                 'Read Books 1-3 on eudaimonia and virtue',
                 'Search corpus for phronesis discussions',
                 'Write: Can AI have practical wisdom (phronesis)?',
             ],
             'searches': ['phronesis practical wisdom', 'eudaimonia virtue ethics', 'Aristotle AI judgment']},
            {'week': 3, 'title': 'Nicomachean Ethics II', 'book_id': 18,
             'book_title': 'Nicomachean Ethics (continued)',
             'tasks': [
                 'Read Books 6 and 10 on intellectual virtues',
                 'Compare Aristotelian and utilitarian approaches in corpus debates',
                 'Ask AI: "What are the strongest arguments for AI having virtues?"',
             ],
             'searches': ['intellectual virtue contemplation', 'virtue ethics vs consequentialism AI']},
            {'week': 4, 'title': 'Philosophical Investigations', 'book_id': 17,
             'book_title': 'Philosophical Investigations (Wittgenstein)',
             'tasks': [
                 'Read sections 1-100 on language games and family resemblance',
                 'Search corpus for Wittgenstein + LLM discussions',
                 'Write: How does the rule-following paradox apply to language models?',
             ],
             'searches': ['Wittgenstein language games', 'rule following paradox LLM', 'private language argument AI']},
        ]
    },
    {
        'month': 5, 'title': 'Prompt & Skill Engineering', 'title_zh': 'Prompt与技能工程',
        'theme': 'Apply everything to AI interaction design',
        'weeks': [
            {'week': 1, 'title': 'Advanced Prompting', 'book_id': None,
             'book_title': 'Prompt engineering practice',
             'tasks': [
                 'Design 3 complex prompts combining writing + argument + structure principles',
                 'Test each prompt in Ask AI, evaluate result quality',
                 'Iterate and document your prompt design principles',
             ],
             'searches': ['prompt design principles structured', 'RAG query optimization']},
            {'week': 2, 'title': 'Skill Design', 'book_id': None,
             'book_title': 'Claude Code skill authoring',
             'tasks': [
                 'Study the existing research-query skill as a template',
                 'Design a new skill for philosophical argument analysis',
                 'Test the skill with real corpus queries',
             ],
             'searches': ['skill design template structured', 'argument analysis automated']},
            {'week': 3, 'title': 'System Integration', 'book_id': None,
             'book_title': 'Cross-system practice',
             'tasks': [
                 'Create a multi-step research workflow combining search + arguments + concepts',
                 'Write a comprehensive analysis using all system features',
                 'Document the optimal research workflow',
             ],
             'searches': ['research workflow multi-source', 'comprehensive analysis method']},
            {'week': 4, 'title': 'Portfolio Review', 'book_id': None,
             'book_title': 'Review all written work',
             'tasks': [
                 'Review QA History for your best prompts and answers',
                 'Compile your best analyses into a portfolio document',
                 'Identify areas for improvement in month 6',
             ],
             'searches': []},
        ]
    },
    {
        'month': 6, 'title': 'Capstone Project', 'title_zh': '毕业项目',
        'theme': 'Produce a substantial piece of original analysis',
        'weeks': [
            {'week': 1, 'title': 'Topic Selection', 'book_id': None,
             'book_title': 'Choose capstone topic',
             'tasks': [
                 'Review all notes and QA history for recurring interests',
                 'Select a topic at the intersection of philosophy + AI',
                 'Create an outline using pyramid principle structure',
             ],
             'searches': ['philosophy AI intersection consciousness', 'original analysis framework']},
            {'week': 2, 'title': 'Research & Draft', 'book_id': None,
             'book_title': 'Deep corpus research',
             'tasks': [
                 'Conduct comprehensive corpus search on your topic',
                 'Write a 2000-word first draft',
                 'Use arguments search to find supporting and opposing views',
             ],
             'searches': []},
            {'week': 3, 'title': 'Revision', 'book_id': None,
             'book_title': 'Apply all writing principles',
             'tasks': [
                 'Revise using Strunk & White and Williams principles',
                 'Check argument structure using Weston framework',
                 'Verify MECE structure using Minto framework',
             ],
             'searches': []},
            {'week': 4, 'title': 'Final Polish', 'book_id': None,
             'book_title': 'Final submission',
             'tasks': [
                 'Final editing pass for clarity and concision',
                 'Add proper citations from corpus sources',
                 'Write a 200-word abstract',
                 'Celebrate completing the 6-month plan!',
             ],
             'searches': []},
        ]
    },
]

@app.route('/api/plan')
def api_plan():
    conn = get_db()
    # Fetch progress
    rows = conn.execute('SELECT month, week, task_idx, done FROM plan_progress').fetchall()
    progress = {}
    for r in rows:
        progress[f"{r['month']}-{r['week']}-{r['task_idx']}"] = r['done']
    # Add book info from DB
    plan_out = []
    for m in LEARNING_PLAN:
        month_data = {**m, 'weeks': []}
        for w in m['weeks']:
            week_data = {**w, 'book_in_corpus': False}
            if w['book_id']:
                row = conn.execute('SELECT id, title, title_zh, author FROM books WHERE id = ?', (w['book_id'],)).fetchone()
                if row:
                    week_data['book_in_corpus'] = True
                    week_data['book_db_title'] = row['title']
            # Add progress
            task_progress = []
            for i in range(len(w['tasks'])):
                key = f"{m['month']}-{w['week']}-{i}"
                task_progress.append(progress.get(key, 0))
            week_data['progress'] = task_progress
            month_data['weeks'].append(week_data)
        plan_out.append(month_data)
    conn.close()
    return jsonify(plan_out)

@app.route('/api/plan/toggle', methods=['POST'])
def api_plan_toggle():
    data = request.json
    month, week, task_idx = data['month'], data['week'], data['task_idx']
    conn = get_db()
    row = conn.execute('SELECT done FROM plan_progress WHERE month=? AND week=? AND task_idx=?',
                       (month, week, task_idx)).fetchone()
    new_val = 0 if (row and row['done']) else 1
    conn.execute('''INSERT OR REPLACE INTO plan_progress (month, week, task_idx, done, updated_at)
                    VALUES (?, ?, ?, ?, datetime('now'))''', (month, week, task_idx, new_val))
    conn.commit()
    conn.close()
    return jsonify({'done': new_val})


if __name__ == '__main__':
    print('Starting server at http://localhost:8765')
    app.run(host='0.0.0.0', port=8765, debug=False)
