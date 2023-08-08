#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a
sorted count of given keywords
"""


import requests


def count_words(subreddit, word_list):
    """
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    reddit_api = "https://api.reddit.com/r/{}/hot".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        api_url = requests.get(reddit_api, headers=headers).json()
        after = api_url.get("data").get("after")
        if after:
            reddit_api = reddit_api + "?after={}".format(after)
        articles = api_url.get("data").get("children")
        for article in articles:
            article.append(article.get("data").get("title"))
        after = api_url.get("data").get("after")
        if after is None:
            return count
        return count_words(subreddit, word_list)
    except BaseException:
        return None
