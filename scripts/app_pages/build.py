# Builds the apps' pages: /ja|en/apps/ (the list, in the site's own look) and, for each app, its own pages in the
# app's look: /ja|en/apps/<app>/ (about the app), support/ and privacy/. Also the language-neutral URLs
# (/apps/, /apps/<app>/...), which open the reader's language (assets/js/lang-redirect.js).
# Usage (from the repository root, after scripts/legal_pages/build.py: the list page takes its header and footer
# from the built /ja|en/privacy/ pages): python3 scripts/app_pages/build.py .
#
# The text of each app lives in its own file here (pickle_up.py); the styles in assets/css/apps/<app>.css.
import html, os, re, sys

ROOT = sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pickle_up

SITE = 'https://quests.it.com'
LANGS = ('ja', 'en')
OTHER = {'ja': 'en', 'en': 'ja'}
LANG_LABEL = {'ja': '日本語', 'en': 'English'}
OG_LOCALE = {'ja': 'ja_JP', 'en': 'en_US'}
CSS_VERSION = 1


def read(path):
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        return f.read()


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(text)
    print('wrote', path)


e = html.escape


def ph(text):
    # Headings, phrase by phrase: '|' marks where a Japanese line may break (each phrase stays whole, as
    # BudouX would cut it); text without it is escaped as it is.
    if '|' not in text:
        return e(text)
    return ''.join(f'<span class="phrase">{e(p)}</span>' for p in text.split('|'))


def remember_lang(lang):
    # As on the other pages: this page's language is remembered first thing, so later pages open in it.
    return f"<script>try {{ localStorage.setItem('preferredLang', '{lang}'); }} catch (_) {{}}</script>"


def alternates(path):
    # path: the page's path without the language, e.g. 'apps/pickle-up/support/'.
    return '\n'.join([f'<link rel="canonical" href="/{{lang}}/{path}">'] + [
        f'<link rel="alternate" hreflang="{l}" href="/{l}/{path}">' for l in ('en', 'ja')
    ] + [f'<link rel="alternate" hreflang="x-default" href="/en/{path}">'])


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">\n'
         '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/remixicon/4.6.0/remixicon.min.css">')


# ----------------------------------------------------------------------------------------------- app pages

def badge_width(file, height=48):
    # The badge's width at `height`, from the artwork (an SVG's size, or a PNG's header).
    path = os.path.join(ROOT, 'images/apps/badges', file)
    if file.endswith('.svg'):
        w, h = (float(v) for v in re.search(r'<svg[^>]*\swidth="([\d.]+)"[^>]*\sheight="([\d.]+)"', read(path)).groups())
    else:
        with open(path, 'rb') as f:
            head = f.read(24)
        w, h = int.from_bytes(head[16:20], 'big'), int.from_bytes(head[20:24], 'big')
    return round(w * height / h)


