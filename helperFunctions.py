__author__ = 'arimorcos'

from flask import render_template
from initialize import flatpages
from settings import POST_DIR


def renderPostList(postList, pageNum=False, tagName=False):

    # Number of posts per page
    nPostsPerPage = 5
    nRecent = 5

    # get recent posts
    allPosts = getPostList()
    recentPosts = allPosts[:nRecent]

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
