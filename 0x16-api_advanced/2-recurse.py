#!/usr/bin/python3
"""
    Recursively get all HOT posts in subreddit
"""
import requests


def recurse(subreddit, hot_list=[], page=''):
    """ returns a list of hot posts in given subreddit """
    userAgent = 'Python.wsl2.windows.ApiProject:v1 (by Dry-Improvement-3814)'

    _headers = {
        'User-Agent': userAgent
    }

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    _params = {
        'after': page
    }

    if page is None:
        if (len(hot_list) == 0):
            return None
        return hot_list

    with requests.get(url, headers=_headers, params=_params) as response:
        if response.status_code == 200:
            res = response.json()
            _page = res.get('data').get('after')
            ch = res.get('data').get('children')
            for c in ch:
                    hot_list.append(c.get('data').get('title'))
            return recurse(subreddit, hot_list, _page)
        else:
            return None
