// The contact form at the end of an app's support page (#contact; built by scripts/app_pages/build.py).
// It works like the company's form on the home page: nothing is sent from the page. The answers are checked,
// then the visitor picks a mail service and its compose window opens with them filled in.
// ?app= and ?os= (added by the app's Contact button) fill in the app version and the phone.
(function () {
  var form = document.getElementById('appContactForm');
  if (!form) return;
  var t = JSON.parse(form.getAttribute('data-strings'));
  var lang = form.getAttribute('data-lang');
  var TO = 'contact@quests.it.com';
  var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var $ = function (id) { return document.getElementById(id); };

  // Filled in from the app's link, so people need not look them up.
  var params = new URLSearchParams(window.location.search);
  if (params.get('app')) $('cf-app').value = params.get('app').slice(0, 20);
  if (params.get('os')) $('cf-device').value = params.get('os').slice(0, 60);

  // Required fields: the error appears under the field once it has been left or the form sent, and goes
  // as soon as the answer is fixed.
  var rules = {
    'cf-name': function (v) { return v ? '' : 'name'; },
    'cf-email': function (v) { return !v ? 'email' : (EMAIL.test(v) ? '' : 'emailFormat'); },
    'cf-topic': function (v) { return v ? '' : 'topic'; },
    'cf-message': function (v) { return v ? '' : 'message'; }
  };
  function check(id) {
    var input = $(id);
    var error = $(id + '-error');
    var key = rules[id](input.value.trim());
    if (key) input.setAttribute('aria-invalid', 'true');
    else input.removeAttribute('aria-invalid');
    error.hidden = !key;
    error.textContent = key ? t.errors[key] : '';
    return !key;
  }
  Object.keys(rules).forEach(function (id) {
    var input = $(id);
    var again = function () { if (input.hasAttribute('aria-invalid')) check(id); };
    input.addEventListener('blur', function () { if (input.value.trim() || input.hasAttribute('aria-invalid')) check(id); });
    input.addEventListener('input', again);
    input.addEventListener('change', again);
  });

  function openMailerPicker(subject, body) {
    var enc = encodeURIComponent;
    var urls = {
      default: 'mailto:' + TO + '?subject=' + enc(subject) + '&body=' + enc(body),
      gmail: 'https://mail.google.com/mail/?view=cm&fs=1&to=' + enc(TO) + '&su=' + enc(subject) + '&body=' + enc(body),
      outlook: 'https://outlook.live.com/mail/0/deeplink/compose?to=' + enc(TO) + '&subject=' + enc(subject) + '&body=' + enc(body)
    };
    var opener = document.activeElement;
    var overlay = document.createElement('div');
    overlay.className = 'mailer';
    overlay.innerHTML =
      '<div class="mailer-backdrop" data-close></div>' +
      '<div class="mailer-panel" role="dialog" aria-modal="true" aria-labelledby="mailer-title">' +
      '<button type="button" class="mailer-close" data-close><i class="ri-close-line" aria-hidden="true"></i></button>' +
      '<h3 id="mailer-title"></h3><p class="mailer-lead"></p>' +
      '<div class="mailer-options">' +
      '<button type="button" data-mailer="default"><i class="ri-mail-send-line" aria-hidden="true"></i><span></span></button>' +
      '<button type="button" data-mailer="gmail"><i class="ri-google-fill" aria-hidden="true"></i><span>Gmail</span></button>' +
      '<button type="button" data-mailer="outlook"><i class="ri-microsoft-fill" aria-hidden="true"></i><span></span></button>' +
      '</div></div>';
    // Text is set as text, never as HTML.
    overlay.querySelector('#mailer-title').textContent = t.mailerTitle;
    overlay.querySelector('.mailer-lead').textContent = t.mailerDescription;
    overlay.querySelector('.mailer-close').setAttribute('aria-label', t.close);
    overlay.querySelector('[data-mailer="default"] span').textContent = t.mailerDefault;
    overlay.querySelector('[data-mailer="outlook"] span').textContent = t.mailerOutlookWeb;
    document.body.appendChild(overlay);
    var close = function () {
      document.removeEventListener('keydown', onKey);
      overlay.remove();
      if (opener && opener.focus) opener.focus();
    };
    var onKey = function (ev) { if (ev.key === 'Escape') close(); };
    document.addEventListener('keydown', onKey);
    overlay.querySelectorAll('[data-close]').forEach(function (el) { el.addEventListener('click', close); });
    overlay.querySelectorAll('[data-mailer]').forEach(function (button) {
      button.addEventListener('click', function () {
        var url = urls[this.getAttribute('data-mailer')];
        // Web mail opens in a new tab; mailto: hands over to the visitor's own mail app.
        if (/^https?:/.test(url)) window.open(url, '_blank', 'noopener');
        else window.location.href = url;
        close();
      });
    });
    overlay.querySelector('[data-mailer="default"]').focus();
  }

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var invalid = Object.keys(rules).filter(function (id) { return !check(id); });
    if (invalid.length) { $(invalid[0]).focus(); return; }
    var topic = $('cf-topic');
    var topicText = topic.options[topic.selectedIndex].text.trim();
    var line = function (label, value) { return lang === 'ja' ? '【' + label + '】' + value : label + ': ' + value; };
    var lines = [
      line(t.name, $('cf-name').value.trim()),
      line(t.email, $('cf-email').value.trim()),
      line(t.topic, topicText)
    ];
    if ($('cf-device').value.trim()) lines.push(line(t.device, $('cf-device').value.trim()));
    if ($('cf-app').value.trim()) lines.push(line(t.appVersion, $('cf-app').value.trim()));
    lines.push('', lang === 'ja' ? '【' + t.message + '】' : t.message + ':', $('cf-message').value.trim());
    openMailerPicker(t.mailSubject + (lang === 'ja' ? '：' : ': ') + topicText, lines.join('\n'));
  });
})();
