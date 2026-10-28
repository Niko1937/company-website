(function () {
  'use strict';

  // Renders the Solutions demo videos listed in SITE_CONFIG.solutions. Load synchronously in <head>
  // (after config.js) so empty layers, or the whole section and its menu items, are hidden before the body renders.
  //   [data-solutions]                 : the section and its menu items (hidden when no demo is shown)
  //   [data-solutions-layer="<cat>"]   : one layer per category (hidden when it has no demo; when only one is
  //                                      left, its heading is hidden as well)
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
    // With one layer left there is nothing to divide it from, and its heading ("For Business") would only suggest
    // that another kind exists, so the layer and dialog headings are hidden too.
    style.textContent = `${selectors.join(',')}{display:none!important}.solutions-layer{padding-top:0!important;border-top:0!important}`
      + (items.length ? '.solutions-layer-head,.solution-dialog-tag{display:none!important}' : '');
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

    const thumb = el('div', 'solution-thumb');
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
    // Its click area covers the whole card (CSS), so this is the card's only control.
    const button = el('button', 'solution-watch', { type: 'button', 'data-solution-open': item.id, 'aria-label': `${watch}: ${title}` });
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
    // Decide from the cards' own widths, not from the overflow: centering makes the track narrower, so measuring
    // the overflow would flip between the two layouts.
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    const needed = Array.from(track.children).reduce((sum, card) => sum + card.offsetWidth, 0) + gap * Math.max(track.children.length - 1, 0);
    track.classList.toggle('is-centered', needed <= layer.clientWidth);
    const max = track.scrollWidth - track.clientWidth;
    arrows.hidden = track.classList.contains('is-centered') || max <= 1;
    arrows.querySelector('[data-solutions-prev]').disabled = track.scrollLeft <= 1;
    arrows.querySelector('[data-solutions-next]').disabled = track.scrollLeft >= max - 1;
    arrows.querySelector('[data-solutions-count]').textContent = visibleRange(track);
  }

  // "1–3 / 6": the cards that are (mostly) in view. A card peeking in at the edge does not count.
  function visibleRange(track) {
    const cards = Array.from(track.children);
    const view = track.getBoundingClientRect();
    const shown = [];
    cards.forEach((card, i) => {
      const r = card.getBoundingClientRect();
      const visible = Math.min(r.right, view.right) - Math.max(r.left, view.left);
      if (r.width && visible / r.width >= 0.75) shown.push(i + 1);
    });
    if (!shown.length) return '';
    const first = shown[0], last = shown[shown.length - 1];
    return `${first === last ? first : `${first}–${last}`} / ${cards.length}`;
  }

  function scrollTrack(track, direction) {
    const first = track.firstElementChild;
    if (!first) return;
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    track.scrollBy({ left: direction * (first.offsetWidth + gap), behavior: reduceMotion() ? 'auto' : 'smooth' });
  }

  function setUpTracks() {
    const resize = new ResizeObserver(entries => entries.forEach(e => updateArrows(e.target.matches('[data-solutions-track]') ? e.target : e.target.querySelector('[data-solutions-track]'))));
    document.querySelectorAll('[data-solutions-track]').forEach(track => {
      let ticking = false;
      track.addEventListener('scroll', () => {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => { updateArrows(track); ticking = false; });
      }, { passive: true });
      resize.observe(track);
      const layer = track.closest('[data-solutions-layer]');
      resize.observe(layer);
      layer.querySelector('[data-solutions-prev]').addEventListener('click', () => scrollTrack(track, -1));
      layer.querySelector('[data-solutions-next]').addEventListener('click', () => scrollTrack(track, 1));
    });
  }

  // ---- Player -------------------------------------------------------------------------------------------------

  // One shared <dialog>, built on first use. Same layout as the Case Studies dialog: content on the left of the
  // footer, "2 / 6" and the arrows on the right. The close button sits above the video so it never covers
  // YouTube's own controls.
  let player = null;
  let current = null;

  function buildPlayer() {
    const dialog = el('dialog', 'solution-dialog', { 'aria-labelledby': 'solution-dialog-title' });
    const head = el('div', 'solution-dialog-head');
    const tag = el('p', 'solution-dialog-tag');
    const title = el('h3', 'solution-dialog-title', { id: 'solution-dialog-title' });
    head.append(tag, title);
    const frame = el('div', 'solution-dialog-frame');
    const foot = el('div', 'solution-dialog-foot');
    const desc = el('p', 'solution-dialog-desc');
    const pager = el('div', 'pager pager-dark');
    const count = el('span', 'pager-count');
    const steps = [-1, 1].map(dir => {
      const button = el('button', 'pager-arrow', { type: 'button', 'data-solution-step': dir });
      button.appendChild(el('i', dir < 0 ? 'ri-arrow-left-line' : 'ri-arrow-right-line', { 'aria-hidden': 'true' }));
      button.addEventListener('click', () => step(dir));
      return button;
    });
    pager.append(count, ...steps);
    foot.append(desc, pager);
    const close = el('button', 'dialog-close', { type: 'button' });
    close.appendChild(el('i', 'ri-close-line', { 'aria-hidden': 'true' }));
    close.addEventListener('click', () => dialog.close());
    dialog.append(head, frame, foot, close);

    // A click outside the panel lands on the backdrop, which belongs to the <dialog> itself.
    dialog.addEventListener('click', e => {
      if (e.target !== dialog) return;
      const r = dialog.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close();
    });
    // Arrow keys page through the demos. Once the video has focus, YouTube uses them to seek instead.
    dialog.addEventListener('keydown', e => {
      if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        e.preventDefault();
        step(e.key === 'ArrowLeft' ? -1 : 1);
      }
    });
    dialog.addEventListener('close', onClose);
    document.body.appendChild(dialog);
    return { dialog, tag, title, frame, desc, count, steps, close };
  }

  function sameLayer(item) {
    return items.filter(i => i.category === item.category);
  }

  // Header, description, "2 / 6" and arrow labels for the current demo, in the current language.
  function fillPlayer() {
    const lang = currentLang();
    const list = sameLayer(current);
    const index = list.indexOf(current);
    player.tag.textContent = tr(`solutions.${current.category}`, current.category === 'business' ? 'For Business' : 'For Consumers');
    player.title.textContent = current.title[lang];
    player.desc.textContent = current.description[lang];
    player.count.textContent = `${index + 1} / ${list.length}`;
    player.close.setAttribute('aria-label', tr('solutions.close', 'Close'));
    player.steps.forEach(button => {
      const dir = Number(button.getAttribute('data-solution-step'));
      const target = list[index + dir];
      const label = dir < 0 ? tr('solutions.prevDemo', 'Previous demo') : tr('solutions.nextDemo', 'Next demo');
      const text = target ? label + (lang === 'ja' ? '：' : ': ') + target.title[lang] : label;
      button.disabled = !target;
      button.setAttribute('aria-label', text);
      button.title = text;
    });
  }

  // Loads a demo into the player. A new iframe replaces the old one, which stops its playback.
  function show(item) {
    current = item;
    const lang = currentLang();
    const frame = el('iframe', '', {
      title: item.title[lang],
      // clipboard-write and web-share let the player's own Share / Copy link buttons work (as in YouTube's embed code).
      allow: 'autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share; fullscreen',
      allowfullscreen: '',
      referrerpolicy: 'strict-origin-when-cross-origin'
    });
    frame.src = `https://www.youtube-nocookie.com/embed/${item.video[lang]}?autoplay=1&rel=0&playsinline=1`;
    player.frame.replaceChildren(frame);
    fillPlayer();
    setHash(`#solutions-${item.id}`);
  }

  function step(dir) {
    const list = sameLayer(current);
    const next = list[list.indexOf(current) + dir];
    if (!next) return;
    show(next);
    // An arrow that just became disabled loses focus: keep it on the pager.
    if (document.activeElement && document.activeElement.disabled) {
      (player.steps.find(b => !b.disabled) || player.close).focus();
    }
  }

  // Opens the player for one demo. Returns false when no shown demo has that id.
  function open(id) {
    const item = items.find(i => i.id === id);
    if (!item) return false;
    player = player || buildPlayer();
    show(item);
    if (!player.dialog.open) {
      player.dialog.showModal();
      document.documentElement.classList.add('solutions-open');
      player.close.focus();
    }
    return true;
  }

  // Stops playback, and brings the card of the last demo watched into view and focus.
  function onClose() {
    document.documentElement.classList.remove('solutions-open');
    player.frame.replaceChildren();
    setHash('#solutions');
    const button = current && document.querySelector(`.solution-watch[data-solution-open="${current.id}"]`);
    current = null;
    if (!button) return;
    const card = button.closest('.solution-card');
    const track = card.parentElement;
    const view = track.getBoundingClientRect(), r = card.getBoundingClientRect();
    if (r.left < view.left || r.right > view.right) track.scrollLeft += r.left - view.left;
    button.focus({ preventScroll: true });
  }

  // ---- Start --------------------------------------------------------------------------------------------------

  window.solutions = { open };
  if (!items.length) return;

  document.addEventListener('DOMContentLoaded', () => {
    setUpTracks();
    render();
    document.addEventListener('click', e => {
      const trigger = e.target.closest('[data-solution-open]');
      if (trigger) open(trigger.getAttribute('data-solution-open'));
    });
  });
  document.addEventListener('i18n:changed', () => {
    render();
    if (current) fillPlayer();
  });
})();
