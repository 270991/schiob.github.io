#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Santiago Chio'
SITENAME = u'schiob'
SITESUBTITLE = u'A space to write about my work and interests.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Monterrey'

DEFAULT_LANG = 'en'

# Bootstrap theme
THEME = "/home/chio/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'flatly'

# Header
ABOUT_ME = "I build things with Python!"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/schiob'),
          ('Facebook', 'https://facebook.com/schiob'),
          ('Twitter', 'https://twitter.com/schiob'),
          ('Google+', 'https://plus.google.com/u/0/+SantiagoChío'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
