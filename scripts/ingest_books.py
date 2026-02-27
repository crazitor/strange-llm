#!/usr/bin/env python3
"""Parse PDF books, extract chapters, chunk text, and ingest into corpus.db."""

import os
import re
import sys
import json
import sqlite3
import fitz  # pymupdf

RESEARCH_DIR = os.path.join(os.path.dirname(__file__), '..', 'research')
DB_PATH = os.path.join(RESEARCH_DIR, 'corpus.db')
PDF_DIR = os.path.join(os.path.dirname(__file__), '..', 'pdf')

CHUNK_SIZE = 600      # target tokens per chunk (approx chars * 0.75)
CHUNK_CHARS = 2400    # ~600 tokens
CHUNK_OVERLAP = 200   # overlap in chars

# ─── Book metadata mapping ───────────────────────────────────────────
BOOKS = [
    # EN books
    {
        "filename": "Douglas R. Hofstadter - Gödel, Escher, Bach_ An Eternal Golden Braid (1979, Basic Books) - libgen.li.pdf",
        "title": "Gödel, Escher, Bach: An Eternal Golden Braid",
        "title_zh": "哥德尔、艾舍尔、巴赫：集异璧之大成",
        "author": "Douglas Hofstadter",
        "year": "1979",
        "language": "en",
        "category": "philosophy",
        "topics": ["consciousness", "self-reference", "computation", "philosophy-of-mind"],
        "importance": 10.0,
    },
    {
        "filename": "哥德尔、艾舍尔、巴赫  集异璧之大成_10977169.pdf",
        "title": "哥德尔、艾舍尔、巴赫：集异璧之大成",
        "title_zh": "哥德尔、艾舍尔、巴赫：集异璧之大成",
        "author": "Douglas Hofstadter",
        "year": "1979",
        "language": "zh",
        "category": "philosophy",
        "topics": ["consciousness", "self-reference", "computation", "philosophy-of-mind"],
        "importance": 10.0,
        "_link_en": "Gödel, Escher, Bach: An Eternal Golden Braid",
    },
    {
        "filename": "From bacteria to Bach and back  the evolution of minds (Dennett, D. C. (Daniel Clement), author).pdf",
        "title": "From Bacteria to Bach and Back: The Evolution of Minds",
        "title_zh": "从细菌到巴赫：心智的进化",
        "author": "Daniel Dennett",
        "year": "2017",
        "language": "en",
        "category": "philosophy",
        "topics": ["consciousness", "evolution", "philosophy-of-mind"],
        "importance": 9.5,
    },
    {
        "filename": "Being and Time A Revised Edition of the Stambaugh Translation (Martin Heidegger (author) etc.).pdf",
        "title": "Being and Time",
        "title_zh": "存在与时间",
        "author": "Martin Heidegger",
        "year": "1927",
        "language": "en",
        "category": "philosophy",
        "topics": ["phenomenology", "ontology", "philosophy-of-mind"],
        "importance": 9.5,
    },
    {
        "filename": "存在与时间 修订译本_13009178.pdf",
        "title": "存在与时间",
        "title_zh": "存在与时间",
        "author": "Martin Heidegger",
        "year": "1927",
        "language": "zh",
        "category": "philosophy",
        "topics": ["phenomenology", "ontology", "philosophy-of-mind"],
        "importance": 9.5,
        "_link_en": "Being and Time",
    },
    {
        "filename": "The Human Condition (1958) (Arendt).pdf",
        "title": "The Human Condition",
        "title_zh": "人的境况",
        "author": "Hannah Arendt",
        "year": "1958",
        "language": "en",
        "category": "philosophy",
        "topics": ["political-philosophy", "ethics", "philosophy-of-mind"],
        "importance": 9.0,
    },
    {
        "filename": "人的境况_12125502.pdf",
        "title": "人的境况",
        "title_zh": "人的境况",
        "author": "Hannah Arendt",
        "year": "1958",
        "language": "zh",
        "category": "philosophy",
        "topics": ["political-philosophy", "ethics", "philosophy-of-mind"],
        "importance": 9.0,
        "_link_en": "The Human Condition",
    },
    {
        "filename": "The Myth of Sisyphus (Albert Camus).pdf",
        "title": "The Myth of Sisyphus",
        "title_zh": "西西弗斯神话",
        "author": "Albert Camus",
        "year": "1942",
        "language": "en",
        "category": "philosophy",
        "topics": ["existentialism", "absurdism", "ethics"],
        "importance": 9.0,
    },
    {
        "filename": "诺贝尔文学奖获奖者散文丛书  西西弗斯神话  青少年版_13847564.pdf",
        "title": "西西弗斯神话",
        "title_zh": "西西弗斯神话",
        "author": "Albert Camus",
        "year": "1942",
        "language": "zh",
        "category": "philosophy",
        "topics": ["existentialism", "absurdism", "ethics"],
        "importance": 9.0,
        "_link_en": "The Myth of Sisyphus",
    },
    {
        "filename": "The Structure of Scientific Revolutions_ 50th Anniversary -- Ian Hacking, Emeritus University Professor Ian Hacking.pdf",
        "title": "The Structure of Scientific Revolutions",
        "title_zh": "科学革命的结构",
        "author": "Thomas Kuhn",
        "year": "1962",
        "language": "en",
        "category": "epistemology",
        "topics": ["epistemology", "philosophy-of-science"],
        "importance": 9.5,
    },
    {
        "filename": "13227834科学革命的结构  第4版.pdf",
        "title": "科学革命的结构（第4版）",
        "title_zh": "科学革命的结构",
        "author": "Thomas Kuhn",
        "year": "1962",
        "language": "zh",
        "category": "epistemology",
        "topics": ["epistemology", "philosophy-of-science"],
        "importance": 9.5,
        "_link_en": "The Structure of Scientific Revolutions",
    },
    {
        "filename": "Conjectures and Refutations The Growth of Scientific Knowledge.pdf",
        "title": "Conjectures and Refutations: The Growth of Scientific Knowledge",
        "title_zh": "猜想与反驳：科学知识的增长",
        "author": "Karl Popper",
        "year": "1963",
        "language": "en",
        "category": "epistemology",
        "topics": ["epistemology", "philosophy-of-science", "falsificationism"],
        "importance": 9.5,
    },
    {
        "filename": "What Computers Still Can't Do _ A Critique of Artificial -- Hubert L_ Dreyfus -- MIT Press, Cambridge, Mass, 1992.pdf",
        "title": "What Computers Still Can't Do: A Critique of Artificial Reason",
        "title_zh": "计算机仍然不能做什么",
        "author": "Hubert Dreyfus",
        "year": "1992",
        "language": "en",
        "category": "ai",
        "topics": ["ai-critique", "phenomenology", "philosophy-of-mind"],
        "importance": 9.0,
    },
    {
        "filename": "The Book of Why The New Science of Cause and Effect (Judea Pearl, Dana Mackenzie).pdf",
        "title": "The Book of Why: The New Science of Cause and Effect",
        "title_zh": "为什么：因果关系的新科学",
        "author": "Judea Pearl",
        "year": "2018",
        "language": "en",
        "category": "ai",
        "topics": ["causality", "statistics", "ai"],
        "importance": 9.0,
    },
    {
        "filename": "The Question Concerning Technology  Other Essays (Martin Heidegger).pdf",
        "title": "The Question Concerning Technology and Other Essays",
        "title_zh": "技术的追问",
        "author": "Martin Heidegger",
        "year": "1954",
        "language": "en",
        "category": "philosophy",
        "topics": ["philosophy-of-technology", "phenomenology"],
        "importance": 9.0,
    },
    {
        "filename": "思考，快与慢=Thinking,Fast and Slow_13023830.pdf",
        "title": "思考，快与慢",
        "title_zh": "思考，快与慢",
        "author": "Daniel Kahneman",
        "year": "2011",
        "language": "zh",
        "category": "psychology",
        "topics": ["cognitive-science", "psychology", "decision-making"],
        "importance": 9.0,
    },
    {
        "filename": "哲学研究_13950973.pdf",
        "title": "哲学研究",
        "title_zh": "哲学研究",
        "author": "Ludwig Wittgenstein",
        "year": "1953",
        "language": "zh",
        "category": "philosophy",
        "topics": ["philosophy-of-language", "philosophy-of-mind"],
        "importance": 9.5,
    },
    {
        "filename": "13950921_尼各马可伦理学_p411.pdf",
        "title": "尼各马可伦理学",
        "title_zh": "尼各马可伦理学",
        "author": "Aristotle",
        "year": "-340",
        "language": "zh",
        "category": "philosophy",
        "topics": ["ethics", "virtue-ethics"],
        "importance": 9.5,
    },
    {
        "filename": "第一哲学沉思集  反驳和答辩_13342539.pdf",
        "title": "第一哲学沉思集：反驳和答辩",
        "title_zh": "第一哲学沉思集",
        "author": "René Descartes",
        "year": "1641",
        "language": "zh",
        "category": "philosophy",
        "topics": ["epistemology", "philosophy-of-mind", "rationalism"],
        "importance": 9.5,
    },
    {
        "filename": "13302508.pdf",
        "title": "未知书籍 (13302508)",
        "author": "Unknown",
        "year": "",
        "language": "zh",
        "category": "philosophy",
        "topics": [],
        "importance": 7.0,
    },
    # Writing books
    {
        "filename": "A Rulebook for Arguments -- Anthony Weston -- Hackett Publishing Company, Indianapolis, 2017.pdf",
        "title": "A Rulebook for Arguments",
        "title_zh": "论证手册",
        "author": "Anthony Weston",
        "year": "2017",
        "language": "en",
        "category": "writing",
        "topics": ["argumentation", "critical-thinking"],
        "importance": 8.0,
    },
    {
        "filename": "Style_ Lessons in Clarity and Grace -- Joseph M_ Williams, Joseph Bizup, Gregory G_ Colomb -- 2017.pdf",
        "title": "Style: Lessons in Clarity and Grace",
        "title_zh": "风格：清晰与优雅的写作课",
        "author": "Joseph Williams",
        "year": "2017",
        "language": "en",
        "category": "writing",
        "topics": ["writing", "style"],
        "importance": 8.0,
    },
    {
        "filename": "THE ELEMENTS OF STYLE (William Strunk, E. B. White).pdf",
        "title": "The Elements of Style",
        "title_zh": "写作风格的要素",
        "author": "William Strunk Jr., E. B. White",
        "year": "1959",
        "language": "en",
        "category": "writing",
        "topics": ["writing", "style"],
        "importance": 8.5,
    },
    {
        "filename": "The Art of Dramatic Writing_ Its Basis in the Creative -- Egri, Lajos -- Newly rev_ ed, Place of publication not identified.pdf",
        "title": "The Art of Dramatic Writing",
        "title_zh": "戏剧写作的艺术",
        "author": "Lajos Egri",
        "year": "1960",
        "language": "en",
        "category": "writing",
        "topics": ["writing", "drama", "storytelling"],
        "importance": 8.0,
    },
    {
        "filename": "《金字塔原理思考、表达和解决问题的逻辑》_13441941.pdf",
        "title": "金字塔原理：思考、表达和解决问题的逻辑",
        "title_zh": "金字塔原理",
        "author": "Barbara Minto",
        "year": "1987",
        "language": "zh",
        "category": "writing",
        "topics": ["writing", "logic", "communication"],
        "importance": 8.0,
    },
]


