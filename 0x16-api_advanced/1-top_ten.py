#!/usr/bin/python3
"""
Has the `top_ten(subreddit)` function.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    header = {'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    req = requests.get(url, headers=header, allow_redirects=False, timeout=10)
    if req.status_code != 200:
        print('None')
    else:
        count = 0
        resp = req.json()['data']['children']
        for post in resp:
            if count >= 10:
                break
            print(post['data']['title'])
            count += 1
