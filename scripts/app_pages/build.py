# Builds the apps' pages: /ja|en/apps/ (the list, in the site's own look) and, for each app, its own pages in the
# app's look: /ja|en/apps/<app>/ (about the app), support/ and privacy/. Also the language-neutral URLs
# (/apps/, /apps/<app>/...), which open the reader's language (assets/js/lang-redirect.js).
# Usage (from the repository root, after scripts/legal_pages/build.py: the list page takes its header and footer
# from the built /ja|en/privacy/ pages): python3 scripts/app_pages/build.py .
#
# The text of each app lives in its own file here (pickle_up.py); the styles in assets/css/apps/<app>.css.
import html, json, os, re, sys

ROOT = sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pickle_up

SITE = 'https://quests.it.com'
LANGS = ('ja', 'en')
OTHER = {'ja': 'en', 'en': 'ja'}
LANG_LABEL = {'ja': '日本語', 'en': 'English'}
OG_LOCALE = {'ja': 'ja_JP', 'en': 'en_US'}
CSS_VERSION = 42


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
            '<meta name="theme-color" content="#141110">',
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
        # The support page is not one of them: it is reached from the FAQ's link and the footer.
        top = '' if home else f'/{lang}/{self.base}'
        other = OTHER[lang]
        # On the app's own page the bar lies over the dark hero, see-through until the page is scrolled.
        return f'''<header class="app-header{' over-hero' if home else ''}">
<div class="bar">
<a class="app-brand" href="/{lang}/{self.base}"><img src="{self.img}/icon-128.png" alt="" width="32" height="32"><span lang="en">{self.m.NAME}</span></a>
<nav class="app-nav" aria-label="{e(n['menu'])}">
<a href="{top}#features">{e(n['features'])}</a>
<a href="{top}#how">{e(n['how'])}</a>
<a href="{top}#pricing">{e(n['pricing'])}</a>
<a href="{top}#privacy">{e(n['privacy'])}</a>
<a href="{top}#faq">{e(n['faq'])}</a>
</nav>
<div class="app-actions">
<a class="lang" href="/{other}/{path}" hreflang="{other}" lang="{other}" aria-label="{e(t['langSwitch'])}"><i class="ri-global-line" aria-hidden="true"></i><span>{LANG_LABEL[other]}</span></a>
<a class="button button-small header-download" href="{top}#download">{e(n['download'])}</a>
<button type="button" id="appMenuBtn" class="menu-btn" aria-expanded="false" aria-controls="appMenu" aria-label="{e(n['menuOpen'])}" data-open-label="{e(n['menuOpen'])}" data-close-label="{e(n['menuClose'])}"><i class="ri-menu-line" aria-hidden="true"></i></button>
</div>
</div>
<div id="appMenu" class="app-menu" hidden>
<nav class="wrap" aria-label="{e(n['menu'])}">
<a href="{top}#features">{e(n['features'])}</a>
<a href="{top}#how">{e(n['how'])}</a>
<a href="{top}#pricing">{e(n['pricing'])}</a>
<a href="{top}#privacy">{e(n['privacy'])}</a>
<a href="{top}#faq">{e(n['faq'])}</a>
<a class="app-menu-download" href="{top}#download">{e(n['download'])}</a>
</nav>
</div>
</header>'''

    def footer(self, lang, path):
        t = self.text(lang)
        f = t['footer']
        # The year is this year's, set by the script below (the 2026 written in the page is only the fallback).
        return f'''<footer class="app-footer">
<div class="wrap">
<div class="footer-grid">
<div class="footer-about">
<a class="app-brand" href="/{lang}/{self.base}"><img src="{self.img}/icon-128.png" alt="" width="32" height="32"><span lang="en">{self.m.NAME}</span></a>
</div>
<div>
<h2>{e(f['app'])}</h2>
<ul>
<li><a href="/{lang}/{self.base}support/">{e(f['links']['support'])}</a></li>
<li><a href="/{lang}/{self.base}support/#contact">{e(f['links']['contact'])}</a></li>
<li><a href="/{lang}/{self.base}privacy/">{e(f['links']['privacy'])}</a></li>
</ul>
</div>
<div>
<h2>{e(f['company'])}</h2>
<ul>
<li><a href="/{lang}/">{e(f['companyLinks']['home'])}</a></li>
<li><a href="/{lang}/apps/">{e(f['companyLinks']['apps'])}</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p class="footer-by"><a class="quests" href="/{lang}/" lang="en">Quests</a><span lang="en">© <span data-year>2026</span> Quests Bay Pte. Ltd.</span></p>
<p class="trademarks">{e(f['trademarks'])}</p>
</div>
</div>
</footer>
<script src="/assets/js/app-menu.js?v={CSS_VERSION}" defer></script>
<script src="/assets/js/app-lang.js?v={CSS_VERSION}" defer></script>
<script>document.querySelectorAll('[data-year]').forEach(function (el) {{ el.textContent = new Date().getFullYear(); }});</script>'''

    def phone(self, screen, alt, lang, eager=False, tag='figure'):
        w, h = self.m.SCREEN_SIZE
        dh = round(300 * h / w)
        load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return (f'<{tag} class="phone"><img src="{self.img}/screens/{screen}-{lang}.webp" alt="{e(alt)}" '
                f'width="300" height="{dh}" {load}></{tag}>')

    def audio_button(self, audio):
        # A sound sample beside a feature (the score call, in the app's own voice; assets/js/app-audio.js).
        if not audio:
            return ''
        return (f'\n<button type="button" class="audio-sample" data-audio="/assets/audio/apps/{self.slug}/{audio["src"]}">'
                f'<i class="ri-volume-up-line" aria-hidden="true"></i><span>{e(audio["label"])}</span></button>')

    def slides(self, slides, lang):
        # One screen, or several to page through (‹ ›, the dots, or a swipe; assets/js/app-carousel.js).
        # Without the script they still scroll sideways, one screen at a time.
        # No caption under the screen: the feature's text says it, and on phones it was too much to read.
        figs = ''.join(f'<figure class="slide">{self.phone(screen, alt, lang, tag="div")}</figure>' for screen, alt in slides)
        if len(slides) == 1:
            return f'<div class="carousel carousel-single"><div class="carousel-track">{figs}</div></div>'
        c = self.text(lang)['carousel']
        current = ' aria-current="true"'
        dots = ''.join(f'<button type="button" class="carousel-dot" aria-label="{e(c["slide"].format(n=i + 1))}"{current if i == 0 else ""}></button>'
                       for i in range(len(slides)))
        return (f'<div class="carousel" data-carousel><div class="carousel-track" tabindex="0">{figs}</div>'
                f'<div class="carousel-nav"><button type="button" class="carousel-prev" aria-label="{e(c["prev"])}" disabled><i class="ri-arrow-left-s-line" aria-hidden="true"></i></button>'
                f'<div class="carousel-dots">{dots}</div>'
                f'<button type="button" class="carousel-next" aria-label="{e(c["next"])}"><i class="ri-arrow-right-s-line" aria-hidden="true"></i></button></div></div>')

    def home(self, lang):
        t = self.text(lang)
        path = self.base
        h = t['hero']
        title = ''.join(f'<span class="phrase">{e(p)}</span>' for p in h['title'])
        feats = []
        for i, it in enumerate(t['features']['items']):
            feats.append(f'''<article class="feature{' feature-flip' if i % 2 else ''}">
<div class="feature-media">{self.slides(it['slides'], lang)}</div>
<div class="feature-copy">
<h3>{ph(it['title'])}</h3>
<p>{e(it['body'])}</p>{self.audio_button(it.get('audio'))}
</div>
</article>''')
        pv = t['privacy']
        pv_items = ''.join(f'<li><i class="{icon}" aria-hidden="true"></i><h3>{e(a)}</h3><p>{e(b)}</p></li>' for icon, a, b in pv['items'])
        # Two cards, the free plan and Premium (highlighted); docs/PRICING.md in the app's repository is the source.
        plans = ''.join(
            f'''<article class="plan{' plan-premium' if p.get('badge') else ''}">
<div class="plan-head">
<div class="plan-title"><h3>{e(p['name'])}</h3>{f'<span class="plan-badge">{e(p["badge"])}</span>' if p.get('badge') else ''}</div>
<p class="plan-price"><span lang="en">{e(p['price'])}</span><span class="plan-period">{e(p['period'])}</span></p>
<p class="plan-sub">{e(p['sub'])}</p>{f'<p class="plan-trial">{e(p["trial"]).replace(chr(10), "<br>")}</p>' if p.get('trial') else ''}
</div>
<dl>{''.join(f'<div><dt>{e(k)}</dt><dd>{'<i class="ri-check-line" aria-hidden="true"></i>' if p.get('badge') else ''}{e(v)}</dd></div>' for k, v in p['items'])}</dl>
</article>''' for p in t['pricing']['plans'])
        steps = ''.join(f'<li><span class="step-number" lang="en">{n + 1}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>'
                        for n, (a, b) in enumerate(t['how']['steps']))
        faq = ''.join(f'<details><summary>{e(q)}<i class="ri-add-line" aria-hidden="true"></i></summary><p>{e(a)}</p></details>'
                      for q, a in t['faq']['items'])
        court = court_lines_svg()
        hero_court = hero_court_svg()
        # Three of the sample's numbers around the phone (never over it): decorative, as its screens show them too.
        (in_label, in_value), (net_label, net_value), (miss_label, (net_name, net_n), (out_name, out_n)) = h['stats']
        # A label breaks only before its bracket ("…（中央値）"), not inside a word. The space before an English
        # bracket stays between the phrases: inside one (an inline-block), it would be dropped.
        label = lambda text: ' '.join(''.join(f'<span class="phrase">{e(p)}</span>' for p in re.split(r'(?=（)', part))
                                      for part in re.split(r' (?=\()', text))
        bars = ''.join(f'<rect x="{i * 12}" y="{28 - v}" width="10" height="{v}" rx="2"/>' for i, v in enumerate((8, 16, 24, 28, 19, 12, 6)))
        stats = f'''<div class="hero-stats" aria-hidden="true">
<div class="hero-stat hero-stat-1"><span class="hero-stat-label">{label(in_label)}</span><span class="hero-stat-value">{e(in_value)}</span><span class="hero-stat-bar"><span style="width:{e(in_value)}"></span></span></div>
<div class="hero-stat hero-stat-2"><span class="hero-stat-label">{label(net_label)}</span><span class="hero-stat-value">{e(net_value)}</span><svg class="hero-stat-bars" viewBox="0 0 82 28">{bars}</svg></div>
<div class="hero-stat hero-stat-3"><span class="hero-stat-label">{label(miss_label)}</span><span class="hero-stat-misses"><span><b>{net_n}</b> {e(net_name)}</span><span><b>{out_n}</b> {e(out_name)}</span></span><span class="hero-stat-split"><span class="net" style="flex:{net_n}"></span><span class="out" style="flex:{out_n}"></span></span></div>
</div>'''
        body = f'''<body class="page-home">
{self.header(lang, path, True)}
<main>
<section class="hero">
{hero_court}
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="hero-app"><img src="{self.img}/icon-128.png" alt="" width="40" height="40"><span lang="en">{self.m.NAME}</span></p>
<h1>{title}</h1>
<p class="lead">{e(h['lead'])}</p>
{self.badges(lang, 'hero')}
</div>
<div class="hero-media">
{stats}
{self.phone(h['screen'], h['screenAlt'], lang, eager=True)}
</div>
</div>
</section>
<section id="features" class="section section-light">
<div class="wrap">
<h2 class="section-title">{ph(t['features']['title'])}</h2>
{''.join(feats)}
</div>
</section>
<section id="how" class="section">
<div class="wrap">
<h2 class="section-title">{ph(t['how']['title'])}</h2>
<ol class="steps" data-swipe>{steps}</ol>
<div class="swipe-pager" data-swipe-pager hidden><span class="swipe-count" data-swipe-count aria-live="polite"></span><button type="button" class="swipe-arrow" data-swipe-prev aria-label="{e(t['carousel']['prev'])}"><i class="ri-arrow-left-s-line" aria-hidden="true"></i></button><button type="button" class="swipe-arrow" data-swipe-next aria-label="{e(t['carousel']['next'])}"><i class="ri-arrow-right-s-line" aria-hidden="true"></i></button></div>
</div>
</section>
<section id="pricing" class="section section-light">
<div class="wrap">
<h2 class="section-title">{ph(t['pricing']['title'])}</h2>
<div class="plans">{plans}</div>
<p class="plans-note">{e(t['pricing']['note'])}</p>
</div>
</section>
<section id="privacy" class="section section-dark">
<div class="wrap">
<h2 class="section-title">{ph(pv['title'])}</h2>
<ul class="promises" data-swipe>{pv_items}</ul>
<div class="swipe-pager swipe-pager-dark" data-swipe-pager hidden><span class="swipe-count" data-swipe-count aria-live="polite"></span><button type="button" class="swipe-arrow" data-swipe-prev aria-label="{e(t['carousel']['prev'])}"><i class="ri-arrow-left-s-line" aria-hidden="true"></i></button><button type="button" class="swipe-arrow" data-swipe-next aria-label="{e(t['carousel']['next'])}"><i class="ri-arrow-right-s-line" aria-hidden="true"></i></button></div>
<p class="section-more"><a href="privacy/">{e(pv['link'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></p>
</div>
</section>
<section id="faq" class="section">
<div class="wrap narrow">
<h2 class="section-title">{ph(t['faq']['title'])}</h2>
<div class="faq">{faq}</div>
<p class="section-more"><a href="support/">{e(t['faq']['more'])}<i class="ri-arrow-right-line" aria-hidden="true"></i></a></p>
</div>
</section>
<section id="download" class="cta">
{court}
<div class="wrap cta-inner">
<img class="cta-icon" src="{self.img}/icon-256.png" alt="" width="96" height="96">
<h2>{ph(t['cta']['title'])}</h2>
{self.badges(lang, 'cta')}
</div>
</section>
</main>
{self.footer(lang, path)}
<script src="/assets/js/app-carousel.js?v={CSS_VERSION}" defer></script>
<script src="/assets/js/app-audio.js?v={CSS_VERSION}" defer></script>
<script src="/assets/js/app-swipe.js?v={CSS_VERSION}" defer></script>
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
        inner = f'''<h1>{e(s['h1'])}</h1>
