__author__ = 'arimorcos'

import sys, os
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'blogPosts'

app = Flask(__name__)  # initialize app
flatpages = FlatPages(app)  # initialize flatpages
freezer = Freezer(app)  # initialize frozen
app.config.from_object(__name__)  # grab configuration file

# create route for posts, which will grab all posts in the posts folder and render them in a template
@app.route("/blog/page<blogPage>/")  # route to <webpage>/posts/
def blog(blogPage):

    # Number of posts per page
    nPostsPerPage = 4

    # get list of all pages which come from the post directory within the flatpages root
    postlist = [p for p in flatpages if p.path.startswith(POST_DIR)]

    # sort each post according to the date
    postlist.sort(key=lambda item:item['date'], reverse=True)

    # slice to the correct post subset
    startPost = (int(blogPage)-1) * nPostsPerPage
    stopPost = int(blogPage) * nPostsPerPage
    postSubset = postlist[startPost:stopPost]

    # generate booleans for whether there should be a new or old posts button
    if len(postlist) > nPostsPerPage and nPostsPerPage*int(blogPage) <= len(postlist):
        shouldOlder = True
    else:
        shouldOlder = False

    if int(blogPage) > 1:
        shouldNewer = True
    else:
        shouldNewer = False

    # return the posts rendered by the posts.html template
    return render_template('posts.html', posts=postSubset, olderpage=str(int(blogPage)+1),
                           newerpage=str(int(blogPage)-1), shouldNewer=shouldNewer, shouldOlder=shouldOlder)


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
        app.run(host='0.0.0.0', debug=True)