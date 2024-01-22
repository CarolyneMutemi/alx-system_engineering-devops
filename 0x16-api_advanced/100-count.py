#!/usr/bin/python3
"""
Has count_words function.
"""

import requests


def count_words(subreddit, word_list=[], titles=[], after=None):
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
        word_dict = get_word_count(word_list, titles)
        print_count(word_dict)
        return

    return count_words(subreddit, word_list, titles, after)


def get_data(lis):
    """
    Get titles from the given post data.
    """
    data = []
    for post in lis:
        data.append(post['data']['title'])
    return data


def get_word_count(word_list=[], title_list=[]):
    """
    Gets the number of occurences of the words
    from the titles list.
    """
    return_dict = {}
    for title in title_list:
        title_words = [titly.lower() for titly in title.split()]
        for word in word_list:
            if word.lower() in title_words:
                if word not in return_dict:
                    return_dict[word] = title_words.count(word.lower())
                else:
                    return_dict[word] += title_words.count(word.lower())
    return return_dict


def print_count(dic):
    """
    Fulfill the given requirements about printing the result.
    """
    sort_dic = dict(sorted(dic.items(), key=lambda elem: elem[0]))
    sorted_dic = dict(sorted(sort_dic.items(), key=lambda elem: elem[1], reverse=True))
    for key, value in sorted_dic.items():
        print(f"{key}: {value}")
