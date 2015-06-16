__author__ = 'arimorcos'


from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)  # initialize app
app.config.from_pyfile('settings.py')  # grab configuration file
flatpages = FlatPages(app)  # initialize flatpages
flatpages.reload()
freezer = Freezer(app)  # initialize frozen

