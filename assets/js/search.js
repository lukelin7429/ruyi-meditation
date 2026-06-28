/* Ru-Yi Meditation Center — site-wide search (client-side, zero dependency) */
(function () {
  var btn = document.getElementById('siteSearchBtn');
  if (!btn) return;

  var index = null;          // loaded search corpus
  var overlay = null, input = null, list = null, emptyEl = null;
  var rows = [];             // current rendered result rows
  var active = -1;
  var loading = false;

  var SECTIONS = {
    about: 'About', columns: 'Column', dharma: 'Dharma', discourses: 'Discourse',
    forbearance: 'Dharma', 'three-refuges': 'Dharma', 'english-school': 'English School',
    community: 'Community', registration: 'Community'
  };

  function sectionOf(url) {
    var seg = (url || '').split('/').filter(Boolean)[0] || '';
    if (SECTIONS[seg]) return SECTIONS[seg];
    if (!seg) return 'Home';
    return seg.charAt(0).toUpperCase() + seg.slice(1);
  }

  function load() {
    if (index || loading) return Promise.resolve();
    loading = true;
    return fetch('/search.json', { credentials: 'same-origin' })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        index = data.map(function (it) {
          var title = it.title || '';
          var tags = it.tags || '';
          var body = it.body || '';
          return {
            title: title, url: it.url, date: it.date || '',
            tags: tags, body: body, section: sectionOf(it.url),
            hay: (title + ' ' + tags + ' ' + body).toLowerCase()
          };
        });
        loading = false;
      })
      .catch(function () { loading = false; });
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function highlight(text, words) {
    var out = esc(text);
    words.forEach(function (w) {
      if (!w) return;
      var re = new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig');
      out = out.replace(re, '<mark>$1</mark>');
    });
    return out;
  }

  function snippet(body, words) {
    var lc = body.toLowerCase();
    var pos = -1;
    for (var i = 0; i < words.length; i++) {
      var p = lc.indexOf(words[i]);
      if (p !== -1 && (pos === -1 || p < pos)) pos = p;
    }
    if (pos > 60) body = '…' + body.slice(pos - 50);
    return body.length > 160 ? body.slice(0, 160) + '…' : body;
  }

  function search(q) {
    q = q.trim().toLowerCase();
    if (!q) return [];
    var words = q.split(/\s+/);
    var res = [];
    index.forEach(function (it) {
      var ok = true, score = 0;
      for (var i = 0; i < words.length; i++) {
        var w = words[i];
        if (it.hay.indexOf(w) === -1) { ok = false; break; }
        if (it.title.toLowerCase().indexOf(w) !== -1) score += 12;
        if (it.tags.toLowerCase().indexOf(w) !== -1) score += 4;
        score += 1;
      }
      if (ok) res.push({ it: it, score: score });
    });
    res.sort(function (a, b) { return b.score - a.score; });
    return res.slice(0, 14).map(function (r) { return r.it; });
  }

  function render(q) {
    var results = q.trim() ? search(q) : [];
    var words = q.trim().toLowerCase().split(/\s+/);
    rows = results;
    active = results.length ? 0 : -1;
    if (!q.trim()) {
      list.innerHTML = '';
      emptyEl.hidden = true;
      return;
    }
    if (!results.length) {
      list.innerHTML = '';
      emptyEl.hidden = false;
      return;
    }
    emptyEl.hidden = true;
    list.innerHTML = results.map(function (it, i) {
      return '<li class="rs-item' + (i === 0 ? ' is-active' : '') + '" role="option" data-url="' + esc(it.url) + '">' +
        '<a href="' + esc(it.url) + '" tabindex="-1">' +
        '<span class="rs-sec">' + esc(it.section) + (it.date ? ' · ' + esc(it.date) : '') + '</span>' +
        '<span class="rs-title">' + highlight(it.title, words) + '</span>' +
        (it.body ? '<span class="rs-snippet">' + highlight(snippet(it.body, words), words) + '</span>' : '') +
        '</a></li>';
    }).join('');
    Array.prototype.forEach.call(list.children, function (li, i) {
      li.addEventListener('mousemove', function () { setActive(i); });
    });
  }

  function setActive(i) {
    if (i < 0 || i >= rows.length) return;
    active = i;
    Array.prototype.forEach.call(list.children, function (li, j) {
      li.classList.toggle('is-active', j === i);
    });
    var el = list.children[i];
    if (el) el.scrollIntoView({ block: 'nearest' });
  }

  function go(i) {
    if (i < 0 || i >= rows.length) return;
    window.location.href = rows[i].url;
  }

  function onKey(e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); setActive(Math.min(active + 1, rows.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
    else if (e.key === 'Enter') { e.preventDefault(); go(active < 0 ? 0 : active); }
    else if (e.key === 'Escape') { e.preventDefault(); close(); }
  }

  function build() {
    overlay = document.createElement('div');
    overlay.className = 'rs-overlay';
    overlay.innerHTML =
      '<div class="rs-modal" role="dialog" aria-modal="true" aria-label="Search this site">' +
        '<div class="rs-bar">' +
          '<svg class="rs-mag" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>' +
          '<input type="search" class="rs-input" placeholder="Search teachings, columns, lessons…" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Search query">' +
          '<kbd class="rs-esc">esc</kbd>' +
        '</div>' +
        '<ul class="rs-results" role="listbox"></ul>' +
        '<div class="rs-empty" hidden>No matches — try another word.</div>' +
        '<div class="rs-foot"><span><kbd>↑</kbd><kbd>↓</kbd> to navigate</span><span><kbd>↵</kbd> to open</span><span><kbd>esc</kbd> to close</span></div>' +
      '</div>';
    document.body.appendChild(overlay);
    input = overlay.querySelector('.rs-input');
    list = overlay.querySelector('.rs-results');
    emptyEl = overlay.querySelector('.rs-empty');
    overlay.addEventListener('mousedown', function (e) { if (e.target === overlay) close(); });
    overlay.querySelector('.rs-esc').addEventListener('click', close);
    input.addEventListener('input', function () { render(input.value); });
    input.addEventListener('keydown', onKey);
    list.addEventListener('mousedown', function (e) {
      var li = e.target.closest('.rs-item');
      if (li) { e.preventDefault(); window.location.href = li.getAttribute('data-url'); }
    });
  }

  function open() {
    if (!overlay) build();
    load();
    document.documentElement.classList.add('rs-open');
    overlay.classList.add('is-open');
    input.value = '';
    render('');
    setTimeout(function () { input.focus(); }, 20);
  }

  function close() {
    if (!overlay) return;
    overlay.classList.remove('is-open');
    document.documentElement.classList.remove('rs-open');
  }

  btn.addEventListener('click', open);

  document.addEventListener('keydown', function (e) {
    var open_ = overlay && overlay.classList.contains('is-open');
    var typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName) ||
                 document.activeElement.isContentEditable;
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) {
      e.preventDefault(); open_ ? close() : open();
    } else if (e.key === '/' && !open_ && !typing) {
      e.preventDefault(); open();
    }
  });
})();