def extract_text_by_page(pdf_path):
    """Extract text from each page of a PDF. Returns list of (page_num, text)."""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            pages.append((i + 1, text))
    doc.close()
    return pages


def detect_chapters(doc, pages_text):
    """Detect chapter boundaries. Uses TOC if available, else regex."""
    toc = doc.get_toc()
    if toc and len(toc) >= 3:
        # Filter to level-1 entries (or level-2 if no level-1)
        levels = set(e[0] for e in toc)
        target_level = min(levels)
        chapters = []
        for level, title, page_num in toc:
            if level <= target_level + 1:
                chapters.append({
                    'title': title.strip(),
                    'start_page': page_num,
                    'level': level,
                })
        # Only keep if we have a reasonable number
        if len(chapters) >= 2:
            return chapters

    # Fallback: regex chapter detection
    chapter_patterns = [
        re.compile(r'^(?:Chapter|CHAPTER)\s+(\d+|[IVXLC]+)[.:)?\s]*(.*)', re.MULTILINE),
        re.compile(r'^第[一二三四五六七八九十百]+[章节篇]\s*(.*)', re.MULTILINE),
        re.compile(r'^(\d+)\.\s+([A-Z].*)', re.MULTILINE),
    ]

    chapters = []
    for page_num, text in pages_text:
        for pat in chapter_patterns:
            for m in pat.finditer(text[:500]):  # only check top of page
                title = m.group(0).strip()[:100]
                chapters.append({
                    'title': title,
                    'start_page': page_num,
                    'level': 1,
                })
                break

    return chapters if len(chapters) >= 2 else []


