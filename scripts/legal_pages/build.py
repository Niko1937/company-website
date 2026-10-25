# Builds the static legal pages /en|ja/privacy/ and /en|ja/terms/ from content_en.py and content_ja.py.
# Usage (from the repository root): python3 scripts/legal_pages/build.py .
#
# The header and footer look and behave like the home page's (as on the legal pages of Thoughtworks, Deloitte,
# Capgemini and others), but without Tailwind: their labels come from locales/v2/*.json and the company name from
# assets/js/site-config.js, so rebuild after changing either. Only the body is a plain document layout.
import html, json, os, re, sys

ROOT = sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_en, content_ja


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()


COMPANY = re.search(r'companyName:\s*"([^"]+)"', read('assets/js/site-config.js')).group(1)
HOME = read('en/index.html')
# Same script versions as the home page, so the Solutions menu item hides itself the same way (no demos, no item).
SCRIPTS = [m for m in re.findall(r'<script src="(/assets/js/(?:site-config|solutions)\.js\?v=\d+)"></script>', HOME)]
assert len(SCRIPTS) == 2, SCRIPTS


def texts(lang):
    data = json.loads(read(f'locales/v2/{lang}.json'))
    fill = lambda v: v.replace('{company}', COMPANY)
    return {
        'nav': {k: fill(v) for k, v in data['nav'].items()},
        'footer': {k: fill(v) for k, v in data['footer'].items()},
    }


