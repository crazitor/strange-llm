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

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Try to load ChromaDB at startup
chroma_articles = None
chroma_books = None
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
except Exception as e:
    print(f'ChromaDB not available: {e}')

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
</style>
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
  loadArticles({sort: 'importance', limit: 100});
}

function renderSidebar(data) {
  // Mode tabs
  let html = '<div class="mode-tabs">';
  html += `<div class="mode-tab ${browseMode==='articles'?'active':''}" onclick="switchMode('articles')">Articles</div>`;
  html += `<div class="mode-tab ${browseMode==='books'?'active':''}" onclick="switchMode('books')">Books</div>`;
  html += `<div class="mode-tab" onclick="showMyNotes()" style="background:var(--tag-bg)">Notes</div>`;
  html += '</div>';

  if (browseMode === 'books') {
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
      html += `<div class="filter-item" onclick="toggleFilter('topic','${t.name}')">${zh} #${t.name} <span class="count">${t.count}</span></div>`;
    });
  }
  document.getElementById('sidebar').innerHTML = html;
}

async function switchMode(mode) {
  browseMode = mode;
  currentFilters = {};
  const resp = await fetch('/api/filters');
  const data = await resp.json();
  renderSidebar(data);
  if (mode === 'books') {
    loadBooks({});
  } else {
    loadArticles({sort: 'importance', limit: 100});
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
    loadArticles({...currentFilters, sort: 'importance', limit: 100});
  }
}

async function loadArticles(params) {
  const qs = new URLSearchParams(params).toString();
  const resp = await fetch('/api/articles?' + qs);
  allArticles = await resp.json();
  renderList(allArticles);
}

async function loadBooks(params) {
  const qs = new URLSearchParams(params).toString();
  const resp = await fetch('/api/books?' + qs);
  const books = await resp.json();
  renderBookList(books);
}

