#!/usr/bin/python3

"""
Script with `number_of_subscribers(subreddit)` function.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    header = {'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    req = requests.get(url, headers=header, timeout=10, allow_redirects=False)
    if req.status_code != 200:
        return 0

    response = req.json()

    return response['data'].get('subscribers', 0)