CSS = """
:root { --ink: #111827; --body: #374151; --muted: #6b7280; --line: #e5e7eb; --soft: #f8fafc; --primary: #0047AB; --dark: #1F1F1F; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
body { margin: 0; background: #fff; color: var(--body); font-family: 'Inter', 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif; line-height: 1.8; }
/* Same text rendering as the home page (Tailwind's base styles): no font-smoothing override, which made the
   text look thinner on macOS. */
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; }
html[lang="ja"] { line-break: strict; overflow-wrap: break-word; font-feature-settings: "palt"; letter-spacing: .02em; }
a { color: var(--primary); text-underline-offset: 2px; }
button { font: inherit; }
/* Tailwind's .container, as on the home page */
.container { width: 100%; margin: 0 auto; padding: 0 1.5rem; }
@media (min-width: 640px) { .container { max-width: 640px; } }
@media (min-width: 768px) { .container { max-width: 768px; } }
@media (min-width: 1024px) { .container { max-width: 1024px; } }
@media (min-width: 1280px) { .container { max-width: 1280px; } }
@media (min-width: 1536px) { .container { max-width: 1536px; } }

/* Page changes cross-fade with the header in place, as on the home page. */
@media (prefers-reduced-motion: no-preference) {
  @view-transition { navigation: auto; }
}
.site-header { view-transition-name: site-header; }
/* Header: the home page's header in its scrolled state */
.site-header, footer { line-height: 1.5; }
.site-header { position: sticky; top: 0; z-index: 50; background: rgba(31,31,31,.94); -webkit-backdrop-filter: blur(15px); backdrop-filter: blur(15px); }
.site-header .bar { display: flex; align-items: center; justify-content: space-between; padding-top: .5rem; padding-bottom: .5rem; }
.brand { color: #fff; font-family: 'Inter'; font-size: 1.5rem; line-height: 2rem; font-weight: 700; text-decoration: none; white-space: nowrap; }
.desktop-nav { display: none; align-items: center; gap: 2rem; }
.desktop-nav a.nav-link { color: #fff; text-decoration: none; white-space: nowrap; transition: color .25s ease; }
.desktop-nav a.nav-link:hover { color: #93c5fd; }
.lang-switcher { display: inline-flex; align-items: center; gap: .5rem; padding-left: 1.25rem; font-size: .875rem; }
.lang-switcher i { color: rgba(255,255,255,.85); font-size: 1rem; }
.lang-switcher a { color: rgba(255,255,255,.85); text-decoration: none; transition: color .2s; }
.lang-switcher a:hover, .lang-switcher a[aria-current] { color: #93c5fd; }
.lang-switcher a[aria-current] { font-weight: 600; }
.lang-divider { color: rgba(255,255,255,.35); }
.mobile-actions { display: flex; align-items: center; gap: 1rem; }
.icon-btn { width: 2rem; height: 2rem; display: inline-flex; align-items: center; justify-content: center; color: rgba(255,255,255,.85); background: none; border: 0; padding: 0; cursor: pointer; text-decoration: none; transition: color .25s ease; }
.icon-btn:hover { color: #93c5fd; }
#mobileMenuBtn { color: #fff; }
#mobileMenu { position: absolute; left: 0; right: 0; background: #fff; border-top: 1px solid #f1f5f9; box-shadow: 0 16px 32px -12px rgba(0,0,0,.25); }
#mobileMenu[hidden] { display: none; }
#mobileMenu nav { display: flex; flex-direction: column; padding-top: .5rem; padding-bottom: .5rem; }
#mobileMenu a { display: block; padding: .875rem 0; color: #1f2937; font-size: 1.0625rem; font-weight: 500; text-decoration: none; border-bottom: 1px solid #f3f4f6; transition: color .2s; }
#mobileMenu a:last-child { border-bottom: 0; }
#mobileMenu a:hover { color: var(--primary); }
@media (min-width: 1024px) {
  .brand { font-size: 1.875rem; line-height: 2.25rem; }
  .desktop-nav { display: flex; }
  .mobile-actions, #mobileMenu { display: none !important; }
}

/* Document */
main { max-width: 46rem; margin: 0 auto; padding: 4rem 1.5rem 5rem; }
html[lang="ja"] main { max-width: 42rem; }
.eyebrow { margin: 0 0 .5rem; color: var(--primary); font-size: .875rem; font-weight: 600; }
h1 { margin: 0 0 .75rem; color: var(--ink); font-size: clamp(2rem, 4vw, 2.5rem); line-height: 1.25; letter-spacing: -.01em; }
.updated { margin: 0 0 2rem; color: var(--muted); font-size: .9375rem; }
.lead { margin: 0 0 2.5rem; font-size: 1.0625rem; }
.toc { margin: 0 0 3rem; padding: 1.25rem 1.5rem; background: var(--soft); border: 1px solid #eef2f7; border-radius: 16px; }
.toc p { margin: 0 0 .5rem; color: var(--ink); font-weight: 600; font-size: .9375rem; }
/* The headings already carry their numbers. */
.toc ol { margin: 0; padding: 0; list-style: none; columns: 2; column-gap: 2rem; font-size: .9375rem; line-height: 1.9; }
.toc li { margin: 0; break-inside: avoid; text-wrap: pretty; }
p, li { text-wrap: pretty; }
.toc a { color: var(--body); text-decoration: none; }
.toc a:hover { color: var(--primary); text-decoration: underline; }
@media (max-width: 639px) { .toc ol { columns: 1; } main { padding-top: 2.5rem; } }
section { scroll-margin-top: 5rem; padding-top: 2rem; margin-top: 2rem; border-top: 1px solid var(--line); }
section:first-of-type { border-top: 0; margin-top: 0; padding-top: 0; }
h2 { margin: 0 0 1rem; color: var(--ink); font-size: 1.375rem; line-height: 1.4; }
h3 { margin: 1.5rem 0 .5rem; color: var(--ink); font-size: 1.0625rem; }
p { margin: 0 0 1rem; }
ul { margin: 0 0 1rem; padding-left: 1.25rem; }
li { margin: .25rem 0; }
.table-wrap { overflow-x: auto; margin: 0 0 1rem; }
table { width: 100%; border-collapse: collapse; font-size: .9375rem; line-height: 1.6; }
th, td { text-align: left; vertical-align: top; padding: .75rem .75rem .75rem 0; border-bottom: 1px solid var(--line); }
th { color: var(--ink); font-weight: 600; white-space: nowrap; }
.contact { padding: 1.25rem 1.5rem; background: var(--soft); border: 1px solid #eef2f7; border-radius: 16px; }
.contact p { margin: 0; }

/* Footer: same as the home page */
footer { background: var(--dark); color: #fff; padding: 3rem 0; }
html[lang="ja"] footer p { line-height: 1.85; }
.footer-top { display: flex; flex-direction: column; gap: 2.5rem; }
.footer-brand { display: inline-block; margin-bottom: 1rem; color: #fff; font-family: 'Inter'; font-size: 1.875rem; line-height: 2.25rem; font-weight: 700; text-decoration: none; }
.tagline { margin: 0 0 1.5rem; color: #9ca3af; }
.social { display: flex; gap: 1rem; }
.social a { width: 2rem; height: 2rem; display: inline-flex; align-items: center; justify-content: center; color: #9ca3af; text-decoration: none; transition: color .2s; }
.social a:hover { color: #fff; }
.footer-cols { display: flex; gap: 2.5rem; }
.footer-cols > div { flex: 1; }
.footer-cols h3 { margin: 0 0 1rem; color: #fff; font-size: 1.125rem; line-height: 1.75rem; font-weight: 600; }
.footer-cols ul { list-style: none; margin: 0; padding: 0; display: grid; gap: .75rem; }
.footer-cols li { margin: 0; }
.footer-cols a { color: #9ca3af; text-decoration: none; transition: color .2s; }
.footer-cols a:hover { color: #fff; }
.copyright { margin: 2.5rem 0 0; color: #6b7280; }
@media (min-width: 768px) {
  .footer-top { flex-direction: row; }
  .footer-top > div { width: 50%; }
}
"""

