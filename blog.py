__author__ = 'arimorcos'

import sys, os
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)  # initialize app
flatpages = FlatPages(app)  # initialize flatpages
freezer = Freezer(app)  # initialize frozen
app.config.from_object(__name__)  # grab configuration file

# create route for posts, which will grab all posts in the posts folder and render them in a template
@app.route("/posts/")  # route to <webpage>/posts/
def posts():
    # get list of all pages which come from the post directory within the flatpages root
    postlist = [p for p in flatpages if p.path.startswith(POST_DIR)]
    # sort each post according to the date
    postlist.sort(key=lambda item:item['date'], reverse=False)
    # return the posts rendered by the posts.html template
    return render_template('posts.html', posts=postlist)


# create a route for an individual post
@app.route('/posts/<name>/')  # route with the post name
def post(name):
    # generate the path with the first argument inside the first brackets, and the second argument inside the second
    # set of brackets
    path = '{}/{}'.format(POST_DIR, name)

    # return the page object that exists at that path, or return 404 if it doesn't exist
    post = flatpages.get_or_404(path)

    # return the requested post rendered through the post template
    return render_template('post.html', post=post)

# create router for general web pages
@app.route('/<page>/')
def webpage(page):
    return render_template('{}.html'.format(page))

# Add url generator
@freezer.register_generator
def pages():
    path = app.root_path
    pages = next(os.walk(path))[2]
    for page in pages:
        yield {"page": page}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        # run on the local host so that anyone can see it
        app.run(host='0.0.0.0', debug=True)