#!/usr/bin/env python3
"""Builds the home page in each language from one bilingual template.

    python3 build/make.py   →  index.html (English, /) and uk/index.html (Ukrainian, /uk/)

The template (build/home.tpl.html) carries both languages: every piece of copy is an element with
data-l="en" or data-l="uk". Each page keeps only its own language, so search engines index two clean
pages linked by hreflang. Edit the template, never the generated pages, then run this script.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://falamos.app'
VOID = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'use', 'wbr'}

PAGES = {
    'en': {
        'path': '/',
        'out': ROOT / 'index.html',
        'title': 'Falamos — European Portuguese for people who moved',
        'description': 'Falamos is an app for learning European Portuguese (pt-PT) for people who moved to '
                       'Portugal: letters from Finanças, renting, the doctor and the A2 exam. On the App '
                       'Store, soon on Google Play.',
        'og_description': 'Letters from Finanças, renting, the doctor, the A2 exam. Only the Portuguese of Portugal.',
        'og_alt': 'A yellow tram at night between stops signed «Olá!» and «Bom dia!»',
        'locale': 'en_GB',
        'nav': 'Language',
    },
    'uk': {
        'path': '/uk/',
        'out': ROOT / 'uk' / 'index.html',
        'title': 'Falamos — європейська португальська для тих, хто переїхав',
        'description': 'Falamos — застосунок для вивчення європейської португальської (pt-PT) для тих, хто '
                       'переїхав до Португалії: листи з Finanças, оренда, лікар, іспит A2. В App Store, '
                       'скоро в Google Play.',
        'og_description': 'Листи з Finanças, оренда, лікар, іспит A2. Лише португальська Португалії.',
        'og_alt': 'Жовтий трамвай уночі між зупинками «Olá!» і «Bom dia!»',
        'locale': 'uk_UA',
        'nav': 'Мова',
    },
}


def esc(text):
    return text.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def keep_language(html, lang):
    """Drops every element whose data-l names another language (with everything inside it)."""
    tag = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)\b([^>]*?)(/?)>')
    out, pos, skip, depth = [], 0, None, 0
    for m in tag.finditer(html):
        closing, name, attrs, selfclose = m.group(1), m.group(2).lower(), m.group(3), m.group(4)
        if skip is None:
            other = re.search(r'\sdata-l="([a-z]+)"', attrs)
            if not closing and other and other.group(1) != lang:
                out.append(html[pos:m.start()])
                if name in VOID or selfclose:
                    pos = m.end()
                else:
                    skip, depth = name, 1
            continue
        if name == skip:
            depth += -1 if closing else (0 if selfclose else 1)
            if depth == 0:
                skip, pos = None, m.end()
    out.append(html[pos:])
    return ''.join(out).replace(' data-l="' + lang + '"', '')


def strip_tags(fragment):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', fragment)).strip()


def faq_pairs(html):
    """The visible questions and answers, so the FAQ markup always says exactly what the page says."""
    items = re.findall(r'<summary>(.*?)</summary>\s*<p class="faq-a">(.*?)</p>', html, re.S)
    return [(strip_tags(q), strip_tags(a)) for q, a in items]


def head(lang, faq):
    p = PAGES[lang]
    url = SITE + p['path']
    alternates = '\n'.join(
        f'<link rel="alternate" hreflang="{code}" href="{SITE + PAGES[code]["path"]}">' for code in PAGES
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    other_locales = '\n'.join(
        f'<meta property="og:locale:alternate" content="{PAGES[code]["locale"]}">' for code in PAGES if code != lang
    )
    org = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'Falamos', 'url': SITE + '/',
           'logo': SITE + '/assets/icons/icon-192.png', 'email': 'support@falamos.app'}
    ld = {'@context': 'https://schema.org', '@graph': [
        org,
        {'@type': 'WebSite', '@id': url + '#site', 'name': 'Falamos', 'url': url, 'inLanguage': lang,
         'description': p['description'], 'publisher': {'@id': SITE + '/#org'}},
        # iOS only until Google Play is live; no offers or rating: nothing here may claim more than the page.
        {'@type': 'MobileApplication', 'name': 'Falamos', 'operatingSystem': 'iOS',
         'url': SITE + '/', 'installUrl': 'https://apps.apple.com/app/id6826639944', 'sameAs': 'https://apps.apple.com/app/id6826639944',
         'applicationCategory': 'EducationalApplication', 'inLanguage': ['en', 'uk'],
         'description': p['description'], 'publisher': {'@id': SITE + '/#org'},
         'about': {'@type': 'Language', 'name': 'European Portuguese', 'alternateName': 'pt-PT'}},
        {'@type': 'FAQPage', 'inLanguage': lang, 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]},
    ]}
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{esc(p['description'])}">
<meta name="theme-color" content="#FFCC1A" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1E1D1A" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/icons/favicon-32.png" sizes="32x32">
<link rel="icon" href="/assets/icons/icon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
<link rel="canonical" href="{url}">
{alternates}
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['og_description'])}">
<meta property="og:image" content="{SITE}/assets/media/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(p['og_alt'])}">
<meta property="og:site_name" content="Falamos">
<meta property="og:locale" content="{p['locale']}">
{other_locales}
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'''


def lang_nav(lang):
    links = ''.join(
        f'<a href="{PAGES[code]["path"]}" hreflang="{code}" lang="{code}"'
        + (' aria-current="page"' if code == lang else '') + f'>{"UA" if code == "uk" else code.upper()}</a>'
        for code in PAGES
    )
    return f'<nav class="lang" aria-label="{PAGES[lang]["nav"]}">{links}</nav>'


def main():
    template = (ROOT / 'build' / 'home.tpl.html').read_text()
    # The template's own <head> lines that the generated block replaces.
    template = re.sub(r'<meta charset="utf-8">\n<meta name="viewport"[^\n]*\n', '', template)
    for lang, p in PAGES.items():
        body = keep_language(template.replace('{{lang}}', lang).replace('{{langnav}}', lang_nav(lang)), lang)
        html = body.replace('{{head}}', head(lang, faq_pairs(body)))
        assert 'data-l=' not in html and '{{' not in html, lang
        p['out'].parent.mkdir(parents=True, exist_ok=True)
        p['out'].write_text(html)
        print('wrote', p['out'].relative_to(ROOT))


if __name__ == '__main__':
    main()
