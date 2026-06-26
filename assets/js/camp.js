/* Summer Camp — inline video lightbox + gentle reveal.
   Videos always play on the page (youtube.com/embed, never a pop-out). */
(function () {
  document.body.classList.add('camp-js');

  var lb = document.getElementById('camp-lb');
  var frame = lb ? lb.querySelector('.camp-lb-frame') : null;

  function open(id) {
    if (!lb || !frame) return;
    frame.innerHTML =
      '<iframe src="https://www.youtube.com/embed/' + id +
      '?autoplay=1&rel=0&modestbranding=1" title="Ru-Yi Summer Camp" ' +
      'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>';
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    if (!lb || !frame) return;
    lb.classList.remove('open');
    frame.innerHTML = '';
    document.body.style.overflow = '';
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('.vthumb');
    if (btn) { open(btn.getAttribute('data-yt')); return; }
    if (e.target === lb || (e.target.classList && e.target.classList.contains('camp-lb-close'))) {
      close();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  /* Gentle reveal on scroll. Defaults to visible if anything fails. */
  var items = [].slice.call(document.querySelectorAll('.reveal'));
  if ('IntersectionObserver' in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }
})();
