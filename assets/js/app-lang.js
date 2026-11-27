// The app pages' language links (built by scripts/app_pages/build.py) opens the same page in the other language
// where the reader was, as the Quests site's switch does, instead of at the top.
// Both languages are built from the same template, so the n-th block of text in one is the n-th in the other:
// the link remembers the block at the top of the screen and where it sat (or, when it runs under the header, how
// far into it the screen starts, as a share of its height, since the other language's block is taller or shorter),
// and the new page puts it there.
(function () {
  var KEY = 'appLangPosition';
  var BLOCKS = 'main h1, main h2, main h3, main p, main li, main figure, main summary, main dt, main dd, main form';
  function header() {
    var h = document.querySelector('.app-header');
    return h ? h.getBoundingClientRect().bottom : 0;
  }

  // The other language's links: in the switcher from 1024px, and the globe below it.
  var links = document.querySelectorAll('.app-header .lang-switcher a:not(.lang-active), .app-header a.lang-toggle');
  Array.prototype.forEach.call(links, function (link) {
    link.addEventListener('click', function () {
      if (window.scrollY < 1) return;
      var blocks = document.querySelectorAll(BLOCKS);
      var top = header();
      for (var i = 0; i < blocks.length; i++) {
        var r = blocks[i].getBoundingClientRect();
        if (r.height && r.bottom > top) {
          try {
            sessionStorage.setItem(KEY, JSON.stringify({
              path: new URL(link.href, location.href).pathname, index: i, count: blocks.length,
              offset: Math.max(r.top - top, 0), into: r.top < top ? (top - r.top) / r.height : 0, at: Date.now()
            }));
          } catch (_) {}
          return;
        }
      }
    });
  });

  var saved = null;
  try {
    saved = JSON.parse(sessionStorage.getItem(KEY));
    sessionStorage.removeItem(KEY);
  } catch (_) {}
  // Only for the page the link led to, straight after it, and not when the address asks for a section.
  if (!saved || saved.path !== location.pathname || Date.now() - saved.at > 15000 || location.hash) return;

  function restore() {
    var blocks = document.querySelectorAll(BLOCKS);
    if (blocks.length !== saved.count) return;
    var r = blocks[saved.index].getBoundingClientRect();
    var y = r.top + window.scrollY - header() - saved.offset + saved.into * r.height;
    window.scrollTo({ top: Math.max(0, y), behavior: 'instant' });
  }
  restore();
  // Again as fonts and images come in and move the text, until the reader scrolls or presses a key themselves.
  var moved = false;
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (type) {
    window.addEventListener(type, function () { moved = true; }, { once: true, passive: true });
  });
  function again() { if (!moved) restore(); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(again);
  window.addEventListener('load', function () { again(); setTimeout(again, 300); });
})();
