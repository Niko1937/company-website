// The app pages' screens to page through (built by scripts/app_pages/build.py): a sideways scroll that stops at each
// screen. The arrows and dots move it and follow it; a swipe or the arrow keys work too. Without this script the
// screens still scroll sideways.
(function () {
  document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
    var track = carousel.querySelector('.carousel-track');
    var slides = track.children;
    var dots = carousel.querySelectorAll('.carousel-dot');
    var prev = carousel.querySelector('.carousel-prev');
    var next = carousel.querySelector('.carousel-next');
    var current = 0;

    function go(i) {
      i = Math.max(0, Math.min(slides.length - 1, i));
      show(i);
      track.scrollTo({ left: i * track.clientWidth });
    }
    function show(i) {
      current = i;
      dots.forEach(function (dot, n) {
        if (n === i) dot.setAttribute('aria-current', 'true');
        else dot.removeAttribute('aria-current');
      });
      prev.disabled = i === 0;
      next.disabled = i === slides.length - 1;
    }

    prev.addEventListener('click', function () { go(current - 1); });
    next.addEventListener('click', function () { go(current + 1); });
    dots.forEach(function (dot, n) { dot.addEventListener('click', function () { go(n); }); });
    track.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowRight') { ev.preventDefault(); go(current + 1); }
      if (ev.key === 'ArrowLeft') { ev.preventDefault(); go(current - 1); }
    });
    // A swipe moves it too: the screen nearest the middle is the current one.
    var pending = false;
    track.addEventListener('scroll', function () {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () {
        pending = false;
        show(Math.round(track.scrollLeft / track.clientWidth));
      });
    });
  });
})();
