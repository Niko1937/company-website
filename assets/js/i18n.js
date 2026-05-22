(function () {
  'use strict';

  const SUPPORTED = ['en', 'ja'];
  const DEFAULT_LANG = 'en';
  const STORAGE_KEY = 'preferredLang';

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
    return `/locales/${lang}.json`;
  }

  async function fetchTranslations(lang) {
    const res = await fetch(localesUrl(lang), { cache: 'no-cache' });
    if (!res.ok) throw new Error(`Failed to load ${lang}.json: ${res.status}`);
    return res.json();
  }

  function applyTranslations(translations) {
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const value = getByPath(translations, key);
      if (typeof value === 'string') {
        el.textContent = value;
      }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const key = el.getAttribute('data-i18n-html');
      const value = getByPath(translations, key);
      if (typeof value === 'string') {
        el.innerHTML = value;
      }
    });

    document.querySelectorAll('[data-i18n-list]').forEach(el => {
      const key = el.getAttribute('data-i18n-list');
      const arr = getByPath(translations, key);
      if (Array.isArray(arr)) {
        const tag = el.getAttribute('data-i18n-list-tag') || 'li';
        el.innerHTML = arr.map(item => `<${tag}>${escapeHtml(item)}</${tag}>`).join('');
      }
    });

    document.querySelectorAll('*').forEach(el => {
      for (const attr of Array.from(el.attributes)) {
        if (attr.name.startsWith('data-i18n-attr-')) {
          const targetAttr = attr.name.replace('data-i18n-attr-', '');
          const value = getByPath(translations, attr.value);
          if (typeof value === 'string') {
            el.setAttribute(targetAttr, value);
          }
        }
      }
    });

    if (translations.meta) {
      if (translations.meta.htmlLang) {
        document.documentElement.lang = translations.meta.htmlLang;
      }
      if (translations.meta.title) {
        document.title = translations.meta.title;
      }
    }
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
    return typeof value === 'string' ? value : '';
  }

  function init() {
    const lang = resolveInitialLang();
    setLanguage(lang, { updateUrl: !detectLangFromPath() });

    document.addEventListener('click', e => {
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
