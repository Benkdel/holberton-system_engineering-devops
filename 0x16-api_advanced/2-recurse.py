#!/usr/bin/python3
"""
    Recursively get all HOT posts in subreddit
"""

import requests


def recurse(subreddit, hot_list=[], page=''):
    """
        returns a list of the top 10 hot posts in
        a given subreddit
        args
        subreddit: sub to look for
        hot_list: list of titles
        page: to look next page
    """
    userAgent = 'Python.wsl2.windows.ApiProject:v1 (by Dry-Improvement-3814)'

    _headers = {
        'User-Agent': userAgent
    }

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    if subreddit is None or type(subreddit) is not str:
        if (len(hot_list) == 0):
            return None
        return hot_list

    if page != '':
        _params = {
            'after': page
        }
    else:
        _params = {}

    with requests.get(url, headers=_headers, params=_params) as response:
        titles = response.json()
        if response.status_code == 200:
            ch = titles.get('data').get('children')
            if ch is None or (len(ch) > 0 and ch[0].get('kind') != 't3'):
                print(None)
            else:
                hot_list += list(map(lambda elm: elm.get('data').get('title'), ch))
            _page = titles.get('data').get('after')

    if _page is None or _page == 'null':
        return (hot_list)
    else:
        return recurse(subreddit, hot_list, _page)
