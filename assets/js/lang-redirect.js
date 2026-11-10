// Language-neutral URLs (/apps/pickle-up/ and the like) open the same page in the reader's language, as the root
// URL does (index.html): the language chosen before on this site (localStorage "preferredLang"), else the
// browser's, else English. The page itself has a meta refresh to English and plain links for when this cannot run.
(function () {
  var supported = ['en', 'ja'];
  var target = 'en';
  try {
    var stored = localStorage.getItem('preferredLang');
    if (stored && supported.indexOf(stored) !== -1) target = stored;
    else if ((navigator.language || navigator.userLanguage || '').toLowerCase().indexOf('ja') === 0) target = 'ja';
  } catch (_) {}
  location.replace('/' + target + location.pathname + location.search + location.hash);
})();
