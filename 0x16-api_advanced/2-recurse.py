#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API and 
    returns a list containing the titles of all hot
    articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None
    """

    reddit_api = "https://api.reddit.com/r/{}/hot?after={}".format(
        subreddit, after)
    headers = {"User-Agent": "My User Agent Request"}
    try:
        api_url = requests.get(reddit_api, headers=headers).json()
        posts = api_url.get("data").get("children")
        for post in posts:
            hot_list.append(post.get("data").get("title"))
        after = api_url.get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except BaseException:
        return None
