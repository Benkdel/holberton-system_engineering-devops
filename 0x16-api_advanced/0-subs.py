#!usr/bin/python3
"""
    Get number of subscribers
"""


import requests

userAgent = 'Python.wsl2.windows.ApiProject:v1 (by Dry-Improvement-3814)'


def number_of_subscribers(subreddit):
    """
        Returns number of subscribers for given subredit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)

    _headers = {'User-Agent': userAgent}

    with requests.get(url, headers=_headers) as response:
        subscribers = response.json().get('data', {}).get("subscribers", 0)
        return int(subscribers)
