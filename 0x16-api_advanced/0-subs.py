#!/usr/bin/python3
import requests
""" queries the Reddit API and returns the
    number of subscribers (not active users,
    total subscribers) for a given subreddit """


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users,
        total subscribers) for a given subreddit. If an invalid
        subreddit is given, the function should return 0. """
    
    reddit_api = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "My User Agent Request"}

    try:
        api_url = requests.get(reddit_api, headers=headers).json()
        return api_url.get("data").get("subscribers")
    except:
        return 0