def chunk_text(text, chunk_chars=CHUNK_CHARS, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks by paragraph boundaries."""
    paragraphs = text.split('\n\n')
    chunks = []
    current = []
    current_len = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if current_len + len(para) > chunk_chars and current:
            chunks.append('\n\n'.join(current))
            # Keep last paragraph for overlap
            overlap_paras = []
            overlap_len = 0
            for p in reversed(current):
                if overlap_len + len(p) > overlap:
                    break
                overlap_paras.insert(0, p)
                overlap_len += len(p)
            current = overlap_paras
            current_len = overlap_len
        current.append(para)
        current_len += len(para)

    if current:
        chunks.append('\n\n'.join(current))

    return chunks


def ingest():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    # Check if migration was run
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
    if not c.fetchone():
        print("ERROR: Run migrate_books.py first!")
        sys.exit(1)

    # Track existing books to avoid duplicates
    c.execute("SELECT filename FROM books")
    existing = {row['filename'] for row in c.fetchall()}

    # Build title→id map for linking
    title_to_id = {}

    total_chapters = 0
    total_chunks = 0

    for meta in BOOKS:
        fname = meta['filename']
        if fname in existing:
            print(f"  SKIP (exists): {fname[:60]}")
            continue

        pdf_path = os.path.join(PDF_DIR, fname)
        if not os.path.exists(pdf_path):
            print(f"  MISSING: {pdf_path}")
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {meta['title']}")

        doc = fitz.open(pdf_path)
        page_count = len(doc)

        # Extract text
        pages_text = extract_text_by_page(pdf_path)
        print(f"  Pages with text: {len(pages_text)}/{page_count}")

        # Detect chapters
        chapters = detect_chapters(doc, pages_text)
        doc.close()

        # Insert book
        c.execute("""INSERT INTO books (title, title_zh, author, year, language,
                     filename, page_count, category, importance, topics, level)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                  (meta['title'], meta.get('title_zh'), meta['author'], meta['year'],
                   meta.get('language', 'en'), fname, page_count,
                   meta['category'], meta['importance'],
                   json.dumps(meta.get('topics', [])), 'essential'))
        book_id = c.lastrowid
        title_to_id[meta['title']] = book_id

        # Build page→text mapping
        page_text_map = {pn: txt for pn, txt in pages_text}

        if chapters:
            print(f"  Chapters detected: {len(chapters)}")
            # Set end pages
            for i, ch in enumerate(chapters):
                if i + 1 < len(chapters):
                    ch['end_page'] = chapters[i + 1]['start_page'] - 1
                else:
                    ch['end_page'] = page_count

            for i, ch in enumerate(chapters):
                # Collect chapter text
                ch_text_parts = []
                for pn in range(ch['start_page'], ch['end_page'] + 1):
                    if pn in page_text_map:
                        ch_text_parts.append(page_text_map[pn])
                ch_text = '\n\n'.join(ch_text_parts)

                if not ch_text.strip():
                    continue

                c.execute("""INSERT INTO book_chapters
                             (book_id, chapter_num, title, start_page, end_page, content, word_count)
                             VALUES (?,?,?,?,?,?,?)""",
                          (book_id, i + 1, ch['title'], ch['start_page'],
                           ch['end_page'], ch_text, len(ch_text.split())))
                chapter_id = c.lastrowid
                total_chapters += 1

                # Chunk the chapter
                chunks = chunk_text(ch_text)
                for ci, chunk in enumerate(chunks):
                    c.execute("""INSERT INTO book_chunks
                                 (book_id, chapter_id, chunk_index, content, page_start, page_end)
                                 VALUES (?,?,?,?,?,?)""",
                              (book_id, chapter_id, ci, chunk,
                               ch['start_page'], ch['end_page']))
                    total_chunks += 1
        else:
            # No chapters detected — treat whole book as one chapter
            print("  No chapters detected, treating as single chapter")
            all_text = '\n\n'.join(txt for _, txt in pages_text)
            c.execute("""INSERT INTO book_chapters
                         (book_id, chapter_num, title, start_page, end_page, content, word_count)
                         VALUES (?,?,?,?,?,?,?)""",
                      (book_id, 1, meta['title'], 1, page_count,
                       all_text, len(all_text.split())))
            chapter_id = c.lastrowid
            total_chapters += 1

            chunks = chunk_text(all_text)
            for ci, chunk in enumerate(chunks):
                c.execute("""INSERT INTO book_chunks
                             (book_id, chapter_id, chunk_index, content, page_start, page_end)
                             VALUES (?,?,?,?,?,?)""",
                          (book_id, chapter_id, ci, chunk, 1, page_count))
                total_chunks += 1

        print(f"  Chunks created: {total_chunks}")

    # Link EN↔ZH versions
    print("\nLinking EN↔ZH versions...")
    for meta in BOOKS:
        link_title = meta.get('_link_en')
        if link_title and link_title in title_to_id:
            en_id = title_to_id[link_title]
            zh_id = title_to_id.get(meta['title'])
            if zh_id:
                c.execute("UPDATE books SET linked_book_id=? WHERE id=?", (en_id, zh_id))
                c.execute("UPDATE books SET linked_book_id=? WHERE id=?", (zh_id, en_id))
                print(f"  Linked: {link_title} <-> {meta['title']}")

    conn.commit()

    # Stats
    c.execute("SELECT count(*) FROM books")
    print(f"\n=== Ingestion complete ===")
    print(f"Books: {c.fetchone()[0]}")
    print(f"Chapters: {total_chapters}")
    print(f"Chunks: {total_chunks}")

    conn.close()


if __name__ == '__main__':
    ingest()
