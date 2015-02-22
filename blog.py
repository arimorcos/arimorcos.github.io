__author__ = 'arimorcos'

import sys, os
from flask import Flask, render_template, redirect
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


# redirect empty blog page to page 1
@app.route('/blog/')
def blognopage():
    return redirect('/blog/page1/')


# redirect empty tag to page 1
@app.route('/blog/tag/<tagname>/')
def tagnopage(tagname):
    return redirect('/blog/tag/' + tagname + '/page1/')


# create route for posts, which will grab all posts in the posts folder and render them in a template
@app.route("/blog/page<pagenum>/")  # route to <webpage>/posts/
def blog(pagenum):

    postlist = get_post_list()

    post_view = render_postlist(postlist, pagenum)

    return post_view


# create a route for tags, which will grab all posts which match a tag and render
@app.route("/blog/tag/<tagname>/page<pagenum>/")
def blog_tag(tagname, pagenum):

    # find posts which match tag
    postlist = find_tag_match(tagname)

    post_view = render_postlist(postlist, pagenum)

    return post_view


def render_postlist(postlist, pagenum):

    # Number of posts per page
    nPostsPerPage = 2

    # slice to the correct post subset
    startPost = (int(pagenum)-1) * nPostsPerPage
    stopPost = max(len(postlist) - 1, int(pagenum) * nPostsPerPage)
    postSubset = postlist[startPost:stopPost]

    # generate booleans for whether there should be a new or old posts button
    if len(postlist) > nPostsPerPage and nPostsPerPage*int(pagenum) <= len(postlist):
        shouldOlder = True
    else:
        shouldOlder = False

    if int(pagenum) > 1:
        shouldNewer = True
    else:
        shouldNewer = False

    # return the posts rendered by the posts.html template
    return render_template('posts.html', posts=postSubset, olderpage=str(int(pagenum)+1),
                           newerpage=str(int(pagenum)-1), shouldNewer=shouldNewer, shouldOlder=shouldOlder)


def get_post_list():
    # get list of all pages which come from the post directory within the flatpages root
    postlist = [p for p in flatpages if p.path.startswith(POST_DIR)]

    # sort each post according to the date
    postlist.sort(key=lambda item:item['date'], reverse=True)

    # return
    return postlist


def find_tag_match(tagName):
    """
    Finds posts which match a given tag, case-insensitive
    :param tagName: string containing tag to match
    :return: postlist
    """

    postlist = get_post_list()

    matchTag = []
    for p in postlist:

        if any(tag.lower() == tagName for tag in p['tags'].replace(' ', '').split(',')):
            matchTag.append(p)

    return matchTag


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