class App:
    def __init__(self, mod):
        self.m = mod
        self.slug = mod.SLUG
        self.base = f'apps/{self.slug}/'
        self.img = f'/images/apps/{self.slug}'

    def text(self, lang):
        return self.m.JA if lang == 'ja' else self.m.EN

    def head(self, lang, path, title, description, og=True):
        t = self.text(lang)
        meta = [
            '<!DOCTYPE html>', f'<html lang="{lang}">', '<head>', '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">', remember_lang(lang),
            f'<title>{e(title)}</title>', f'<meta name="description" content="{e(description)}">',
            '<meta name="theme-color" content="#0E1014">',
            f'<link rel="icon" href="{self.img}/icon-64.png" sizes="64x64" type="image/png">',
            f'<link rel="apple-touch-icon" href="{self.img}/icon-180.png">',
            alternates(path).replace('{lang}', lang),
        ]
        if og:
            meta += [
                '<meta property="og:type" content="website">', f'<meta property="og:site_name" content="{self.m.NAME}">',
                f'<meta property="og:title" content="{e(title)}">', f'<meta property="og:description" content="{e(description)}">',
                f'<meta property="og:url" content="{SITE}/{lang}/{path}">', f'<meta property="og:locale" content="{OG_LOCALE[lang]}">',
                f'<meta property="og:image" content="{SITE}{self.img}/og-{lang}.png">',
                '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
                '<meta name="twitter:card" content="summary_large_image">',
            ]
        meta += [FONTS, f'<link rel="stylesheet" href="/assets/css/apps/{self.slug}.css?v={CSS_VERSION}">', '</head>']
        return '\n'.join(meta)

    def badges(self, lang, where):
        t = self.text(lang)
        out = []
        for store, file in (('appStore', f'app-store-{lang}.svg'), ('googlePlay', f'google-play-{lang}.png')):
            url = self.m.STORES[store]
            w = badge_width(file)  # both 48 px high, as the stores ask
            img = f'<img src="/images/apps/badges/{file}" alt="{e(t["storeAlt"][store])}" width="{w}" height="48">'
            if url:
                out.append(f'<a class="store" href="{e(url)}" target="_blank" rel="noopener">{img}</a>')
            else:
                out.append(f'<span class="store">{img}</span>')
        soon = '' if all(self.m.STORES.values()) else f'<p class="stores-note">{e(t["soon"])}</p>'
        return f'<div class="stores stores-{where}">{"".join(out)}</div>{soon}'

    def header(self, lang, path, home):
        t = self.text(lang)
        n = t['nav']
        # On the app's own page the menu scrolls within it; elsewhere it leads back to that page's sections.
        top = '' if home else f'/{lang}/{self.base}'
        other = OTHER[lang]
        return f'''<header class="app-header">
<div class="wrap bar">
<a class="app-brand" href="/{lang}/{self.base}"><img src="{self.img}/icon-128.png" alt="" width="32" height="32"><span lang="en">{self.m.NAME}</span></a>
<nav class="app-nav" aria-label="{e(n['menu'])}">
<a href="{top}#features">{e(n['features'])}</a>
<a href="{top}#how">{e(n['how'])}</a>
<a href="{top}#faq">{e(n['faq'])}</a>
<a href="/{lang}/{self.base}support/">{e(n['support'])}</a>
</nav>
<div class="app-actions">
<a class="lang" href="/{other}/{path}" hreflang="{other}" lang="{other}" aria-label="{e(t['langSwitch'])}"><i class="ri-global-line" aria-hidden="true"></i><span>{LANG_LABEL[other]}</span></a>
<a class="button button-small" href="{top}#download">{e(n['download'])}</a>
</div>
</div>
</header>'''

    def footer(self, lang, path):
        t = self.text(lang)
        f = t['footer']
        other = OTHER[lang]
        return f'''<footer class="app-footer">
<div class="wrap">
<div class="footer-grid">
<div class="footer-about">
<a class="app-brand" href="/{lang}/{self.base}"><img src="{self.img}/icon-128.png" alt="" width="32" height="32"><span lang="en">{self.m.NAME}</span></a>
<p>{e(f['tagline'])}</p>
</div>
<div>
<h2>{e(f['app'])}</h2>
<ul>
<li><a href="/{lang}/{self.base}#features">{e(f['links']['features'])}</a></li>
<li><a href="/{lang}/{self.base}support/">{e(f['links']['support'])}</a></li>
<li><a href="/{lang}/{self.base}privacy/">{e(f['links']['privacy'])}</a></li>
</ul>
</div>
<div>
<h2>{e(f['company'])}</h2>
<ul>
<li><a href="/{lang}/">{e(f['companyLinks']['home'])}</a></li>
<li><a href="/{lang}/apps/">{e(f['companyLinks']['apps'])}</a></li>
<li><a href="/{lang}/#contact">{e(f['companyLinks']['contact'])}</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p class="footer-by"><a class="quests" href="/{lang}/" lang="en">Quests</a><span>{e(f['by'])}</span></p>
<p class="footer-meta"><a class="lang" href="/{other}/{path}" hreflang="{other}" lang="{other}"><i class="ri-global-line" aria-hidden="true"></i>{LANG_LABEL[other]}</a><span lang="en">© <span data-year>2026</span> Quests Bay Pte. Ltd.</span></p>
<p class="trademarks">{e(f['trademarks'])}</p>
</div>
</div>
</footer>
<script>document.querySelectorAll('[data-year]').forEach(function (el) {{ el.textContent = new Date().getFullYear(); }});</script>'''

    def phone(self, screen, alt, lang, eager=False):
        w, h = self.m.SCREEN_SIZE
        dh = round(300 * h / w)
        load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return (f'<figure class="phone"><img src="{self.img}/screens/{screen}-{lang}.webp" alt="{e(alt)}" '
                f'width="300" height="{dh}" {load}></figure>')

    def home(self, lang):
        t = self.text(lang)
        path = self.base
        h = t['hero']
        title = ''.join(f'<span class="phrase">{e(p)}</span>' for p in h['title'])
        feats = []
        for i, it in enumerate(t['features']['items']):
            points = ''.join(f'<li><i class="ri-check-line" aria-hidden="true"></i>{e(p)}</li>' for p in it['points'])
            feats.append(f'''<article class="feature{' feature-flip' if i % 2 else ''}">
<div class="feature-media">{self.phone(it['screen'], it['alt'], lang)}</div>
<div class="feature-copy">
<p class="feature-index" lang="en">0{i + 1}</p>
<h3>{ph(it['title'])}</h3>
<p>{e(it['body'])}</p>
<ul class="points">{points}</ul>
</div>
</article>''')
        pv = t['privacy']
        pv_items = ''.join(f'<li><i class="{icon}" aria-hidden="true"></i><h3>{e(a)}</h3><p>{e(b)}</p></li>' for icon, a, b in pv['items'])
        steps = ''.join(f'<li><span class="step-number" lang="en">{n + 1}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>'
                        for n, (a, b) in enumerate(t['how']['steps']))
        faq = ''.join(f'<details><summary>{e(q)}<i class="ri-add-line" aria-hidden="true"></i></summary><p>{e(a)}</p></details>'
                      for q, a in t['faq']['items'])
        court = court_lines_svg()
        body = f'''<body class="page-home">
{self.header(lang, path, True)}
<main>
<section class="hero">
{court}
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow">{e(h['eyebrow'])}</p>
<h1>{title}</h1>
<p class="lead">{e(h['lead'])}</p>
{self.badges(lang, 'hero')}
</div>
<div class="hero-media">
<div class="glow" aria-hidden="true"></div>
{self.phone('analysis-3d', h['screenAlt'], lang, eager=True)}
</div>
</div>
</section>
<section id="features" class="section section-light">
<div class="wrap">
<div class="section-head"><p class="eyebrow">{e(t['features']['eyebrow'])}</p><h2>{ph(t['features']['title'])}</h2></div>
{''.join(feats)}
</div>
</section>
<section id="privacy" class="section section-dark">
<div class="wrap">
<div class="section-head"><p class="eyebrow">{e(pv['eyebrow'])}</p><h2>{ph(pv['title'])}</h2><p class="section-lead">{e(pv['lead'])}</p></div>
<ul class="promises">{pv_items}</ul>
<p class="section-more"><a href="privacy/">{e(pv['link'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></p>
</div>
</section>
<section id="how" class="section section-light">
<div class="wrap">
<div class="section-head"><p class="eyebrow">{e(t['how']['eyebrow'])}</p><h2>{ph(t['how']['title'])}</h2></div>
<ol class="steps">{steps}</ol>
</div>
</section>
<section id="faq" class="section">
<div class="wrap narrow">
<div class="section-head"><p class="eyebrow">{e(t['faq']['eyebrow'])}</p><h2>{ph(t['faq']['title'])}</h2></div>
<div class="faq">{faq}</div>
<p class="section-more"><a href="support/">{e(t['faq']['more'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></p>
</div>
</section>
<section id="download" class="cta">
{court}
<div class="wrap cta-inner">
<img class="cta-icon" src="{self.img}/icon-256.png" alt="" width="96" height="96">
<h2>{ph(t['cta']['title'])}</h2>
<p>{e(t['cta']['lead'])}</p>
{self.badges(lang, 'cta')}
</div>
</section>
</main>
{self.footer(lang, path)}
</body>
</html>
'''
        return self.head(lang, path, t['title'], t['description']) + '\n' + body

    def document(self, lang, sub, page, inner):
        path = self.base + sub
        return self.head(lang, path, page['title'], page['description']) + f'''
<body class="page-doc">
{self.header(lang, path, False)}
<main class="doc">
<div class="wrap narrow">
{inner}
</div>
</main>
{self.footer(lang, path)}
</body>
</html>
'''

    def support(self, lang):
        s = self.text(lang)['support']
        groups = []
        for name, items in s['groups']:
            qa = ''.join(f'<details><summary>{e(q)}<i class="ri-add-line" aria-hidden="true"></i></summary><p>{e(a)}</p></details>' for q, a in items)
            groups.append(f'<section class="doc-section"><h2>{e(name)}</h2><div class="faq">{qa}</div></section>')
        inner = f'''<p class="eyebrow">{e(s['eyebrow'])}</p>
<h1>{e(s['h1'])}</h1>
<p class="lead">{e(s['lead'])}</p>
{''.join(groups)}
<section class="doc-section contact-card">
<h2>{e(s['contactTitle'])}</h2>
<p>{e(s['contactBody'])}</p>
<p><a class="button" href="/{lang}/#contact">{e(s['contactLink'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></p>
</section>'''
        return self.document(lang, 'support/', s, inner)

    def privacy(self, lang):
        p = self.text(lang)['privacyPage']
        sections = ''.join(f'<section class="doc-section" id="{sid}"><h2>{e(title)}</h2>{body}</section>' for sid, title, body in p['sections'])
        inner = f'''<p class="eyebrow" lang="en">{e(p['eyebrow'])}</p>
<h1>{e(p['h1'])}</h1>
<p class="updated">{e(p['updated'])}: {e(self.m.UPDATED[lang])}</p>
<p class="lead">{p['lead']}</p>
{sections}'''
        return self.document(lang, 'privacy/', p, inner)


