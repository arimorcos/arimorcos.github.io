__author__ = 'arimorcos'

import sys, os
from flask import Flask, render_template, redirect
from flask_flatpages import FlatPages
from flask_frozen import Freezer

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
@app.route('/blog/tag/<tagname>/')
def tagNoPage(tagname):
    return redirect('/blog/tag/' + tagname + '/page1/')


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

    # find posts which match tag
    postList = findTagMatch(tagName)

    postView = renderPostList(postList, pageNum, tagName)

    return postView


def renderPostList(postList, pageNum=False, tagName=False):

    # Number of posts per page
    nPostsPerPage = 2

    # get recent posts
    nRecent = 10
    allPosts = getPostList()
    recentPosts = allPosts[:nRecent-1]

    if pageNum:

        # slice to the correct post subset
        startPost = (int(pageNum) - 1) * nPostsPerPage
        stopPost = max(len(postList) - 1, int(pageNum) * nPostsPerPage)
        postSubset = postList[startPost:stopPost]

        # generate booleans for whether there should be a new or old posts button
        if len(postList) > nPostsPerPage and nPostsPerPage*int(pageNum) <= len(postList):
            shouldOlder = True
            if tagName:
                olderPage = '/blog/tag/' + tagName + '/page' + str(int(pageNum)+1)
            else:
                olderPage = '/blog/page' + str(int(pageNum)+1)
        else:
            shouldOlder = False
            olderPage = False

        if int(pageNum) > 1:
            shouldNewer = True
            if tagName:
                newerPage = '/blog/tag/' + tagName + '/page' + str(int(pageNum)-1)
            else:
                newerPage = '/blog/page' + str(int(pageNum)-1)
        else:
            shouldNewer = False
            newerPage = False
    else:
        shouldNewer = False
        shouldOlder = False
        newerPage = False
        olderPage = False
        postSubset = postList

    tagFreq = getTagFrequency(True)
    for tag in tagFreq:
        tagFreq[tag] = 'tag{0}'.format(tagFreq[tag])

    # return the posts rendered by the posts.html template
    return render_template('posts.html', posts=postSubset, olderPage=olderPage,
                           newerPage=newerPage, shouldNewer=shouldNewer, shouldOlder=shouldOlder,
                           recentPosts=recentPosts, tagFreq=tagFreq)


def getPostList():
    # get list of all pages which come from the post directory within the flatpages root
    postList = [p for p in flatpages if p.path.startswith(POST_DIR)]

    # sort each post according to the date
    postList.sort(key=lambda item:item['date'], reverse=True)

    # return
    return postList


def findTagMatch(tagName):
    """
    Finds posts which match a given tag, case-insensitive
    :param tagName: string containing tag to match
    :return: postList
    """

    postList = getPostList()

    matchTag = []
    for p in postList:

        if any(tag.lower() == tagName for tag in p['tags'].replace(' ', '').split(',')):
            matchTag.append(p)

    return matchTag


def getTagFrequency(normalizeRange):
    """
    Finds the frequency of each tag
    normalizeRange: normalize the range of the tag frequencies
    :return: dict with key as tag and value being number of occurences
    """
    postList = getPostList()

    tagList = {}
    for p in postList:
        for tag in p['tags'].replace(' ', '').split(','):
            if tag in tagList:
                tagList[tag] += 1
            else:
                tagList[tag] = 1

    if normalizeRange:
        maxFreq = float(max(list(tagList[i] for i in tagList)))
        for tag in tagList:
            tagList[tag] = int(round(maxFreq*(float(tagList[tag])/maxFreq)))

    return tagList


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