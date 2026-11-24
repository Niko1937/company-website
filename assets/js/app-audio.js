// Sound samples on the app pages (built by scripts/app_pages/build.py): a button with data-audio plays the
// file from the start, or stops it if it is playing. Only one plays at a time.
(function () {
  var buttons = document.querySelectorAll('[data-audio]');
  if (!buttons.length) return;
  var current = null;
  function stop() {
    if (!current) return;
    current.audio.pause();
    current.button.classList.remove('is-playing');
    current.button.setAttribute('aria-pressed', 'false');
    current = null;
  }
  buttons.forEach(function (button) {
    button.setAttribute('aria-pressed', 'false');
    var audio = new Audio(button.getAttribute('data-audio'));
    audio.preload = 'none';
    audio.addEventListener('ended', stop);
    button.addEventListener('click', function () {
      var mine = current && current.button === button;
      stop();
      if (mine) return;
      audio.currentTime = 0;
      current = { audio: audio, button: button };
      button.classList.add('is-playing');
      button.setAttribute('aria-pressed', 'true');
      audio.play().catch(stop);
    });
  });
})();
