#!/usr/bin/python3
"""
    function that queries the Reddit API and prints the titles of the first 10
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'URL'}
    response = requests.get(URL, headers=headers)
    if response.status_code == 404:
        print("None")
        return 0
    post = response.json().get('data')
    children = post.get('children')
    for posts in children:
        print(posts.get('data').get('title'))
