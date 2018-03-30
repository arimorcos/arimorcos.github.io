__author__ = 'arimorcos'

from flask import redirect, url_for, send_from_directory
from initialize import freezer, app
from helperFunctions import *
import os
from settings import FLATPAGES_ROOT, TEST_DIR
from bs4 import BeautifulSoup

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
@app.route('/blog/post/<name>/')  # route with the post name
def blogPost(name):
    # generate the path with the first argument inside the first brackets, and the second argument inside the second
    # set of brackets
    path = '{}/{}'.format(POST_DIR, name)

    # return the page object that exists at that path, or return 404 if it doesn't exist
    post = flatpages.get_or_404(path)

    # get description
    post.description = ''.join(BeautifulSoup(post.html[0:400], 'lxml').findAll(text=True)) + '...'
    post.url = 'http://www.arimorcos.com' + url_for('blogPost',name=name)

    # get tags
    post.tagList = [convertToCamelCase(tag) for tag in post.meta['tags'].replace(', ',',').split(',')]

    # return the requested post rendered through the post template
    return render_template('post.html', post=post)

# redirect old format
@app.route('/blog/<name>/')
def blogPostRedirect(name):
    # print "redirect to: " + url_for('blogPost', name=name)
    return redirect(url_for('blogPost', name=name), code=301)

@freezer.register_generator
def blogPostRedirect():
    postList = getPostList()
    for post in postList:
        yield {'name': post.path.split('/')[1]}

# create a route for an individual test post
@app.route('/testPost/')  # route with the post name
def testPost():
    # generate the path with the first argument inside the first brackets, and the second argument inside the second
    # set of brackets

    path = '{}/{}'.format(TEST_DIR, os.path.splitext(
                                    os.listdir(
                                    os.path.join(FLATPAGES_ROOT,TEST_DIR))[0])[0])

    # raise
    flatpages.reload()

    # return the page object that exists at that path, or return 404 if it doesn't exist
    post = flatpages.get_or_404(path)

    # return the requested post rendered through the post template
    return render_template('post.html', post=post)

# Routing
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/neuro_research/')
def neuroResearch():
    return render_template('neuro_research.html')


@app.route('/ml_research/')
def mlResearch():
    return render_template('ml_research.html')


@app.route('/publications/')
def publications():
    return render_template('publications.html')


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

