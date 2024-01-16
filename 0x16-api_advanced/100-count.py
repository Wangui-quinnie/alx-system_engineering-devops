#!/usr/bin/python3

"""recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively query the Reddit API, parse titles of hot articles, and
    print sorted counts of keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Parameter for pagination to get the next page of results.
        counts (dict): Dictionary to store the counts of keywords.

    Returns:
        None
    """
    if counts is None:
        counts = {}

    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {'User-Agent': 'MyRedditBot/1.0 (by YourUsername)'}

    # Make a request to the Reddit API to get the hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract post titles
        data = response.json().get('data', {})
        children = data.get('children', [])

        if children:
            for post in children:
                title = post['data'].get('title', '')
                # Count occurrences of keywords in the title
                for word in word_list:
                    word_lower = word.lower()
                    title_lower = title.lower()
                    if title_lower.count(word_lower):
                        counts[word_lower] = counts.get(word_lower, 0) + title_lower.count(word_lower)
            if data.get('after'):
                count_words(subreddit, word_list, data['after'], counts)
            else:
                # Print the sorted counts
                print_sorted_counts(counts)
        else:
            # Print nothing if no posts are found
            return
    else:
        # Print nothing for invalid subreddit or any other error
        return


def print_sorted_counts(counts):
    """
    Print the sorted counts of keywords in descending order.

    Args:
        counts (dict): Dictionary containing counts of keywords.

    Returns:
        None
    """
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # Print the sorted counts
    for keyword, count in sorted_counts:
        print(f'{keyword}: {count}')