def court_lines_svg():
    # A court seen at an angle, as in the app's 3D view (the same camera: up behind the near right corner,
    # looking at the net), faint behind the hero and the closing call. Court metres: across, depth, height.
    import math
    W, L, NET, K = 6.1, 13.41, 6.705, 2.13
    eye, target = (W + 4, -4.0, 10.0), (W / 2, NET, 0.0)
    sub = lambda a, b: tuple(x - y for x, y in zip(a, b))
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    unit = lambda a: tuple(x / math.sqrt(dot(a, a)) for x in a)
    f = unit(sub(target, eye)); r = unit(cross(f, (0, 0, 1))); u = cross(r, f)

    def at(x, y, z=0.0):
        d = sub((x, y, z), eye)
        depth = dot(d, f)
        # Scaled and placed so the court sits to the right of a 1200 x 700 picture.
        return f'{780 + 900 * dot(d, r) / depth:.0f} {400 - 900 * dot(d, u) / depth:.0f}'

    lines = [((0, 0), (W, 0)), ((0, L), (W, L)), ((0, 0), (0, L)), ((W, 0), (W, L)),
             ((0, NET - K), (W, NET - K)), ((0, NET + K), (W, NET + K)),
             ((W / 2, 0), (W / 2, NET - K)), ((W / 2, NET + K), (W / 2, L))]
    court = ' '.join(f'M{at(*a)} L{at(*b)}' for a, b in lines)
    net = f'M{at(-0.3, NET, 0.914)} L{at(W + 0.3, NET, 0.914)}'
    return (f'<svg class="court-lines" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            f'<path d="{court}" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path d="{net}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>')


# --------------------------------------------------------------------------------------- language-neutral URLs

def redirect_page(path):
    # path: e.g. 'apps/pickle-up/support/'. English when nothing can run (meta refresh), as the root URL.
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quests</title>
{alternates(path).replace('{lang}', 'en')}
<meta http-equiv="refresh" content="0; url=/en/{path}">
<script src="/assets/js/lang-redirect.js"></script>
</head>
<body>
<p><a href="/ja/{path}" hreflang="ja" lang="ja">日本語</a> / <a href="/en/{path}" hreflang="en">English</a></p>
</body>
</html>
'''


# ------------------------------------------------------------------------------------------- the apps' list

APPS_LIST = {
    'ja': {'title': 'アプリ | Quests', 'description': 'Quests が開発・運営しているアプリ。', 'eyebrow': 'アプリ', 'h1': 'Quests のアプリ',
           'lead': 'Quests が開発・運営しているスマートフォン向けアプリです。'},
    'en': {'title': 'Apps | Quests', 'description': 'Apps built and run by Quests.', 'eyebrow': 'Apps', 'h1': 'Apps by Quests',
           'lead': 'Smartphone apps built and run by Quests.'},
}

LIST_CSS = '''
.apps { list-style: none; margin: 0; padding: 0; display: grid; gap: 1.25rem; }
.app-card { display: flex; gap: 1.25rem; align-items: flex-start; padding: 1.5rem; background: var(--soft); border: 1px solid #eef2f7; border-radius: 20px; }
.app-card img { flex: none; width: 72px; height: 72px; border-radius: 16px; box-shadow: 0 6px 16px -8px rgba(15,23,42,.4); }
.app-card h2 { margin: 0 0 .25rem; font-size: 1.25rem; }
.app-card p { margin: 0 0 .75rem; }
.app-card a.more { display: inline-flex; align-items: center; gap: .25rem; font-weight: 600; text-decoration: none; }
.app-card a.more:hover { text-decoration: underline; }
'''


def apps_list(lang, apps):
    # The site's own look: the header, footer and styles of the built /<lang>/privacy/ page.
    base = read(f'{lang}/privacy/index.html')
    style = re.search(r'<style>(.*?)</style>', base, re.S).group(1)
    header = re.search(r'<header class="site-header">.*?</header>', base, re.S).group(0)
    footer = re.search(r'<footer>.*?</footer>', base, re.S).group(0)
    scripts = re.findall(r'<script src="[^"]+"></script>', base)
    # The page's own language links point here, not to the privacy page.
    other = OTHER[lang]
    header = header.replace(f'href="/{other}/privacy/"', f'href="/{other}/apps/"').replace(f'href="/{lang}/privacy/" hreflang', f'href="/{lang}/apps/" hreflang')
    # The menu script at the end of the page (Esc / tap outside), without the legal pages' place-keeping.
    menu = re.search(r'// Phone menu:.*?\}\)\(\);', base, re.S).group(0)
    t = APPS_LIST[lang]
    cards = ''.join(
        f'''<li class="app-card"><img src="{a.img}/icon-256.png" alt="" width="72" height="72">
<div><h2 lang="en">{e(a.m.APP_CARD[lang]['title'])}</h2><p>{e(a.m.APP_CARD[lang]['body'])}</p>
<a class="more" href="{a.slug}/">{e(a.m.APP_CARD[lang]['cta'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></div></li>'''
        for a in apps)
    path = 'apps/'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{remember_lang(lang)}
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['description'])}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/images/brand/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{alternates(path).replace('{lang}', lang)}
{FONTS}
{''.join(scripts)}
<style>{style}{LIST_CSS}</style>
</head>
<body>
{header}
<main>
<p class="eyebrow">{e(t['eyebrow'])}</p>
<h1>{e(t['h1'])}</h1>
<p class="lead">{e(t['lead'])}</p>
<ul class="apps">{cards}</ul>
</main>
{footer}
<script>
document.getElementById('year').textContent = new Date().getFullYear();
{menu}
</script>
</body>
</html>
'''


def main():
    apps = [App(pickle_up)]
    for lang in LANGS:
        write(f'{lang}/apps/index.html', apps_list(lang, apps))
        for a in apps:
            write(f'{lang}/{a.base}index.html', a.home(lang))
            write(f'{lang}/{a.base}support/index.html', a.support(lang))
            write(f'{lang}/{a.base}privacy/index.html', a.privacy(lang))
    write('apps/index.html', redirect_page('apps/'))
    for a in apps:
        for sub in ('', 'support/', 'privacy/'):
            write(f'{a.base}{sub}index.html', redirect_page(a.base + sub))


main()
