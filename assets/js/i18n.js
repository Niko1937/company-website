(function () {
  'use strict';

  const SUPPORTED = ['en', 'ja'];
  const DEFAULT_LANG = 'en';
  const STORAGE_KEY = 'preferredLang';
  const PHRASE_SCOPE = 'h1, h2, h3, h4, [data-phrase]';
  const DEFAULT_COMPANY = 'Quests';
  // Locale files live in /locales/v<I18N_VERSION>/. When they start using something older copies of this
  // script cannot render, bump this number, move the files to the new folder, and set meta.requiresI18n to
  // the same number. Older folders (and /locales/*.json) stay frozen for pages still running a cached older
  // script, so those pages show older text instead of raw {placeholders} (see README).
  const I18N_VERSION = 2;
  const RELOAD_KEY = 'i18nReloadedFor';
  const PLACEHOLDER = /\{[A-Za-z]+\}/;

  function detectLangFromPath() {
    const path = window.location.pathname;
    const match = path.match(/^\/(en|ja)(\/|$)/);
    if (match) return match[1];
    return null;
  }

  function detectLangFromStorage() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored && SUPPORTED.includes(stored)) return stored;
    } catch (_) {}
    return null;
  }

  function detectLangFromBrowser() {
    const browserLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (browserLang.startsWith('ja')) return 'ja';
    return null;
  }

  function resolveInitialLang() {
    return (
      detectLangFromPath() ||
      detectLangFromStorage() ||
      detectLangFromBrowser() ||
      DEFAULT_LANG
    );
  }

  function getByPath(obj, path) {
    return path.split('.').reduce((acc, part) => {
      if (acc == null) return undefined;
      const arrayMatch = part.match(/^(.+)\[(\d+)\]$/);
      if (arrayMatch) {
        const key = arrayMatch[1];
        const idx = parseInt(arrayMatch[2], 10);
        return acc[key] != null ? acc[key][idx] : undefined;
      }
      return acc[part];
    }, obj);
  }

  function localesUrl(lang) {
    return `/locales/v${I18N_VERSION}/${lang}.json`;
  }

  async function fetchTranslations(lang) {
    const res = await fetch(localesUrl(lang), { cache: 'no-cache' });
    if (!res.ok) throw new Error(`Failed to load ${lang}.json: ${res.status}`);
    return fillCompanyName(await res.json());
  }

  // Replaces {company} in every translation string with the company name from site-config.js.
  function fillCompanyName(node) {
    const name = (window.siteConfig && window.siteConfig.get('companyName')) || DEFAULT_COMPANY;
    const fill = v => typeof v === 'string' ? v.split('{company}').join(name)
      : Array.isArray(v) ? v.map(fill)
      : v && typeof v === 'object' ? Object.fromEntries(Object.entries(v).map(([k, x]) => [k, fill(x)]))
      : v;
    return fill(node);
  }

  function applyTranslations(translations) {
    const lang = (translations.meta && translations.meta.htmlLang) || '';

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const value = getByPath(translations, key);
      if (isRenderable(value)) {
        el.textContent = value;
      }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const key = el.getAttribute('data-i18n-html');
      const value = getByPath(translations, key);
      if (isRenderable(value)) {
        el.innerHTML = value;
      }
    });

    document.querySelectorAll('[data-i18n-list]').forEach(el => {
      const key = el.getAttribute('data-i18n-list');
      const arr = getByPath(translations, key);
      if (Array.isArray(arr) && arr.every(isRenderable)) {
        const tag = el.getAttribute('data-i18n-list-tag') || 'li';
        el.innerHTML = arr.map(item => `<${tag}>${escapeHtml(item)}</${tag}>`).join('');
      }
    });

    document.querySelectorAll('*').forEach(el => {
      for (const attr of Array.from(el.attributes)) {
        if (attr.name.startsWith('data-i18n-attr-')) {
          const targetAttr = attr.name.replace('data-i18n-attr-', '');
          const value = getByPath(translations, attr.value);
          if (isRenderable(value) && el.getAttribute(targetAttr) !== value) {
            el.setAttribute(targetAttr, value);
          }
        }
      }
    });

    if (translations.meta) {
      if (translations.meta.htmlLang) {
        document.documentElement.lang = translations.meta.htmlLang;
      }
      if (isRenderable(translations.meta.title)) {
        document.title = translations.meta.title;
      }
    }

    if (lang === 'ja' && typeof customElements !== 'undefined' && customElements.get('budoux-ja')) {
      const wrapWithBudoux = (el) => {
        if (!el || !el.innerHTML) return;
        if (el.firstElementChild && el.firstElementChild.tagName === 'BUDOUX-JA') return;
        el.innerHTML = '<budoux-ja>' + el.innerHTML + '</budoux-ja>';
      };
      // Phrase-based line breaking suits headings and short leads; body text and lists
      // keep regular Japanese line breaking so their right edge stays even.
      document.querySelectorAll('[data-i18n], [data-i18n-html]').forEach(el => {
        if (el.closest(PHRASE_SCOPE)) wrapWithBudoux(el);
      });
    }
  }

  function isRenderable(value) {
    return typeof value === 'string' && !PLACEHOLDER.test(value);
  }

  // After a deploy, the browser may still hold a cached older copy of this script while the locale files are
  // already new. In that case reload once so the page picks up the matching HTML and scripts.
  function reloadForNewerScript(translations) {
    const required = (translations.meta && translations.meta.requiresI18n) || 0;
    if (required <= I18N_VERSION) return false;
    try {
      if (sessionStorage.getItem(RELOAD_KEY) === String(required)) return false;
      sessionStorage.setItem(RELOAD_KEY, String(required));
    } catch (_) {
      return false;
    }
    location.reload();
    return true;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function updateLanguageSwitcherUI(lang) {
    document.querySelectorAll('[data-lang-switch]').forEach(el => {
      const target = el.getAttribute('data-lang-switch');
      if (target === lang) {
        el.classList.add('lang-active');
      } else {
        el.classList.remove('lang-active');
      }
    });
  }

  function syncUrlPath(lang) {
    const path = window.location.pathname;
    const currentMatch = path.match(/^\/(en|ja)(\/.*)?$/);
    let newPath;
    if (currentMatch) {
      const rest = currentMatch[2] || '/';
      newPath = `/${lang}${rest}`;
    } else {
      newPath = `/${lang}/`;
    }
    if (newPath !== path) {
      window.history.replaceState({}, '', newPath + window.location.search + window.location.hash);
    }
  }

  async function setLanguage(lang, options = {}) {
    if (!SUPPORTED.includes(lang)) lang = DEFAULT_LANG;
    try {
      const translations = await fetchTranslations(lang);
      if (reloadForNewerScript(translations)) return;
      window.__translations = translations;
      window.__currentLang = lang;
      applyTranslations(translations);
      updateLanguageSwitcherUI(lang);
      try { localStorage.setItem(STORAGE_KEY, lang); } catch (_) {}
      if (options.updateUrl !== false) {
        syncUrlPath(lang);
      }
      document.dispatchEvent(new CustomEvent('i18n:changed', { detail: { lang, translations } }));
    } catch (err) {
      console.error('[i18n] Failed to set language:', err);
    }
  }

  function t(key) {
    const translations = window.__translations;
    if (!translations) return '';
    const value = getByPath(translations, key);
    return isRenderable(value) ? value : '';
  }

  function init() {
    const lang = resolveInitialLang();
    setLanguage(lang, { updateUrl: !detectLangFromPath() });

    document.addEventListener('click', e => {
      const toggle = e.target.closest('[data-lang-toggle]');
      if (toggle) {
        e.preventDefault();
        const current = window.__currentLang || DEFAULT_LANG;
        const idx = SUPPORTED.indexOf(current);
        const next = SUPPORTED[(idx + 1) % SUPPORTED.length];
        setLanguage(next);
        return;
      }
      const trigger = e.target.closest('[data-lang-switch]');
      if (!trigger) return;
      e.preventDefault();
      const target = trigger.getAttribute('data-lang-switch');
      setLanguage(target);
    });
  }

  window.i18n = { setLanguage, t, getByPath };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