<p class="lead">{e(s['lead'])}</p>
{''.join(groups)}
{self.contact_form(lang)}'''
        return self.document(lang, 'support/', s, inner)

    def contact_form(self, lang):
        # The app's own contact form, at the end of its support page (the footer's Contact and the app's
        # Contact button open it at #contact). It works like the company's form on the home page: nothing is
        # sent from the page; it opens the visitor's email app with the answers filled in
        # (assets/js/app-contact.js). ?app= and ?os=, added by the app, fill in the version and the phone.
        c = self.text(lang)['support']['contact']
        req = f'<span class="form-required">{e(c["required"])}</span>'

        def field(fid, label, control, required=False, hint=''):
            hint_html = f'<p class="form-hint" id="{fid}-hint">{e(hint)}</p>' if hint else ''
            error = f'<p class="form-error" id="{fid}-error" role="alert" hidden></p>' if required else ''
            return (f'<div class="form-field"><label for="{fid}">{e(label)}{req if required else ""}</label>'
                    f'{control}{hint_html}{error}</div>')

        def described(fid, required, hint=False):
            ids = ([f'{fid}-hint'] if hint else []) + ([f'{fid}-error'] if required else [])
            return f' aria-describedby="{" ".join(ids)}"' if ids else ''

        topics = ''.join(f'<option value="{k}">{e(c["topics"][k])}</option>' for k in self.m.CONTACT_TOPICS)
        strings = {k: c[k] for k in ('name', 'email', 'topic', 'device', 'appVersion', 'message', 'mailSubject',
                                     'mailerTitle', 'mailerDescription', 'mailerDefault', 'mailerOutlookWeb', 'close')}
        strings['errors'] = c['errors']
        data = e(json.dumps(strings, ensure_ascii=False))
        return f'''<section class="doc-section contact-section" id="contact">
