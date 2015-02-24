__author__ = 'arimorcos'

import sys
from flask import Flask, redirect
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from blogHelper import *

DEBUG = False
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'blogPosts'

app = Flask(__name__)  # initialize app
flatpages = FlatPages(app)  # initialize flatpages
freezer = Freezer(app)  # initialize frozen
app.config.from_object(__name__)  # grab configuration file


# redirect empty blog page to page 1
@app.route('/blog/')
def blogNoPage():
    return redirect('/blog/page1/')


# redirect empty tag to page 1
@app.route('/blog/tag/<tagName>/')
def tagNoPage(tagName):
    return redirect('/blog/tag/' + tagName + '/page1/')


# create route for posts, which will grab all posts in the posts folder and render them in a template
@app.route("/blog/page<pageNum>/")  # route to <webpage>/posts/
def blog(pageNum):

    postList = getPostList()

    postView = renderPostList(postList, pageNum)

    return postView


@app.route('/blog/all/')
def blogAll():

    postList = getPostList()
    postView = renderPostList(postList)
    return postView


# create a route for tags, which will grab all posts which match a tag and render
@app.route("/blog/tag/<tagName>/page<pageNum>/")
def blogTag(tagName, pageNum):

    postList = findTagMatch(tagName)

    postView = renderPostList(postList, pageNum, tagName)

    return postView


# create a route for an individual post
@app.route('/blog/<name>/')  # route with the post name
def blogPost(name):
    # generate the path with the first argument inside the first brackets, and the second argument inside the second
    # set of brackets
    path = '{}/{}'.format(POST_DIR, name)

    # return the page object that exists at that path, or return 404 if it doesn't exist
    post = flatpages.get_or_404(path)

    # return the requested post rendered through the post template
    return render_template('post.html', post=post)


# Routing
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/research/')
def research():
    return render_template('research.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


# route index to about page
@app.route('/')
def index():
    return render_template('about.html')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        # run on the local host so that anyone can see it
        app.run(host='0.0.0.0', debug=False)