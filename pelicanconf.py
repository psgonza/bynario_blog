#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'psgonza'
SITENAME = u'Bynario'
SITESUBTITLE = u'Geek as a platform'
SITEURL = 'https://bynario.com'

#PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "all_atom.xml"
FEED_RSS = "rss.xml" 
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

#Bynario
SUMMARY_MAX_LENGTH = None
THEME = 'pelican-octopress-theme'
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.literal','better_codeblock_line_numbering']

MD_EXTENSIONS  = [
   'extra',
   'codehilite(linenums=False,css_class=prettyprint,guess_lang=True,use_pygments=True)'
]

DISQUS_SITENAME = "bynario"
GOOGLE_ANALYTICS = "UA-90925-1"
TWITTER_USER = "psgonza"
GITHUB_USER = "psgonza"
GITHUB_SHOW_USER_LINK = True
GITHUB_REPO_COUNT = 5
SIDEBAR_IMAGE = "https://dl.dropboxusercontent.com/u/14814182/blog/roundPic.gif"
SEARCH_BOX = True
DISPLAY_FEEDS_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'), ('Posts', '/category/posts.html'), ('RSS','/rss.xml')]
DEFAULT_CATEGORY = "Posts"
