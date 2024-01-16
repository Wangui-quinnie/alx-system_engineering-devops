#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number
of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 for invalid
    subreddits or errors.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
