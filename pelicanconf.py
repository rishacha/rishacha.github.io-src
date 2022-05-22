#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import sys
# sys.path.append('./plugins')

from functools import partial
from datetime import datetime


# Metadata
AUTHOR = 'Rishabh Chakrabarti'
SITENAME = "Rishacha's Blog"
SITEURL = 'https://rishacha.github.io'
SITETITLE = "Rishabh Chakrabarti"
SITESUBTITLE = "Developer searching for excitement"
SITEDESCRIPTION = "Developer searching for excitement"
SITELOGO = '/media/rctest.jpg'
FAVICON = '/media/favicon.ico'

# Styling
BROWSER_COLOR = "#333333"
# PYGMENTS_STYLE = "monokai"

PATH = 'content'
STATIC_PATHS = ["media" 
# ,"extra/ads.txt"
# ,"extra/CNAME"
]

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

THEME = "themes/flex-rc"

# Blogroll
LINKS = (('Projects', '/projects'),
         ('Thoughts', '/thoughts'),
         ('About Me', '/me'))

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = False

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

"""def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True),

    'sidebar':sidebar
        }  # reversed for descending order
"""
MARKUP = ('md', 'ipynb')
IPYNB_MARKUP_USE_FIRST_CELL = True
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["pelican_jupyter.markup","render_math"]

IPYNB_EXPORT_TEMPLATE = 'ipynb_template/sample.tpl'
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = True
IPYNB_COLORSCHEME='colorful'
# LIQUID_CONFIGS = (("IPYNB_EXPORT_TEMPLATE", "ipynb_template/sample.tpl", ""), )

IGNORE_FILES = [".ipynb_checkpoints"]