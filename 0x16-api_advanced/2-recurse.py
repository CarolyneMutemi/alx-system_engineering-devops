#!/usr/bin/python3
"""
Has recurse function.
"""

import requests


def recurse(subreddit, titles=[], after=None):
    """
    The recursive function.
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    header = {'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    resp = {}
    if not titles:
        req = requests.get(url, headers=header,
                           allow_redirects=False, timeout=10)
        if req.status_code != 200:
            return None
        resp = req.json()['data']
        after = resp['after']
    else:
        req = requests.get(url, params={'after': after}, headers=header,
                           allow_redirects=False, timeout=10)
        resp = req.json()['data']
        after = resp['after']
    titles += get_data(resp['children'])

    if not after:
        return titles

    return recurse(subreddit, titles, after)


def get_data(lis):
    """
    Get titles from the given post data.
    """
    data = []
    for post in lis:
        data.append(post['data']['title'])
    return data
