#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Rishabh Chakrabarti'
SITENAME = "Rishacha's Blog"
SITEURL = ''
SITETITLE = "Rishabh Chakrabarti"
SITESUBTITLE = "Always Be Coding"
SITEDESCRIPTION = "Developer searching for excitement"
SITELOGO = 'images/rctest.jpg'
FAVICON = 'images/favicon.ico'

BROWSER_COLOR = "#333333"
# PYGMENTS_STYLE = "monokai"

PATH = 'content'
STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'
I18N_TEMPLATES_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = False

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', )

from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid]

# IPYNB_EXPORT_TEMPLATE = 'ipynb_template/sample.tpl'
# IPYNB_FIX_CSS = False
# IPYNB_SKIP_CSS = True
LIQUID_CONFIGS = (("IPYNB_EXPORT_TEMPLATE", "ipynb_template/sample.tpl", ""), )

IGNORE_FILES = [".ipynb_checkpoints"]