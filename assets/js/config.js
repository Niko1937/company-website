(function () {
  'use strict';

  // Applies window.SITE_CONFIG via an injected stylesheet. Load synchronously in <head>
  // (after site-config.js) so toggled elements are hidden before the body renders.
  //   data-show-if="key" : shown only when the value is true (hidden if false or undefined)
  //   data-hide-if="key" : hidden when the value is true
  const config = window.SITE_CONFIG || {};
  const keys = Object.keys(config).filter(k => /^[\w-]+$/.test(k));
  const enabled = keys.filter(k => config[k] === true);

  const selectors = [
    enabled.length
      ? `[data-show-if]:not(${enabled.map(k => `[data-show-if="${k}"]`).join(',')})`
      : '[data-show-if]',
    ...enabled.map(k => `[data-hide-if="${k}"]`)
  ];

  const style = document.createElement('style');
  style.textContent = `${selectors.join(',')}{display:none!important}`;
  document.head.appendChild(style);

  window.siteConfig = { get: key => config[key] };
})();
