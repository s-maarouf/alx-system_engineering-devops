#!/usr/bin/python3

"""A script that uses the Reddit API to print
    the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot
    posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
