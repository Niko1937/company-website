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
  let current = null;
  let opener = null;

  function visibleCards() {
    return cards.filter(c => !c.hidden);
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
    const list = visibleCards();
    const index = list.indexOf(card);
    steps.forEach(step => {
      step.disabled = !list[index + Number(step.getAttribute('data-case-step'))];
    });
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
  steps.forEach(step => step.addEventListener('click', () => {
    const list = visibleCards();
    const next = list[list.indexOf(current) + Number(step.getAttribute('data-case-step'))];
    if (next) {
      opener = next.querySelector('[data-case-open]');
      show(next);
    }
  }));
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
    placeIndicator();
  });

  countCases();
  placeIndicator();
  window.cases = { open };
})();
