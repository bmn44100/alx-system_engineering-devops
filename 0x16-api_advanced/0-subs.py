#!/usr/bin/python3
import requests
""" queries the Reddit API and returns the
    number of subscribers (not active users,
    total subscribers) for a given subreddit """


def number_of_subscribers(subreddit):
    """ returns the number of subscribers (not active users,
        total subscribers) for a given subreddit. If an invalid
        subreddit is given, the function should return 0. """

    reddit_api = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    api_data = requests.get(
        '{}{}/about'.format(
            reddit_api, subreddit), headers=headers, allow_redirects=False)

    if api_data.status_code != 200:
        return 0

    subreddit_data = api_data.json()

    return subreddit_data['data']['subscribers']
