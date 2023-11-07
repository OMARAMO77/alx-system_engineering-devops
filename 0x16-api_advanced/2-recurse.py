#!/usr/bin/python3
"""Queries the Reddit"""
from requests import get


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all hot articles
    for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'Python/requests'}

    payload = {'after': after, 'limit': '100'}

    response = get(url, headers=headers, params=payload,
                   allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        after = response.json().get('data').get('after')

        for post in posts:
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    return None