function renderBookList(books) {
  if (!books.length) {
    document.getElementById('listPanel').innerHTML = '<div class="empty-state">No books</div>';
    return;
  }
  let html = `<div class="list-header"><span>${books.length} books</span></div>`;
  books.forEach(b => {
    const cat = categoryZh[b.category] || b.category || '';
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
        ${b.linked_title ? '<span style="color:var(--orange)">has ' + (b.language==='en'?'ZH':'EN') + ' version</span>' : ''}
      </div>
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
  let html = `<div class="list-header"><span>${articles.length} articles</span></div>`;
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
  document.getElementById('listPanel').innerHTML = html;
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

  html += `<div class="info-box"><strong>Chapters:</strong> ${bookChapters.length} &nbsp; <strong>Click a chapter on the left to read</strong></div>`;

  html += renderNotesSection('book', b.id);

  document.getElementById('readingPanel').innerHTML = html;
  document.getElementById('readingPanel').scrollTop = 0;
  loadNotes('book', b.id);
}

async function loadChapter(idx, el) {
  if (idx < 0 || idx >= bookChapters.length) return;
  currentChapterIdx = idx;
  const ch = bookChapters[idx];

  document.querySelectorAll('.chapter-item').forEach(e => e.classList.remove('selected'));
  if (el) el.classList.add('selected');

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

  // Notes
  html += renderNotesSection('chapter', ch.id);

  document.getElementById('readingPanel').innerHTML = html;
  document.getElementById('readingPanel').scrollTop = 0;
  loadNotes('chapter', ch.id);
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

  html += '<div id="askResult"></div>';
  html += '</div>';

  document.getElementById('readingPanel').innerHTML = html;
}

async function doAsk(question) {
  if (!question || !question.trim()) return;
  const resultDiv = document.getElementById('askResult') || document.getElementById('readingPanel');

  if (!askMode) {
    askMode = true;
    document.getElementById('btnAskMode').classList.add('active');
    showAskPanel();
    document.getElementById('askInput').value = question;
  }

  const askResult = document.getElementById('askResult');
  askResult.innerHTML = '<div class="ask-loading">Searching and thinking...</div>';

  try {
    const resp = await fetch('/api/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question: question.trim()})
    });
    const data = await resp.json();

    let html = '<div class="ask-answer">';
    html += `<div class="content" style="margin-bottom:16px">${data.answer_html || escHtml(data.answer || 'No answer')}</div>`;

    if (data.sources && data.sources.length) {
      html += '<h3 style="color:var(--accent);margin-bottom:8px">Sources</h3>';
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

  document.getElementById('listPanel').innerHTML = '';
  document.getElementById('readingPanel').innerHTML = html;
}

function escHtml(s) {
  if (!s) return '';
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
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

    limit = int(request.args.get('limit', 100))
    where_clause = 'WHERE ' + ' AND '.join(where) if where else ''
    sort = request.args.get('sort', 'importance')
    order = 'importance DESC NULLS LAST' if sort == 'importance' else 'date DESC'

    c.execute(f'''SELECT id, title, title_zh, author, date, source, importance, topics, level,
                         abstract as snippet
                  FROM articles {where_clause}
                  ORDER BY {order} LIMIT ?''', params + [limit])

    results = []
    for r in c.fetchall():
        results.append({
            'id': r['id'], 'title': r['title'], 'title_zh': r['title_zh'],
            'author': r['author'], 'date': r['date'], 'source': r['source'],
            'importance': r['importance'], 'topics': r['topics'], 'level': r['level'],
            'snippet': (r['snippet'] or '')[:200]
        })

    conn.close()
    return jsonify(results)

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
                r['snippet'] = (r['snippet'] or '')[:200]
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
    # Convert markdown to HTML
    if result.get('content'):
        try:
            result['content_html'] = markdown.markdown(
                result['content'][:100000],
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
                result['content_zh'][:100000],
                extensions=['fenced_code', 'tables', 'toc']
            )
        except Exception:
            result['content_zh_html'] = f'<pre>{result["content_zh"][:50000]}</pre>'
        del result['content_zh']
    else:
        result['content_zh_html'] = None

    # Similar articles
    result['similar'] = []
    if chroma_articles:
        try:
            similar = chroma_articles.query(
                query_texts=[result['title'] + ' ' + (result.get('abstract') or '')[:200]],
                n_results=6
            )
            for sid, meta in zip(similar['ids'][0], similar['metadatas'][0]):
                try:
                    aid = int(sid.replace('a_', ''))
                except ValueError:
                    aid = int(sid)
                if aid != article_id:
                    result['similar'].append({
                        'id': aid,
                        'title': meta.get('title', ''),
                        'source': meta.get('source', '')
                    })
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
                         lb.title as linked_title
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

    sources = []
    context_parts = []

    # Search articles via ChromaDB
    if chroma_articles:
        try:
            results = chroma_articles.query(query_texts=[question], n_results=5)
            conn = get_db()
            c = conn.cursor()
            for sid, meta, doc in zip(results['ids'][0], results['metadatas'][0], results['documents'][0]):
                try:
                    aid = int(sid.replace('a_', ''))
                except ValueError:
                    aid = int(sid)
                c.execute('SELECT abstract, content FROM articles WHERE id = ?', (aid,))
                row = c.fetchone()
                snippet = ''
                if row:
                    snippet = (row['content'] or row['abstract'] or '')[:1500]
                sources.append({
                    'type': 'article', 'id': aid,
                    'title': meta.get('title', ''),
                    'author': meta.get('author', ''),
                    'snippet': snippet[:200]
                })
                context_parts.append(f"[Article: {meta.get('title','')} by {meta.get('author','')}]\n{snippet}")
            conn.close()
        except Exception:
            pass

    # Search books via ChromaDB
    if chroma_books:
        try:
            results = chroma_books.query(query_texts=[question], n_results=5)
            conn = get_db()
            c = conn.cursor()
            for sid, meta, doc in zip(results['ids'][0], results['metadatas'][0], results['documents'][0]):
                chunk_id = int(sid.replace('bc_', ''))
                c.execute('SELECT content FROM book_chunks WHERE id = ?', (chunk_id,))
                row = c.fetchone()
                snippet = (row['content'] if row else doc)[:1500]
                sources.append({
                    'type': 'book_chunk',
                    'book_id': meta.get('book_id'),
                    'title': meta.get('book_title', ''),
                    'chapter': meta.get('chapter_title', ''),
                    'author': meta.get('author', ''),
                    'snippet': snippet[:200]
                })
                context_parts.append(
                    f"[Book: {meta.get('book_title','')} - Ch: {meta.get('chapter_title','')} by {meta.get('author','')}]\n{snippet}")
            conn.close()
        except Exception:
            pass

    if not context_parts:
        return jsonify({'answer': 'No relevant sources found.', 'sources': []})

    context = '\n\n---\n\n'.join(context_parts)
    prompt = f"""Based on the following sources, answer the question. Cite sources using [Author, Title] format.
Answer in the same language as the question. Be thorough but concise.

Sources:
{context}

Question: {question}"""

    try:
        r = deepseek_client.chat.completions.create(
            model='deepseek-chat',
            max_tokens=2000,
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = r.choices[0].message.content.strip()
        answer_html = markdown.markdown(answer, extensions=['fenced_code', 'tables'])
        return jsonify({'answer': answer, 'answer_html': answer_html, 'sources': sources})
    except Exception as e:
        return jsonify({'answer': f'Error: {str(e)}', 'sources': sources})

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

if __name__ == '__main__':
    print('Starting server at http://localhost:8765')
    app.run(host='0.0.0.0', port=8765, debug=False)
