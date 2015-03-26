title: Clustering subreddits by common word usage
date: 2015-03-26
tags: reddit, pca, clustering, affinity propagation, euclideandistance
image: '/static/blogImages/201503/static3dClusters.png'

What defines a subreddit? There are some obvious answers: topic, content type (images, videos, self-posts, or all of the above), and user population. For example, by topic, one might expect subreddits related to video games to be more similar to one another than any of them are to [/r/politics](http://www.reddit.com/r/politics). By content type, it seems reasonable to assume that self-post only subreddits like [/r/AskHistorians](http://reddit.com/r/askhistorians) and /r/[AskScience](http://www.reddit.com/r/askscience) are more similar to one another than either is [/r/AdviceAnimals](http://www.reddit.com/r/adviceanimals). But are there more subtle differences between subreddits that can be used to group them in meaningful ways as well? Do users of the different subreddits write in distinct, predictable fashion? Let's find out. 

<div id="breakStart"></div>

## Creating subreddit-specific word frequency distributions ##

To answer the question of whether users in different subreddits write in distinguishable ways, I wanted to analyze the frequency of words used in the comments of each subreddit. Choosing the right number of words to analyze is a bit of a balance. Choose too few words (the, a(n), etc.), and the subreddits will be entirely indistinguishable. Choose too many, and you'll quickly start getting subreddit specific words, such as names, which will trivialize the problem (e.g. "Clinton" is much more likely to appear in a politics related subreddits, while "Bioshock" is much more likely to appear in video game subreddits). For these analyses, I chose to use the 100 words most frequently used across the comments of the top 50 subreddits. This list includes common articles, a lot of pronouns, and a lot of basic verbs. However, there are no words which should be definitely linked to a given subreddit. For example, the 98th, 99th, and 100th words are "going," "want," and "didn't," respectively. You can see a complete list of the words [here](/static/blogImages/201503/100_MostFreqWords.png). Thus, the distribution of these words should provide an intuition into how users write while remaining agnostic to the "jargon" of each subreddit.  

With these words in hand, I analyzed the comments submitted to the 50 most popular subreddits between March 2 and March 8, 2015. If you're interested in how I acquired this dataset, check out this [post](http://www.arimorcos.com/blog/Creating%20a%20Reddit%20Dataset/). To create word frequency distributions for each subreddit, I simply counted the number of occurrences (case-insensitive) of each of the 100 words, and normalized by the total number of words in each subreddit. This normalization step is key, because otherwise, subreddits with longer comments (such as [/r/AskReddit](http://reddit.com/r/askreddit)) will clearly separate from all the other subreddits). 

## A subreddit distance matrix ##

As a first pass analysis on these data, I calculated the euclidean distance between the 100-dimensional normalized word distributions for each pair of subreddits, resulting in the following matrix: 

<img src='/static/blogImages/201503/distMat.png' width=80% class="centeredImage"></img>

Each point in the matrix represents the comparison between two subreddits. Cooler colors signify more similar subreddits, hotter colors subreddits that are more different. Elements along the diagonal represent a comparison of a subreddit to itself, so the distance is 0. Also note that there's no directionality to these comparisons so the matrix is symmetric. 

A few observations pop out immediately. First, there are a few bastions of blue off the diagonal. In a lot of ways, these make intuitive sense. [/r/funny](http://www.reddit.com/r/funny), [/r/pics](http://www.reddit.com/r/pics), [/r/gifs](http://www.reddit.com/r/gifs), [/r/WTF](http://www.reddit.com/r/WTF), and [/r/videos](http://www.reddit.com/r/videos) are all pretty similar to one another. All of these subreddits link to content as opposed to self-posts, they all are or once were default subreddits, and none of them are known for "serious" conversation. 

Second, [/r/circlejerk](http://www.reddit.com/r/circlejerk) is different from every other subreddit. Third, the sports subreddits ([/r/nba](http://www.reddit.com/r/nba), [/r/nfl](http://www.reddit.com/r/nfl), [/r/SquaredCircle](http://www.reddit.com/r/SquaredCircle), and [/r/soccer](http://www.reddit.com/r/soccer)) are all pretty similar as are the variety of video game subreddits. 

## Clustering subreddits ##

While quite informative, the distance matrix is a little hard to quickly grasp some of the effects. It would be substantially more intuitive to plot the subreddits such that there location described their similarity. Unfortunately, we've yet to find a great way to visualize a 100-dimensional space, so I used [principal components analysis (PCA)](http://en.wikipedia.org/wiki/Principal_component_analysis), one of the most basic forms of dimensionality reduction, to allow us to better visualize the data. There's quite a bit of structure in the data, as the first three principal components explain more than 50% of the total variance, and the first 15 explain more than 90%.

<img src='/static/blogImages/201503/pcVarExp.png' width=50% class="centeredImage"></img>

I then used [affinity propagation](http://en.wikipedia.org/wiki/Affinity_propagation), a clustering algorithm based on message passing, to cluster the data in the first 3 principal components. One really nice feature of affinity propagation is that, as opposed to k-means clustering, it doesn't require you to estimate the number of clusters beforehand. The algorithm clustered the data into 7 clusters, as displayed in three dimensions below.

<img src='/static/blogImages/201503/pca3d.gif' width=60% class="centeredImage"></img>

<div id="breakEnd"></div>