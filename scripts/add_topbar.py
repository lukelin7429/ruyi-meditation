#!/usr/bin/env python3
"""
Add the canonical Ru-Yi top bar to the standalone (non-Jekyll) pages that don't
get it from the shared _includes/header.html — namely the Forbearance page and
every Majjhima Nikāya discourse page (index + mn-*.html).

These pages are authored/imported as full standalone HTML, so they need the
header injected directly. This script is IDEMPOTENT: it skips any page that
already has the top bar, so it is safe to re-run after the discourse pipeline
adds new MN pages. Run from the repo root:  python3 scripts/add_topbar.py
"""
import glob, re, os

# The header markup must match _includes/header.html (same links, same labels).
# Dharma is marked active since all these pages live under the Dharma section.
HEADER = '''<header class="site-header">
  <div class="header-inner">
    <a href="/" class="brand">
      <img src="/logos/ruyi-logo-green.png" alt="Ru-Yi Meditation Center" class="brand-logo">
      <span class="brand-name">Ru-Yi <em>Meditation Center</em></span>
    </a>
    <nav class="site-nav" aria-label="Primary">
      <a href="/">Home</a>
      <a href="/about/">About</a>
      <a href="/columns/">Columns</a>
      <a href="/dharma/" class="active">Dharma</a>
      <a href="/english-school/">English School</a>
      <a href="/community/">Community</a>
    </nav>
  </div>
</header>
'''

# Self-contained CSS, scoped under .site-header so it can never touch the host
# page's own styles. position:static so it never fights the reading pages'
# existing sticky elements (the .tabs bar, the sticky sidebar). Visually it is
# identical to the sticky site header on the rest of the site.
CSS = '''<style id="ruyi-topbar">
.site-header{background:#fff;border-bottom:1px solid #e7e7ea;position:static;font-family:'Inter',sans-serif;}
.site-header *{box-sizing:border-box;}
.site-header .header-inner{max-width:1280px;margin:0 auto;padding:0 56px;display:flex;align-items:center;justify-content:space-between;min-height:72px;gap:32px;}
.site-header .brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;color:inherit;}
.site-header .brand:hover{text-decoration:none;}
.site-header .brand-logo{height:44px;width:44px;display:block;flex-shrink:0;}
.site-header .brand-name{font-family:'Playfair Display',serif;font-size:19px;font-weight:500;color:#1a1a1a;letter-spacing:.005em;line-height:1.1;}
.site-header .brand-name em{display:block;font-style:italic;font-weight:400;color:#559986;font-size:12px;letter-spacing:.18em;text-transform:uppercase;margin-top:2px;}
.site-header .site-nav{display:flex;gap:32px;}
.site-header .site-nav a{font-size:15px;font-weight:500;color:#4a4d53;text-decoration:none;letter-spacing:.01em;padding:4px 0;position:relative;}
.site-header .site-nav a:hover{color:#8c2f12;text-decoration:none;}
.site-header .site-nav a.active{color:#1a1a1a;}
.site-header .site-nav a.active::after{content:"";position:absolute;left:0;right:0;bottom:-22px;height:2px;background:#b8431c;}
@media (max-width:720px){.site-header .header-inner{padding:0 22px;min-height:64px;gap:14px;flex-wrap:wrap;}.site-header .brand-name{display:none;}.site-header .site-nav{gap:16px;}.site-header .site-nav a{font-size:14px;}.site-header .site-nav a.active::after{display:none;}}
</style>
'''

TARGETS = ['forbearance/index.html'] + sorted(glob.glob('discourses/majjhima-nikaya/*.html'))

changed, skipped = [], []
for path in TARGETS:
    if not os.path.exists(path):
        continue
    html = open(path, encoding='utf-8').read()
    # skip Jekyll pages (they get the header from the include) and already-done pages
    if html.lstrip().startswith('---') or 'class="site-header"' in html:
        skipped.append(path); continue
    if '</head>' not in html or '<body' not in html:
        skipped.append(path); continue
    # inject CSS before </head>
    html = html.replace('</head>', CSS + '</head>', 1)
    # inject header right after the opening <body ...> tag
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + HEADER, html, count=1)
    open(path, 'w', encoding='utf-8').write(html)
    changed.append(path)

print(f"top bar added to {len(changed)} page(s); skipped {len(skipped)} (Jekyll or already done).")
for p in changed[:6]:
    print("  +", p)
if len(changed) > 6:
    print(f"  … and {len(changed)-6} more")
