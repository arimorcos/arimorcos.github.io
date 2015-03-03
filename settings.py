__author__ = 'arimorcos'

import os


APP_DIR = os.path.dirname(os.path.abspath(__file__))
FREEZER_DESTINATION = APP_DIR
FREEZER_REMOVE_EXTRA_FILES = False

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'blogPosts'