<h2>{e(c['title'])}</h2>
<p>{e(c['lead'])}</p>
<form class="contact-form" id="appContactForm" novalidate data-strings="{data}" data-lang="{lang}">
{field('cf-name', c['name'], f'<input type="text" id="cf-name" name="name" autocomplete="name" placeholder="{e(c["namePlaceholder"])}" required{described("cf-name", True)}>', True)}
{field('cf-email', c['email'], f'<input type="email" id="cf-email" name="email" autocomplete="email" placeholder="{e(c["emailPlaceholder"])}" required{described("cf-email", True)}>', True)}
{field('cf-topic', c['topic'], f'<select id="cf-topic" name="topic" required{described("cf-topic", True)}><option value="" disabled selected>{e(c["topicPlaceholder"])}</option>{topics}</select>', True)}
<div class="form-row">
{field('cf-device', c['device'], f'<input type="text" id="cf-device" name="device" placeholder="{e(c["devicePlaceholder"])}">')}
{field('cf-app', c['appVersion'], f'<input type="text" id="cf-app" name="app" inputmode="decimal" placeholder="{e(c["appVersionPlaceholder"])}"{described("cf-app", False, True)}>', hint=c['appVersionHint'])}
</div>
{field('cf-message', c['message'], f'<textarea id="cf-message" name="message" rows="6" placeholder="{e(c["messagePlaceholder"])}" required{described("cf-message", True)}></textarea>', True)}
<p class="form-note">{c['privacyNote']}</p>
<button type="submit" class="button">{e(c['submit'])}<i class="ri-mail-send-line" aria-hidden="true"></i></button>
</form>
</section>
<script src="/assets/js/app-contact.js?v={CSS_VERSION}" defer></script>'''

    def privacy(self, lang):
        p = self.text(lang)['privacyPage']
        sections = ''.join(f'<section class="doc-section" id="{sid}"><h2>{e(title)}</h2>{body}</section>' for sid, title, body in p['sections'])
        inner = f'''<p class="eyebrow" lang="en">{e(p['eyebrow'])}</p>
