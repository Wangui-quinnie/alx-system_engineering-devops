#!/usr/bin/python3
""" Functin that prints the titles of the first 10 hot posts for a
given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
