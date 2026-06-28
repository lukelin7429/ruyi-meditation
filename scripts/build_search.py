#!/usr/bin/env python3
"""
Build the site-wide search index and wire the search box into hand-built pages.

Outputs:
  - /search.json        a single flat index of every public page
  - injects the search trigger button + assets into standalone HTML pages
    (the Jekyll-rendered pages get the button from _includes/header.html)

Re-run after adding columns, lessons, or discourses:
    python3 scripts/build_search.py
Idempotent — safe to run repeatedly.
"""
import os, re, json, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {'_site', '_layouts', '_includes', 'node_modules', 'vendor',
             '.git', 'scripts', 'apps-script', 'logos', 'assets', '_data'}

CSS_LINK = '<link rel="stylesheet" href="/assets/css/search.css">'
JS_TAG   = '<script defer src="/assets/js/search.js"></script>'
BUTTON = (
    '\n    <button type="button" class="nav-search-btn" id="siteSearchBtn" '
    'aria-label="Search this site" title="Search (press /)">'
    '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/>'
    '<line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>'
    '<span class="nav-search-label">Search</span><kbd>/</kbd></button>'
)

TAG_RE     = re.compile(r'<[^>]+>')
LIQUID_RE  = re.compile(r'\{%.*?%\}|\{\{.*?\}\}', re.S)
SCRIPT_RE  = re.compile(r'<(script|style|svg)\b.*?</\1>', re.S | re.I)
BLOCK_RE   = re.compile(r'<(header|footer|nav)\b.*?</\1>', re.S | re.I)
WS_RE      = re.compile(r'\s+')
HDR_CLOSE  = re.compile(r'</nav>(\s*</div>\s*</header>)', re.S)
TITLE_RE   = re.compile(r'<title>(.*?)</title>', re.S | re.I)
DESC_RE    = re.compile(r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']', re.S | re.I)
BODY_RE    = re.compile(r'<body\b[^>]*>(.*?)</body>', re.S | re.I)

import html as _html

def clean(text, limit=280):
    text = _html.unescape(WS_RE.sub(' ', text)).strip()
    return text[:limit].rstrip() + ('…' if len(text) > limit else '')

def strip_title_suffix(t):
    t = _html.unescape(t).strip()
    for sep in (' | ', ' · '):
        if sep in t and 'Ru-Yi' in t.split(sep)[-1]:
            t = sep.join(t.split(sep)[:-1])
    return t.strip()

def parse_front_matter(raw):
    if not raw.startswith('---'):
        return None, raw
    end = raw.find('\n---', 3)
    if end == -1:
        return None, raw
    fm_block = raw[3:end]
    body = raw[end + 4:]
    fm = {}
    for line in fm_block.splitlines():
        m = re.match(r'^([A-Za-z0-9_\-]+):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"\'')
    return fm, body

def url_for(relpath):
    rel = relpath.replace(os.sep, '/')
    if rel == 'index.html':
        return '/'
    if rel.endswith('/index.html'):
        return '/' + rel[:-len('index.html')]
    return '/' + rel

def text_from_html_body(raw):
    m = BODY_RE.search(raw)
    chunk = m.group(1) if m else raw
    chunk = SCRIPT_RE.sub(' ', chunk)
    chunk = BLOCK_RE.sub(' ', chunk)
    chunk = TAG_RE.sub(' ', chunk)
    return chunk

def md_to_text(body):
    body = LIQUID_RE.sub(' ', body)
    body = SCRIPT_RE.sub(' ', body)
    body = TAG_RE.sub(' ', body)
    body = re.sub(r'[#>*_`\-\|]+', ' ', body)
    return body

# ---------- build index ----------
entries = []

# 1) Columns collection (markdown)
for path in sorted(glob.glob(os.path.join(ROOT, '_columns', '*.md'))):
    raw = open(path, encoding='utf-8').read()
    fm, body = parse_front_matter(raw)
    if not fm:
        continue
    slug = os.path.splitext(os.path.basename(path))[0]
    entries.append({
        'title': fm.get('title', slug),
        'url': '/columns/%s/' % slug,
        'date': (fm.get('original_date') or fm.get('date') or '')[:4],
        'tags': fm.get('tags', '').strip('[]'),
        'body': clean(md_to_text(body)),
    })

# 2) All HTML pages
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
    for fn in filenames:
        if not fn.endswith('.html'):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        if rel.split(os.sep)[0] in SKIP_DIRS:
            continue
        raw = open(full, encoding='utf-8').read()
        fm, body = parse_front_matter(raw)
        url = url_for(rel)
        if fm is not None:                      # Jekyll-rendered page
            title = fm.get('title')
            if not title:
                continue
            text = md_to_text(body)
        else:                                   # standalone hand-built page
            mt = TITLE_RE.search(raw)
            title = strip_title_suffix(mt.group(1)) if mt else None
            if not title:
                continue
            md = DESC_RE.search(raw)
            desc = md.group(1) + ' ' if md else ''
            text = desc + text_from_html_body(raw)
        entries.append({
            'title': title,
            'url': url,
            'date': (fm.get('original_date') or fm.get('date') or '')[:4] if fm else '',
            'tags': (fm.get('tags', '').strip('[]') if fm else ''),
            'body': clean(text),
        })

# de-dup by url, write
seen, unique = set(), []
for e in entries:
    if e['url'] in seen:
        continue
    seen.add(e['url'])
    unique.append(e)
unique.sort(key=lambda e: e['url'])

with open(os.path.join(ROOT, 'search.json'), 'w', encoding='utf-8') as f:
    json.dump(unique, f, ensure_ascii=False, indent=0, separators=(',', ':'))
    f.write('\n')
print('search.json: %d pages indexed' % len(unique))

# ---------- inject search box into standalone pages ----------
injected = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith('.')]
    for fn in filenames:
        if not fn.endswith('.html'):
            continue
        full = os.path.join(dirpath, fn)
        raw = open(full, encoding='utf-8').read()
        if raw.lstrip().startswith('---'):
            continue                            # Jekyll page — uses the include
        if 'id="siteSearchBtn"' in raw:
            continue                            # already wired
        if '<header class="site-header"' not in raw or not HDR_CLOSE.search(raw):
            continue                            # no shared header to attach to
        new = raw
        if CSS_LINK not in new and '</head>' in new:
            new = new.replace('</head>', '  ' + CSS_LINK + '\n</head>', 1)
        new = HDR_CLOSE.sub(lambda m: '</nav>' + BUTTON + m.group(1), new, count=1)
        if JS_TAG not in new and '</body>' in new:
            new = new.replace('</body>', '  ' + JS_TAG + '\n</body>', 1)
        if new != raw:
            open(full, 'w', encoding='utf-8').write(new)
            injected += 1
print('search box injected into %d standalone pages' % injected)
