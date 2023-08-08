#!/usr/bin/python3
import requests
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """

    reddit_api = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        api_url = requests.get(reddit_api, headers=headers).json()
        posts = api_url.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    except BaseException:
        print(None)
