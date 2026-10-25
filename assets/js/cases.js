(function () {
  'use strict';

  // Case Studies: the filter switch and the details dialog.
  //   .case-study[data-case="<id>"] : one card. Its .case-details is moved into the dialog while it is open,
  //                                   so translations keep working on it.
  //   [data-case-dialog]            : the shared <dialog>. #cases-<id> opens it (section-links.js).
  const grid = document.querySelector('.case-grid');
  const dialog = document.querySelector('[data-case-dialog]');
  if (!grid || !dialog) return;

  const cards = Array.from(grid.querySelectorAll('.case-study[data-case]'));
  const filters = document.querySelector('.case-filters');
  const buttons = Array.from(filters.querySelectorAll('.case-filter-btn'));
  const indicator = filters.querySelector('.case-filter-indicator');

  function categoriesOf(card) {
    return card.getAttribute('data-category').split(/\s+/);
  }

  function setHash(hash) {
    history.replaceState(history.state, '', location.pathname + location.search + hash);
  }

  // ---- Filter -------------------------------------------------------------------------------------------------

  function countCases() {
    buttons.forEach(button => {
      const filter = button.getAttribute('data-filter');
      const count = filter === 'all' ? cards.length : cards.filter(c => categoriesOf(c).includes(filter)).length;
      button.querySelector('.case-filter-count').textContent = count;
    });
  }

  // Moves the white marker under the selected button.
  function placeIndicator() {
    const active = buttons.find(b => b.getAttribute('aria-pressed') === 'true');
    indicator.style.width = active.offsetWidth + 'px';
    indicator.style.height = active.offsetHeight + 'px';
    indicator.style.transform = `translate(${active.offsetLeft}px, ${active.offsetTop}px)`;
  }

  function applyFilter(button) {
    buttons.forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    placeIndicator();
    const filter = button.getAttribute('data-filter');
    cards.forEach(card => {
      const show = filter === 'all' || categoriesOf(card).includes(filter);
      const wasHidden = card.hidden;
      card.hidden = !show;
      card.classList.toggle('is-entering', show && wasHidden);
    });
  }

  buttons.forEach(button => button.addEventListener('click', () => applyFilter(button)));
  cards.forEach(card => card.addEventListener('animationend', () => card.classList.remove('is-entering')));
  // Labels change width when fonts load or the language switches, and the buttons wrap on narrow screens.
  const resize = new ResizeObserver(placeIndicator);
  buttons.forEach(b => resize.observe(b));
  resize.observe(filters);

  // ---- Dialog -------------------------------------------------------------------------------------------------

  const media = dialog.querySelector('[data-case-dialog-media]');
  const tag = dialog.querySelector('[data-case-dialog-tag]');
  const title = dialog.querySelector('[data-case-dialog-title]');
  const body = dialog.querySelector('[data-case-dialog-body]');
  const steps = Array.from(dialog.querySelectorAll('[data-case-step]'));
  const count = dialog.querySelector('[data-case-count]');
  let current = null;
  let opener = null;

  function visibleCards() {
    return cards.filter(c => !c.hidden);
  }

  function tr(key, fallback) {
    return (window.i18n && window.i18n.t(key)) || fallback;
  }

  // "2 / 6" within the current filter, and arrow labels that name the case they lead to.
  function updatePager() {
    if (!current) return;
    const list = visibleCards();
    const index = list.indexOf(current);
    count.textContent = `${index + 1} / ${list.length}`;
    steps.forEach(step => {
      const dir = Number(step.getAttribute('data-case-step'));
      const target = list[index + dir];
      const label = dir < 0 ? tr('cases.prev', 'Previous case') : tr('cases.next', 'Next case');
      // Titles may contain zero-width spaces for Japanese line breaks; they do not belong in a tooltip.
      const name = target && target.querySelector('.case-title').textContent.replace(/\u200b/g, '');
      const text = target ? label + (window.__currentLang === 'ja' ? '：' : ': ') + name : label;
      step.disabled = !target;
      step.setAttribute('aria-label', text);
      step.title = text;
    });
  }

  // Copies the card's title and categories into the dialog header (again after a language switch).
  function fillHeader() {
    if (!current) return;
    title.textContent = current.querySelector('.case-title').textContent;
    tag.textContent = categoriesOf(current)
      .map(cat => buttons.find(b => b.getAttribute('data-filter') === cat))
      .filter(Boolean)
      .map(b => b.querySelector('[data-i18n]').textContent)
      .join(' · ');
  }

  // Puts the open card's details back into the card.
  function restoreDetails() {
    if (!current) return;
    const details = body.querySelector('.case-details');
    if (details) {
      details.hidden = true;
      current.querySelector('.case-body').appendChild(details);
    }
    current = null;
  }

  function show(card) {
    restoreDetails();
    current = card;
    const picture = card.querySelector('.case-thumb picture').cloneNode(true);
    picture.querySelectorAll('source, img').forEach(n => n.setAttribute('sizes', '(min-width: 640px) 960px, 100vw'));
    const img = picture.querySelector('img');
    img.alt = '';
    img.removeAttribute('data-i18n-attr-alt');
    img.loading = 'eager';
    media.replaceChildren(picture);
    const details = card.querySelector('.case-details');
    details.hidden = false;
    body.appendChild(details);
    fillHeader();
    updatePager();
    dialog.querySelector('.case-dialog-scroll').scrollTop = 0;
    setHash(`#cases-${card.getAttribute('data-case')}`);
  }

  // Opens the details of one case. Returns false when there is no such case.
  function open(id, from) {
    const card = cards.find(c => c.getAttribute('data-case') === id);
    if (!card) return false;
    if (card.hidden) applyFilter(buttons.find(b => b.getAttribute('data-filter') === 'all'));
    opener = from || card.querySelector('[data-case-open]');
    show(card);
    if (!dialog.open) {
      dialog.showModal();
      document.documentElement.classList.add('case-dialog-open');
    }
    return true;
  }

  dialog.addEventListener('close', () => {
    document.documentElement.classList.remove('case-dialog-open');
    restoreDetails();
    media.replaceChildren();
    if (dialog.returnValue !== 'cta') setHash('#cases');
    dialog.returnValue = '';
    if (opener && opener.isConnected) opener.focus({ preventScroll: true });
  });

  // A click outside the panel lands on the backdrop, which belongs to the <dialog> itself.
  dialog.addEventListener('click', e => {
    if (e.target !== dialog) return;
    const r = dialog.getBoundingClientRect();
    if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) dialog.close();
  });
  dialog.querySelector('[data-case-close]').addEventListener('click', () => dialog.close());
  function step(dir) {
    const list = visibleCards();
    const next = list[list.indexOf(current) + dir];
    if (!next) return;
    opener = next.querySelector('[data-case-open]');
    show(next);
    // An arrow that just became disabled loses focus: keep it on the pager.
    if (document.activeElement && document.activeElement.disabled) {
      (steps.find(b => !b.disabled) || dialog.querySelector('[data-case-close]')).focus();
    }
  }

  steps.forEach(b => b.addEventListener('click', () => step(Number(b.getAttribute('data-case-step')))));
  dialog.addEventListener('keydown', e => {
    if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
      e.preventDefault();
      step(e.key === 'ArrowLeft' ? -1 : 1);
    }
  });
  // Swipe sideways on touch screens. Mostly-vertical moves are scrolling and are ignored.
  let touch = null;
  const scroller = dialog.querySelector('.case-dialog-scroll');
  scroller.addEventListener('touchstart', e => {
    touch = e.touches.length === 1 ? { x: e.touches[0].clientX, y: e.touches[0].clientY } : null;
  }, { passive: true });
  scroller.addEventListener('touchend', e => {
    if (!touch) return;
    const dx = e.changedTouches[0].clientX - touch.x;
    const dy = e.changedTouches[0].clientY - touch.y;
    touch = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) step(dx < 0 ? 1 : -1);
  }, { passive: true });
  // The contact link closes the dialog; section-links.js then scrolls to the form and sets #contact.
  // The page must be scrollable again before that, and the close event only fires later.
  dialog.querySelector('[data-case-cta]').addEventListener('click', () => {
    document.documentElement.classList.remove('case-dialog-open');
    dialog.close('cta');
  });

  grid.addEventListener('click', e => {
    const trigger = e.target.closest('[data-case-open]');
    if (trigger) open(trigger.closest('.case-study').getAttribute('data-case'), trigger);
  });

  document.addEventListener('i18n:changed', () => {
    fillHeader();
    updatePager();
    placeIndicator();
  });

  countCases();
  placeIndicator();
  window.cases = { open };
})();
