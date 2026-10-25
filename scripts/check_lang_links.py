"""Checks that every link on the site keeps the visitor's language.

Each page lives under /en/ or /ja/. A link from a page in one language must open a page in the same language,
except the language switchers, which are marked with hreflang or data-lang-switch / data-lang-toggle.
Run from the repository root before committing a new page or new links:

    python3 scripts/check_lang_links.py

Exits with status 1 and lists the offending links if any link changes the language.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

LANGS = ('en', 'ja')
ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://quests.it.com'


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        a = dict(attrs)
        if 'href' not in a:
            return
        switcher = 'hreflang' in a or 'data-lang-switch' in a or 'data-lang-toggle' in a
        self.links.append((a['href'], switcher, self.getpos()[0]))


def pages():
    for lang in LANGS:
        for path in sorted((ROOT / lang).rglob('index.html')):
            url = '/' + path.parent.relative_to(ROOT).as_posix() + '/'
            yield lang, url, path


def main():
    problems = []
    checked = 0
    for lang, url, path in pages():
        parser = Links()
        parser.feed(path.read_text(encoding='utf-8'))
        for href, switcher, line in parser.links:
            target = urlparse(urljoin(SITE + url, href))
            if target.netloc != urlparse(SITE).netloc or switcher or href.startswith('#'):
                continue
            checked += 1
            first = target.path.strip('/').split('/')[0]
            if first != lang:
                problems.append(f'{path.relative_to(ROOT)}:{line}  {href}  ->  {target.path} (page is /{lang}/)')
    if problems:
        print('Links that change the language:')
        print('\n'.join('  ' + p for p in problems))
        sys.exit(1)
    print(f'OK: {checked} internal links keep the language.')


if __name__ == '__main__':
    main()
