#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Craig J Perry'
SITENAME = u"Craig's Notebook"
SITEURL = 'http://www.craigjperry.com'

PATH = 'content'
OUTPUT_PATH = 'appengine/blog'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ('GitHub', 'https://github.com/CraigJPerry'),
)

SOCIAL = (
    ('Twitter', 'https://twitter.com/CraigJPerry'),
)

DEFAULT_PAGINATION = False

RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(linenums=False)']

THEME = 'themes/svbhack'
USER_LOGO_URL = '/img/me-small.jpg'
TAGLINE = "Unix systems administrator. Python / Java / Web developer."
