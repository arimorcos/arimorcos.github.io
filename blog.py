__author__ = 'arimorcos'

from initialize import app, freezer, flatpages
from views import *

if __name__ == "__main__":
    # run on the local host so that anyone can see it
    app.run(host='0.0.0.0', port=4040, debug=True)
    # freezer.run(debug=False)