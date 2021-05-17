#!/usr/bin/python3
"""function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Function that return the numbers of subcribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'URL'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    data = response.json().get('data')
    subs = data.get('subscribers')
    return subs
