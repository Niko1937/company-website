// Rows swiped sideways on phones (How it works, Privacy; built by scripts/app_pages/build.py), as on the
// Quests home page: below each, "1 / 3" and arrows, shown only while the row is wider than the screen.
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-swipe]').forEach(function (track) {
    var pager = track.nextElementSibling;
    if (!pager || !pager.hasAttribute('data-swipe-pager')) return;
    var count = pager.querySelector('[data-swipe-count]');
    var prev = pager.querySelector('[data-swipe-prev]');
    var next = pager.querySelector('[data-swipe-next]');
    var items = track.children;
    function step() {
      var first = items[0];
      return first ? first.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 0) : 0;
    }
    function update() {
      var overflowing = track.scrollWidth > track.clientWidth + 1;
      pager.hidden = !overflowing;
      if (!overflowing) return;
      var max = track.scrollWidth - track.clientWidth;
      var index = Math.min(items.length - 1, Math.round(track.scrollLeft / (step() || 1)));
      if (track.scrollLeft >= max - 1) index = items.length - 1;
      count.textContent = (index + 1) + ' / ' + items.length;
      prev.disabled = track.scrollLeft <= 1;
      next.disabled = track.scrollLeft >= max - 1;
    }
    function go(direction) {
      track.scrollBy({ left: direction * step(), behavior: reduce.matches ? 'auto' : 'smooth' });
    }
    prev.addEventListener('click', function () { go(-1); });
    next.addEventListener('click', function () { go(1); });
    var frame = 0;
    track.addEventListener('scroll', function () {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(update);
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  });
})();
