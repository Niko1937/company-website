(function () {
  'use strict';

  // In-page links (#services, #solutions, ...): the URL shows the section without adding history entries, and a
  // link opened from outside shows its section right away. #solutions-<id> also opens that demo (solutions.js).
  // The header offset comes from scroll-margin-top in the page CSS.
  const DEMO = /^#solutions-([a-z0-9-]+)$/;

  function reduceMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function setHash(hash) {
    history.replaceState(history.state, '', location.pathname + location.search + hash);
  }

  // Returns the element a hash points to, or null when it is missing or hidden.
  function targetOf(hash) {
    const demo = hash.match(DEMO);
    let id = demo ? 'solutions' : hash.slice(1);
    try { id = decodeURIComponent(id); } catch (_) { return null; }
    const el = id && document.getElementById(id);
    return el && el.getClientRects().length ? el : null;
  }

  // Shows the section for a hash. Returns false when there is nothing to show.
  // Uses the layout position (offsetTop), not scrollIntoView, so the .section-fade slide-in transform cannot shift it.
  function go(hash, behavior, openDemo) {
    const target = targetOf(hash);
    if (!target) return false;
    let top = 0;
    for (let el = target; el; el = el.offsetParent) top += el.offsetTop;
    window.scrollTo({ top: top - (parseFloat(getComputedStyle(target).scrollMarginTop) || 0), behavior });
    const demo = hash.match(DEMO);
    if (demo && openDemo && !(window.solutions && window.solutions.open(demo[1]))) setHash('#solutions');
    return true;
  }

  document.addEventListener('click', e => {
    const link = e.target.closest('a[href^="#"]');
    if (!link || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    e.preventDefault();
    const hash = link.getAttribute('href');
    if (go(hash, reduceMotion() ? 'auto' : 'smooth', true)) setHash(hash === '#hero' ? '' : hash);
  });

  window.addEventListener('hashchange', () => go(location.hash, reduceMotion() ? 'auto' : 'smooth', true));

  // Opened with a hash: the browser jumps there while the page is still loading, but translations, the Solutions
  // cards, and images can move the section afterwards. Jump again (without animation) once each of them is in
  // place, unless the visitor has already started scrolling.
  if (!location.hash) return;
  let moved = false;
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(type =>
    window.addEventListener(type, () => { moved = true; }, { once: true, passive: true }));
  let first = true;
  const settle = () => {
    if (moved || !location.hash) return;
    go(location.hash, 'auto', first);
    first = false;
  };
  if (window.__translations) settle();
  else document.addEventListener('i18n:changed', function onFirst() {
    document.removeEventListener('i18n:changed', onFirst);
    settle();
  });
  if (document.readyState === 'complete') settle();
  else window.addEventListener('load', settle, { once: true });
})();
