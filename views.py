__author__ = 'arimorcos'

from flask import redirect, url_for, send_from_directory
from initialize import freezer, app
from helperFunctions import *
import os
from settings import FLATPAGES_ROOT, TEST_DIR

# redirect empty blog page to page 1
@app.route('/blog/')
def blogNoPage():
    return redirect('/blog/page/1/')


# redirect empty tag to page 1
@app.route('/blog/tag/<tagName>/', strict_slashes=False)
def tagNoPage(tagName):
    return redirect(url_for('blogTag', tagName=tagName, pageNum=1))


@freezer.register_generator
def tagNoPage():
    tagList = getTagFrequency(False)
    for tag in tagList:
        yield {'tagName': tag}


# create route for posts, which will grab all posts in the posts folder and render them in a template
@app.route("/blog/page/<pageNum>/")  # route to <webpage>/posts/
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
@app.route("/blog/tag/<tagName>/page/<pageNum>/")
def blogTag(tagName, pageNum):

    # find posts which match tag
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

# create a route for an individual test post
@app.route('/testPost/')  # route with the post name
def testPost():
    # generate the path with the first argument inside the first brackets, and the second argument inside the second
    # set of brackets

    path = '{}/{}'.format(TEST_DIR, os.path.splitext(
                                    os.listdir(
                                    os.path.join(FLATPAGES_ROOT,TEST_DIR))[0])[0])

    # raise

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

# route to sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('', 'sitemap.xml')

