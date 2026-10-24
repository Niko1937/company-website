(function () {
  'use strict';

  // Renders the Solutions demo videos listed in SITE_CONFIG.solutions. Load synchronously in <head>
  // (after config.js) so empty layers, or the whole section and its menu items, are hidden before the body renders.
  //   [data-solutions]                 : the section and its menu items (hidden when no demo is shown)
  //   [data-solutions-layer="<cat>"]   : one layer per category (hidden when it has no demo)
  //   [data-solutions-track="<cat>"]   : where the cards of that category are rendered
  const CATEGORIES = ['business', 'consumer'];
  const LANGS = ['en', 'ja'];
  const ID = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  const YOUTUBE_ID = /^[A-Za-z0-9_-]{11}$/;
  const PREVIEW = /^\/videos\/(?:[\w-]+\/)*[\w-]+\.(?:mp4|webm)$/;

  const items = readItems((window.SITE_CONFIG || {}).solutions);
  hideEmpty();

  // ---- Config -------------------------------------------------------------------------------------------------

  function readItems(list) {
    if (list == null) return [];
    if (!Array.isArray(list)) {
      console.warn('[solutions] SITE_CONFIG.solutions must be an array.');
      return [];
    }
    const seen = new Set();
    return list.map((item, index) => {
      const solution = readItem(item, index);
      if (solution && seen.has(solution.id)) {
        console.warn(`[solutions] Skipped solutions[${index}]: id "${solution.id}" is used twice.`);
        return null;
      }
      if (solution) seen.add(solution.id);
      return solution;
    }).filter(Boolean);
  }

  // Returns a clean copy of one entry, or null when it is hidden or invalid (invalid entries are reported).
  function readItem(item, index) {
    if (!item || typeof item !== 'object' || item.show !== true) return null;
    const problems = [];
    if (!ID.test(item.id || '')) problems.push('id');
    if (!CATEGORIES.includes(item.category)) problems.push('category');

    const video = readLocalized(item.video, v => YOUTUBE_ID.test(v), 'video', problems);
    if (!video.en && !problems.some(p => p.startsWith('video'))) problems.push('video');
    const title = readLocalized(item.title, Boolean, 'title', problems);
    if (!title.en) problems.push('title');
    const description = readLocalized(item.description, Boolean, 'description', problems);

    let preview = '';
    if (item.preview != null && item.preview !== '') {
      if (typeof item.preview === 'string' && PREVIEW.test(item.preview)) preview = item.preview;
      else problems.push('preview');
    }

    if (problems.length) {
      console.warn(`[solutions] Skipped solutions[${index}]: check ${[...new Set(problems)].join(', ')}.`);
      return null;
    }
    return { id: item.id, category: item.category, video, title, description, preview };
  }

  // Reads an { en, ja } value (a plain string means the same value for both languages).
  // A language left empty falls back to the other language.
  function readLocalized(value, isValid, name, problems) {
    const out = {};
    if (typeof value === 'string') value = { en: value, ja: value };
    if (value != null && typeof value !== 'object') problems.push(name);
    LANGS.forEach(lang => {
      const raw = value && typeof value === 'object' ? value[lang] : undefined;
      const text = typeof raw === 'string' ? raw.trim() : '';
      if (raw != null && raw !== '' && !(text && isValid(text))) problems.push(`${name}.${lang}`);
      out[lang] = text && isValid(text) ? text : '';
    });
    out.en = out.en || out.ja;
    out.ja = out.ja || out.en;
    return out;
  }

  function hideEmpty() {
    const selectors = items.length
      ? CATEGORIES.filter(cat => !items.some(i => i.category === cat)).map(cat => `[data-solutions-layer="${cat}"]`)
      : ['[data-solutions]'];
    if (!selectors.length) return;
    const style = document.createElement('style');
    style.textContent = `${selectors.join(',')}{display:none!important}`;
    document.head.appendChild(style);
  }

  // ---- Helpers ------------------------------------------------------------------------------------------------

  function currentLang() {
    if (LANGS.includes(window.__currentLang)) return window.__currentLang;
    const match = location.pathname.match(/^\/(en|ja)(\/|$)/);
    return match ? match[1] : 'en';
  }

  function tr(key, fallback) {
    return (window.i18n && window.i18n.t(key)) || fallback;
  }

  function el(tag, className, attrs) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    Object.entries(attrs || {}).forEach(([k, v]) => node.setAttribute(k, v));
    return node;
  }

  function setHash(hash) {
    history.replaceState(history.state, '', location.pathname + location.search + hash);
  }

  function reduceMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  // ---- Cards --------------------------------------------------------------------------------------------------

  function render() {
    const lang = currentLang();
    CATEGORIES.forEach(cat => {
      const track = document.querySelector(`[data-solutions-track="${cat}"]`);
      if (!track) return;
      track.replaceChildren(...items.filter(i => i.category === cat).map(i => card(i, lang)));
      track.scrollLeft = 0;
      updateArrows(track);
    });
  }

  function card(item, lang) {
    const title = item.title[lang];
    const watch = tr('solutions.watchDemo', 'Watch demo');
    const article = el('article', 'solution-card');

    const thumb = el('button', 'solution-thumb', { type: 'button', 'data-solution-open': item.id, 'aria-label': `${watch}: ${title}` });
    thumb.appendChild(thumbnail(item.video[lang]));
    if (item.preview) thumb.appendChild(previewVideo(item.preview));
    const play = el('span', 'solution-play', { 'aria-hidden': 'true' });
    play.appendChild(el('i', 'ri-play-fill'));
    thumb.appendChild(play);
    article.appendChild(thumb);

    const body = el('div', 'solution-body');
    const heading = el('h4', 'solution-title');
    heading.textContent = title;
    body.appendChild(heading);
    if (item.description[lang]) {
      const desc = el('p', 'solution-desc');
      desc.textContent = item.description[lang];
      body.appendChild(desc);
    }
    const button = el('button', 'solution-watch', { type: 'button', 'data-solution-open': item.id });
    button.appendChild(el('i', 'ri-play-circle-line', { 'aria-hidden': 'true' }));
    const label = el('span');
    label.textContent = watch;
    button.appendChild(label);
    body.appendChild(button);
    article.appendChild(body);
    return article;
  }

  // YouTube always has hqdefault (480x360). maxresdefault is sharper but missing for some videos, in which case
  // YouTube answers with a 120x90 placeholder, so switch only when a real image arrives.
  function thumbnail(videoId) {
    const img = el('img', 'solution-image', { alt: '', loading: 'lazy', decoding: 'async' });
    img.src = `https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`;
    const hd = new Image();
    hd.onload = () => { if (hd.naturalWidth > 120) img.src = hd.src; };
    hd.src = `https://i.ytimg.com/vi/${videoId}/maxresdefault.jpg`;
    return img;
  }

  function previewVideo(src) {
    const video = el('video', 'solution-preview', { muted: '', loop: '', playsinline: '', preload: 'none', 'aria-hidden': 'true' });
    video.muted = true;
    video.src = src;
    video.addEventListener('playing', () => video.classList.add('is-playing'));
    previewObserver().observe(video);
    return video;
  }

  // Plays a preview only while it is on screen, and never when the visitor prefers reduced motion.
  let observer;
  function previewObserver() {
    observer = observer || new IntersectionObserver(entries => {
      entries.forEach(({ target, isIntersecting }) => {
        if (isIntersecting && !reduceMotion()) target.play().catch(() => {});
        else target.pause();
      });
    }, { threshold: 0.5 });
    return observer;
  }

  // ---- Arrows -------------------------------------------------------------------------------------------------

  function updateArrows(track) {
    const layer = track.closest('[data-solutions-layer]');
    const arrows = layer && layer.querySelector('[data-solutions-arrows]');
    if (!arrows) return;
    const max = track.scrollWidth - track.clientWidth;
    arrows.hidden = max <= 1;
    arrows.querySelector('[data-solutions-prev]').disabled = track.scrollLeft <= 1;
    arrows.querySelector('[data-solutions-next]').disabled = track.scrollLeft >= max - 1;
  }

  function scrollTrack(track, direction) {
    const first = track.firstElementChild;
    if (!first) return;
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    track.scrollBy({ left: direction * (first.offsetWidth + gap), behavior: reduceMotion() ? 'auto' : 'smooth' });
  }

  function setUpTracks() {
    const resize = new ResizeObserver(entries => entries.forEach(e => updateArrows(e.target)));
    document.querySelectorAll('[data-solutions-track]').forEach(track => {
      let ticking = false;
      track.addEventListener('scroll', () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => { updateArrows(track); ticking = false; });
      }, { passive: true });
      resize.observe(track);
      const layer = track.closest('[data-solutions-layer]');
      layer.querySelector('[data-solutions-prev]').addEventListener('click', () => scrollTrack(track, -1));
      layer.querySelector('[data-solutions-next]').addEventListener('click', () => scrollTrack(track, 1));
    });
  }

  // ---- Player -------------------------------------------------------------------------------------------------

  let dialog = null;

  // Opens the player for one demo. Returns false when no shown demo has that id.
  function open(id, opener) {
    const item = items.find(i => i.id === id);
    if (!item) return false;
    close({ keepHash: true });
    const lang = currentLang();

    const overlay = el('div', 'fixed inset-0 z-[60] flex items-center justify-center p-4 sm:p-8', {
      role: 'dialog', 'aria-modal': 'true', 'aria-label': item.title[lang]
    });
    overlay.appendChild(el('div', 'absolute inset-0 bg-black/85', { 'data-close': '' }));
    const panel = el('div', 'relative w-full max-w-5xl');
    const closeButton = el('button', 'absolute -top-11 right-0 w-10 h-10 flex items-center justify-center text-white/80 hover:text-white transition-colors', {
      type: 'button', 'data-close': '', 'aria-label': tr('solutions.close', 'Close')
    });
    closeButton.appendChild(el('i', 'ri-close-line ri-2x', { 'aria-hidden': 'true' }));
    const frameBox = el('div', 'relative w-full aspect-video bg-black rounded-lg overflow-hidden shadow-2xl');
    const frame = el('iframe', 'absolute inset-0 w-full h-full', {
      title: item.title[lang],
      allow: 'autoplay; encrypted-media; picture-in-picture; fullscreen',
      allowfullscreen: '',
      referrerpolicy: 'strict-origin-when-cross-origin'
    });
    frame.src = `https://www.youtube-nocookie.com/embed/${item.video[lang]}?autoplay=1&rel=0&playsinline=1`;
    frameBox.appendChild(frame);
    const caption = el('p', 'mt-4 text-white text-lg font-semibold');
    caption.textContent = item.title[lang];
    panel.append(closeButton, frameBox, caption);
    overlay.appendChild(panel);

    const onKey = e => { if (e.key === 'Escape') close(); };
    overlay.querySelectorAll('[data-close]').forEach(n => n.addEventListener('click', () => close()));
    document.addEventListener('keydown', onKey);
    document.body.appendChild(overlay);
    document.documentElement.classList.add('solutions-open');
    dialog = { overlay, onKey, opener };
    setHash(`#solutions-${item.id}`);
    closeButton.focus();
    return true;
  }

  // Closes the player. Removing the iframe stops playback.
  function close(options) {
    if (!dialog) return;
    const { overlay, onKey, opener } = dialog;
    dialog = null;
    document.removeEventListener('keydown', onKey);
    overlay.remove();
    document.documentElement.classList.remove('solutions-open');
    if (options && options.keepHash) return;
    setHash('#solutions');
    if (opener && opener.isConnected) opener.focus();
  }

  // ---- Start --------------------------------------------------------------------------------------------------

  window.solutions = { open };
  if (!items.length) return;

  document.addEventListener('DOMContentLoaded', () => {
    setUpTracks();
    render();
    document.addEventListener('click', e => {
      const trigger = e.target.closest('[data-solution-open]');
      if (trigger) open(trigger.getAttribute('data-solution-open'), trigger);
    });
  });
  document.addEventListener('i18n:changed', render);
})();