MENU_SCRIPT = """
// Phone menu: same behaviour as the home page (Esc, a tap outside or choosing a link closes it).
(function () {
  var button = document.getElementById('mobileMenuBtn');
  var menu = document.getElementById('mobileMenu');
  var header = document.querySelector('.site-header');
  var labels = { open: button.getAttribute('data-open-label'), close: button.getAttribute('data-close-label') };
  function setOpen(open) {
    menu.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? labels.close : labels.open);
    button.querySelector('i').className = (open ? 'ri-close-line' : 'ri-menu-line') + ' ri-lg';
  }
  button.addEventListener('click', function () { setOpen(menu.hidden); });
  menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) { setOpen(false); button.focus(); } });
  document.addEventListener('click', function (e) { if (!menu.hidden && !header.contains(e.target)) setOpen(false); });
})();
"""


def nav_links(lang, t, cls=''):
    attr = f' class="{cls}"' if cls else ''
    items = [('about', 'about', ''), ('services', 'services', ''), ('solutions', 'solutions', ' data-solutions'),
             ('cases', 'cases', ''), ('contact', 'contact', '')]
    return '\n'.join(f'<a href="/{lang}/#{anchor}"{attr}{extra}>{html.escape(t["nav"][key])}</a>' for anchor, key, extra in items)


def header(lang, kind, t):
    other = 'ja' if lang == 'en' else 'en'
    switch_label = 'Switch language' if lang == 'en' else '言語を切り替える'
    current = lambda l: ' aria-current="page"' if l == lang else ''
    return f"""<header class="site-header">
<div class="container bar">
<a class="brand" href="/{lang}/">{html.escape(COMPANY)}</a>
<nav class="desktop-nav" aria-label="{'Main' if lang == 'en' else 'メイン'}">
{nav_links(lang, t, 'nav-link')}
<span class="lang-switcher">
<i class="ri-global-line" aria-hidden="true"></i>
<a href="/en/{kind}/" hreflang="en" lang="en"{current('en')}>English</a>
<span class="lang-divider">|</span>
<a href="/ja/{kind}/" hreflang="ja" lang="ja"{current('ja')}>日本語</a>
</span>
</nav>
<div class="mobile-actions">
<a class="icon-btn" href="/{other}/{kind}/" hreflang="{other}" aria-label="{switch_label}"><i class="ri-global-line ri-lg" aria-hidden="true"></i></a>
<button type="button" id="mobileMenuBtn" class="icon-btn" aria-expanded="false" aria-controls="mobileMenu" aria-label="{html.escape(t['nav']['openMenu'])}" data-open-label="{html.escape(t['nav']['openMenu'])}" data-close-label="{html.escape(t['nav']['closeMenu'])}"><i class="ri-menu-line ri-lg" aria-hidden="true"></i></button>
</div>
</div>
<div id="mobileMenu" hidden>
<nav class="container">
{nav_links(lang, t)}
</nav>
</div>
</header>"""


