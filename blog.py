__author__ = 'arimorcos'

from initialize import app, freezer, flatpages
from views import *

if __name__ == "__main__":
    # run on the local host so that anyone can see it
    # app.run(host='0.0.0.0', debug=False)
    freezer.run(debug=True)