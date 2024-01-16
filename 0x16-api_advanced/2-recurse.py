#!/usr/bin/python3

"""Recursive function that querries the Reddit API and returns a
list containing titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list of titles for all hot
    articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.
        after (str): Parameter for pagination to get the next page of results.

    Returns:
        list: A list containing the titles of all hot articles in the
    subreddit.
    Returns None if no results are found.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        if children:
            for post in children:
                title = post['data'].get('title', '')
                hot_list.append(title)

            if data.get('after'):
                return recurse(subreddit, hot_list, data['after'])
            else:
                return hot_list
        else:
            return None
    else:
        return None
