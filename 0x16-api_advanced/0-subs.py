#!/usr/bin/python3
"""Queries the Reddit API"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers
    for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'Python/requests'}

    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get('data').get('subscribers')
