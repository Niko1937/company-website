(function () {
  'use strict';

  // Card lists that are grids on tablets and desktops but a swipeable row on phones (Services, Case Studies),
  // looking and working like the Solutions rows.
  //   [data-carousel]       : the list. The page CSS turns it into a row below 768px.
  //   [data-carousel-pager] : "1–2 / 6" and the arrows, right after the list. Shown only while the row overflows,
  //                           so it stays hidden wherever the list is a grid.
  // Hiding cards (the Case Studies filter) recounts the cards and goes back to the first one.

  function reduceMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function cards(track) {
    return Array.from(track.children).filter(card => !card.hidden);
  }

  // "1–2 / 6": the cards that are (mostly) in view. A card peeking in at the edge does not count.
  function visibleRange(track) {
    const list = cards(track);
    const view = track.getBoundingClientRect();
    const shown = [];
    list.forEach((card, i) => {
      const r = card.getBoundingClientRect();
      const visible = Math.min(r.right, view.right) - Math.max(r.left, view.left);
      if (r.width && visible / r.width >= 0.75) shown.push(i + 1);
    });
    if (!shown.length) return '';
    const first = shown[0], last = shown[shown.length - 1];
    return `${first === last ? first : `${first}–${last}`} / ${list.length}`;
  }

  function setUp(track) {
    const pager = track.nextElementSibling;
    if (!pager || !pager.matches('[data-carousel-pager]')) return;
    const count = pager.querySelector('[data-carousel-count]');
    const prev = pager.querySelector('[data-carousel-prev]');
    const next = pager.querySelector('[data-carousel-next]');

    function update() {
      const max = track.scrollWidth - track.clientWidth;
      pager.hidden = max <= 1;
      if (pager.hidden) return;
      prev.disabled = track.scrollLeft <= 1;
      next.disabled = track.scrollLeft >= max - 1;
      count.textContent = visibleRange(track);
    }

    function step(dir) {
      const first = cards(track)[0];
      if (!first) return;
      const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
      track.scrollBy({ left: dir * (first.offsetWidth + gap), behavior: reduceMotion() ? 'auto' : 'smooth' });
    }

    let ticking = false;
    track.addEventListener('scroll', () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => { update(); ticking = false; });
    }, { passive: true });
    prev.addEventListener('click', () => step(-1));
    next.addEventListener('click', () => step(1));
    new ResizeObserver(update).observe(track);
    // Only cards being shown or hidden count, not elements inside a card (the Case Studies dialog moves those).
    new MutationObserver(records => {
      if (!records.some(r => r.target.parentElement === track)) return;
      track.scrollLeft = 0;
      update();
    }).observe(track, { attributes: true, attributeFilter: ['hidden'], subtree: true });
    update();
  }

  document.querySelectorAll('[data-carousel]').forEach(setUp);
})();
