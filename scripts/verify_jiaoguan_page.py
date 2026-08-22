#!/usr/bin/env python3
"""Verify a jiaoguan-gangzong page against the CBETA base text (T1939).

Usage: python3 verify_jiaoguan_page.py <page.html> <start_line> <end_line>

Checks:
  - div/section open/close balance
  - depth-counted extraction of top-level <div class="source ..."> blocks
    (class-token aware: "source verse" matches "source"; "translation-table"
    does NOT match "translation" since tokens are split on whitespace)
  - CJK coverage vs. base text lines [start_line, end_line] via difflib
  - CJK char count in translation columns must be 0
  - flags British spellings
"""
import sys, re, difflib

BASE = "/Users/hayashikisshou/Library/Mobile Documents/iCloud~md~obsidian/Documents/第二個大腦/知識庫/佛法/大正藏/19_諸宗部/T1939_教觀綱宗.md"

TAG_RE = re.compile(r'<(/?)div\b([^>]*)>')

def class_tokens(tag_attrs):
    m = re.search(r'class="([^"]*)"', tag_attrs)
    return set(m.group(1).split()) if m else set()

def extract_top_level_blocks(html, wanted_token):
    blocks = []
    depth = 0
    target_stack = []
    open_target_start = None
    for m in TAG_RE.finditer(html):
        closing = m.group(1) == '/'
        if not closing:
            toks = class_tokens(m.group(2))
            is_target = wanted_token in toks
            if is_target and not target_stack:
                open_target_start = m.end()
                target_stack.append(depth)
            elif is_target:
                target_stack.append(depth)
            depth += 1
        else:
            depth -= 1
            if target_stack and depth == target_stack[-1]:
                target_stack.pop()
                if not target_stack:
                    blocks.append(html[open_target_start:m.start()])
                    open_target_start = None
    return blocks

def cjk_chars(text):
    text = re.sub(r'<[^>]+>', '', text)
    return re.findall(r'[一-鿿]', text)

def check_balance(html):
    problems = []
    for tag in ['div', 'section']:
        opens = len(re.findall(rf'<{tag}\b', html))
        closes = len(re.findall(rf'</{tag}>', html))
        if opens != closes:
            problems.append(f"{tag}: {opens} open vs {closes} close")
    return problems

def main():
    path = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    html = open(path, encoding='utf-8').read()

    print(f"=== {path} (base lines {start}-{end}) ===")
    bal = check_balance(html)
    print("BALANCE PROBLEMS:" if bal else "div/section balance: OK", bal if bal else "")

    source_blocks = extract_top_level_blocks(html, 'source')
    trans_blocks = extract_top_level_blocks(html, 'translation')

    src_chars = []
    for b in source_blocks:
        src_chars.extend(cjk_chars(b))
    src_text = ''.join(src_chars)

    trans_chars = []
    for b in trans_blocks:
        trans_chars.extend(cjk_chars(b))

    print(f"source blocks found: {len(source_blocks)}, CJK chars: {len(src_chars)}")
    print(f"translation blocks found: {len(trans_blocks)}, CJK chars (should be 0): {len(trans_chars)}")
    if trans_chars:
        print("  -> LEAK:", ''.join(trans_chars)[:200])

    base_lines = open(BASE, encoding='utf-8').read().split('\n')
    base_slice = '\n'.join(base_lines[start-1:end])
    base_cjk = ''.join(re.findall(r'[一-鿿]', base_slice))

    sm = difflib.SequenceMatcher(None, base_cjk, src_text, autojunk=False)
    matching = sum(b.size for b in sm.get_matching_blocks())
    coverage = matching / len(base_cjk) * 100 if base_cjk else 0
    print(f"base text CJK chars [{start}:{end}]: {len(base_cjk)}")
    print(f"coverage: {coverage:.1f}%")

    print("GAPS (base text present, not matched in page source, >3 chars):")
    gap_found = False
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ('delete', 'replace') and (i2 - i1) > 3:
            gap_found = True
            snippet = base_cjk[i1:i2]
            print(f"  [{tag}] base[{i1}:{i2}] = {snippet[:100]}")
    if not gap_found:
        print("  none")

    brit = re.findall(r'\b(practise[sd]?|behaviour|colour|organi[sz]e|counselling|judgement|cancelled|centre|defence|licence)\b', html, re.I)
    print("BRITISH SPELLING FLAGS:" if brit else "British spelling check: OK", set(brit) if brit else "")

if __name__ == '__main__':
    main()
