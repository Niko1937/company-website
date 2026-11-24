// The app pages' menu on phones (built by scripts/app_pages/build.py), as on the Quests site: the button opens the
// sections, the support page and Download; Esc, a tap outside or choosing a link closes it.
(function () {
  var button = document.getElementById('appMenuBtn');
  var menu = document.getElementById('appMenu');
  if (!button || !menu) return;
  var header = button.closest('header');
  function setOpen(open) {
    menu.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', button.getAttribute(open ? 'data-close-label' : 'data-open-label'));
    button.querySelector('i').className = open ? 'ri-close-line' : 'ri-menu-line';
  }
  button.addEventListener('click', function () { setOpen(menu.hidden); });
  menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setOpen(false); button.focus(); } });
  document.addEventListener('click', function (e) { if (!menu.hidden && !header.contains(e.target)) setOpen(false); });
  // Wide again (the full menu shows in the bar): close it.
  window.matchMedia('(min-width: 900px)').addEventListener('change', function (e) { if (e.matches) setOpen(false); });
})();