<h1>{e(p['h1'])}</h1>
<p class="updated">{e(p['updated'])}: {e(self.m.UPDATED[lang])}</p>
<p class="lead">{p['lead']}</p>
{sections}'''
        return self.document(lang, 'privacy/', p, inner)


def court_lines_svg(at_x=780, at_y=400):
    # A court seen at an angle, as in the app's 3D view (the same camera: up behind the near right corner,
    # looking at the net), faint behind the closing call. Court metres: across, depth, height.
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
        return f'{at_x + 900 * dot(d, r) / depth:.0f} {at_y - 900 * dot(d, u) / depth:.0f}'

    lines = [((0, 0), (W, 0)), ((0, L), (W, L)), ((0, 0), (0, L)), ((W, 0), (W, L)),
             ((0, NET - K), (W, NET - K)), ((0, NET + K), (W, NET + K)),
             ((W / 2, 0), (W / 2, NET - K)), ((W / 2, NET + K), (W / 2, L))]
    court = ' '.join(f'M{at(*a)} L{at(*b)}' for a, b in lines)
    # The net as it stands: a post just outside each sideline, the tape between their tops, and the mesh
    # down to the ground (a raised line alone read as floating off the court).
    P, H = 0.15, 0.914
    net = (f'M{at(-P, NET)} L{at(-P, NET, H)} L{at(W + P, NET, H)} L{at(W + P, NET)}')
    mesh = f'M{at(-P, NET, H)} L{at(W + P, NET, H)} L{at(W + P, NET)} L{at(-P, NET)} Z'
    return (f'<svg class="court-lines" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            f'<path class="lines" d="{court}" fill="none" stroke="currentColor" stroke-width="2"/>'
            f'<path class="lines" d="{mesh}" fill="currentColor" fill-opacity=".18" stroke="none"/>'
            f'<path class="lines" d="{net}" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/></svg>')


def hero_court_svg(side=5.0, back=-3.0, up=6.5, x0=900, y0=240, scale=920, shots=None):
    # The hero's picture: a big court at the app's 3D angle (up behind the near right corner, looking at the
    # net), with three of your shots as the app marks them: a drop into the back of the far kitchen and a deep
    # ball to the far right back (yellow rings, in), and one long past the baseline (an orange x, out).
    # Each flight is round dots, faint near you and fuller further away; the marks are drawn the size they
    # would be lying on the court there, so nearer ones are bigger. The net is drawn last so nothing hides it.
    # Placed (in the 1200 x 700 picture) so the flights start over the near court left of the phone, and the
    # marks land where the phone and its number cards leave them in view, at 1280 px wide too. Below 1180 px
    # the cards move under the phone, so the shots (.hero-shots) are left out there and the court stays.
    import math
    W, L, NET, K = 6.1, 13.41, 6.705, 2.13
    TANGERINE, LIGHT_TANGERINE, BALL, LINE = '#FF6B2C', '#FF8A57', '#FCE97A', '#F7F2EC'
    # The camera: `side` m right of the right sideline, `back` m behind the near baseline, `up` m high.
    eye, target = (W + side, back, up), (W / 2 - .5, NET + 1.0, 0.0)
    sub = lambda a, b: tuple(x - y for x, y in zip(a, b))
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    unit = lambda a: tuple(x / math.sqrt(dot(a, a)) for x in a)
    f = unit(sub(target, eye)); r = unit(cross(f, (0, 0, 1))); u = cross(r, f)

    def at(x, y, z=0.0):
        d = sub((x, y, z), eye)
        depth = dot(d, f)
        return x0 + scale * dot(d, r) / depth, y0 - scale * dot(d, u) / depth

    pts = lambda ps: ' L'.join(f'{x:.1f} {y:.1f}' for x, y in ps)
    out = []
    # The court: its surface and kitchens a faint tangerine, the lines a faint white.
    out.append(f'<path d="M{pts([at(0, 0), at(W, 0), at(W, L), at(0, L)])} Z" fill="{TANGERINE}" fill-opacity=".07"/>')
    out.append(f'<path d="M{pts([at(0, NET - K), at(W, NET - K), at(W, NET + K), at(0, NET + K)])} Z" fill="{TANGERINE}" fill-opacity=".07"/>')
    for a, b in [((0, 0), (W, 0)), ((0, L), (W, L)), ((0, 0), (0, L)), ((W, 0), (W, L)),
                 ((0, NET - K), (W, NET - K)), ((0, NET + K), (W, NET + K)),
                 ((W / 2, 0), (W / 2, NET - K)), ((W / 2, NET + K), (W / 2, L))]:
        (x1, y1), (x2, y2) = at(*a), at(*b)
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{LINE}" stroke-opacity=".28" stroke-width="2"/>')

    def flight(hit, end, top, peak, z0=.9, n=26):
        # From the hit (z0 m up) to the ground, highest (top m) at `peak` of the way: a drop peaks early.
        (hx, hy), (ex, ey) = hit, end
        for i in range(n + 1):
            s = i / n
            z = z0 + (top - z0) * (1 - ((peak - s) / peak) ** 2) if s < peak else top - top * ((s - peak) / (1 - peak)) ** 2
            yield hx + (ex - hx) * s, hy + (ey - hy) * s, z

    def ring(x, y, rad):
        ps = [at(x + rad * math.cos(a), y + rad * math.sin(a)) for a in [i / 24 * 2 * math.pi for i in range(24)]]
        return f'<path class="mark" d="M{pts(ps)} Z" fill="none" stroke="{BALL}" stroke-width="2.6"/>'

    # (hit, landing, highest point m, where it peaks, out, ring radius m)
    shots = shots or [((4.5, 1.25), (4.25, 8.6875), 1.8, .4, False, .3),  # the drop
                      ((3.0, .5), (4.0, 13.0), 1.6, .5, False, .22),      # the deep ball
                      ((3.0, 1.5), (.25, 14.25), 2.2, .5, True, .3)]      # the long one, out
    out.append('<g class="hero-shots">')
    for hit, end, top, peak, miss, rad in shots:
        dots = list(flight(hit, end, top, peak))
        for i, (x, y, z) in enumerate(dots):
            # Faint near you, fuller further away.
            s = min(max((y + 1.0) / (L + 2.5), 0), 1)
            px, py = at(x, y, z)
            out.append(f'<circle{' class="start"' if i == 0 else ''} cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{LIGHT_TANGERINE if miss else BALL}" fill-opacity="{.3 + .65 * s ** 1.3:.2f}"/>')
        if not miss:
            out.append(ring(*end, rad))
            continue
        # The x: an upright x turned (by at most 25 degrees, so it still reads as an x) so the flight comes in
        # between its arms, and as big as a ring would be there.
        (ax, ay), (bx, by) = at(*dots[-4]), at(*dots[-1])
        ang = math.atan2(by - ay, bx - ax)
        clear = lambda t: min(abs(math.remainder(ang - (math.pi / 4 + t + q * math.pi / 2), math.pi)) for q in (0, 1))
        turn = max((math.radians(v) for v in range(-25, 26)), key=clear)
        cx, cy = at(*end)
        half = math.dist(at(end[0] - rad, end[1]), at(end[0] + rad, end[1])) / 2
        k, w = half * .85, max(2.4, half * .2)
        arms = ' '.join(f'M{cx - k * math.cos(a):.1f} {cy - k * math.sin(a):.1f} L{cx + k * math.cos(a):.1f} {cy + k * math.sin(a):.1f}'
                        for a in (math.pi / 4 + turn, -math.pi / 4 + turn))
        out.append(f'<path class="mark" d="{arms}" stroke="{TANGERINE}" stroke-width="{w:.1f}" stroke-linecap="round"/>')
    out.append('</g>')
    # The net as it stands (posts, tape and mesh), last.
    P, H = .15, .914
    out.append(f'<path d="M{pts([at(-P, NET), at(-P, NET, H), at(W + P, NET, H), at(W + P, NET)])} Z" fill="{LINE}" fill-opacity=".06" '
               f'stroke="{LINE}" stroke-opacity=".4" stroke-width="2.5" stroke-linejoin="round"/>')
    # Laid out in a 1200 x 700 frame; the picture reaches well past it on every side (centred on the same
    # point), so on a wide screen the court runs on to the edge instead of stopping at the frame's.
    return (f'<svg class="court-lines hero-court" viewBox="-700 -250 2600 1200" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
            f'{"".join(out)}</svg>')


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