def footer(lang, t):
    f = t['footer']
    return f"""<footer>
<div class="container">
<div class="footer-top">
<div>
<a class="footer-brand" href="/{lang}/">{html.escape(COMPANY)}</a>
<p class="tagline">{html.escape(f['taglineLine1'])}<br>{html.escape(f['taglineLine2'])}</p>
<div class="social">
<a href="https://www.linkedin.com/company/quests-group" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="ri-linkedin-box-fill ri-lg" aria-hidden="true"></i></a>
<a href="https://www.youtube.com/@QuestsBay" target="_blank" rel="noopener" aria-label="YouTube"><i class="ri-youtube-fill ri-lg" aria-hidden="true"></i></a>
</div>
</div>
<div class="footer-cols">
<div>
<h3>{html.escape(f['quickLinks'])}</h3>
<ul>
{''.join(f'<li{" data-solutions" if key == "solutions" else ""}><a href="/{lang}/#{key}">{html.escape(t["nav"][key])}</a></li>' for key in ['about', 'services', 'solutions', 'cases', 'contact'])}
</ul>
</div>
<div>
<h3>{html.escape(f['legal'])}</h3>
<ul>
<li><a href="/{lang}/privacy/">{html.escape(f['privacyPolicy'])}</a></li>
<li><a href="/{lang}/terms/">{html.escape(f['termsOfService'])}</a></li>
</ul>
</div>
</div>
</div>
<p class="copyright">© <span id="year">2026</span> {html.escape(f['copyrightSuffix'])}</p>
</div>
</footer>"""


def page(lang, kind, c):
    t = texts(lang)
    toc = ''.join(f'<li><a href="#{sid}">{html.escape(title)}</a></li>' for sid, title, _ in c['sections'])
    body = ''.join(f'<section id="{sid}">\n<h2>{html.escape(title)}</h2>\n{content}\n</section>\n' for sid, title, content in c['sections'])
    L = c['labels']
    scripts = '\n'.join(f'<script src="{src}"></script>' for src in SCRIPTS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(c['title'])} | {html.escape(COMPANY)}</title>
<meta name="description" content="{html.escape(c['description'])}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/images/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="/{lang}/{kind}/">
<link rel="alternate" hreflang="en" href="/en/{kind}/">
<link rel="alternate" hreflang="ja" href="/ja/{kind}/">
<link rel="alternate" hreflang="x-default" href="/en/{kind}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+JP:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/remixicon/4.6.0/remixicon.min.css">
{scripts}
<style>{CSS}</style>
<!-- Start loading other pages of this site when the pointer rests on a link (Chrome, Edge). Links within this page are skipped. -->
<script type="speculationrules">{{"prefetch": [{{"source": "document", "where": {{"and": [{{"href_matches": "/*"}}, {{"not": {{"selector_matches": "a[href^='#']"}}}}]}}, "eagerness": "moderate"}}]}}</script>
</head>
<body>
{header(lang, kind, t)}
<main>
<p class="eyebrow">Quests Bay Pte. Ltd.</p>
<h1>{html.escape(c['title'])}</h1>
<p class="updated">{html.escape(c['updated'])}</p>
<p class="lead">{c['lead']}</p>
<nav class="toc" aria-label="{html.escape(L['toc'])}"><p>{html.escape(L['toc'])}</p><ol>{toc}</ol></nav>
{body}</main>
{footer(lang, t)}
<script>
document.getElementById('year').textContent = new Date().getFullYear();
// Remember this page's language, as the home page does (assets/js/i18n.js, key "preferredLang"),
// so every later page, including the root URL, opens in the same language.
try {{ localStorage.setItem('preferredLang', '{lang}'); }} catch (_) {{}}
{MENU_SCRIPT}</script>
</body>
</html>
"""


for lang, mod in [('en', content_en), ('ja', content_ja)]:
    for kind in ['privacy', 'terms']:
        out = os.path.join(ROOT, lang, kind)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page(lang, kind, getattr(mod, kind.upper())))
        print('wrote', lang, kind)
