#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# from mdx_emdash import EmDashExtension

AUTHOR = 'FunBotan'
SITENAME = 'Cyber Ape stories'
SITEURL = 'https://cyberape.space'

PATH = 'content'
STATIC_PATHS = ['content/posts', 'content/pages']
STATIC_EXCLUDES = ['plugins', 'theme', 'output']
PAGE_EXCLUDES = STATIC_EXCLUDES
ARTICLE_EXCLUDES = STATIC_EXCLUDES
ARTICLE_PATHS = ['content/posts']
PAGE_PATHS = ['content/pages']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'pelican-ert', 'render_math']
'''
MARKDOWN = {
    'extension_configs': {
        EmDashExtension(): {},
    }
}
'''

ERT_WPM = 200
ERT_FORMAT = '{time}'
ERT_INT = True

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
I18N_GETTEXT_NEWSTYLE = True
I18N_SUBSITES = {
    'ru': {
        'OUTPUT_PATH': 'output',
        'SITEURL': 'https://cyberape.space',
    },
    'en': {
        'OUTPUT_PATH': 'output/en',
        'TIMEZONE': 'Europe/London',
    },
}

# Feed generation is usually not desired when developing
#FEED_DOMAIN = 'http://rss.cyberape.space'
FEED_RSS = 'rss'
FEED_ATOM = 'atom'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", "CNAME", "_config.yml"]