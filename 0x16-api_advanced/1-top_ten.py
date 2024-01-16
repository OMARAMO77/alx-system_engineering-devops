#!/usr/bin/python3
"""Queries the Reddit API"""
from requests import get


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
        listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'Python/requests'}

    payload = {'limit': '10'}

    response = get(url, headers=headers, params=payload,
                   allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        posts = response.json().get('data').get('children')
        if posts:
            for post in posts:
                if post.get('data').get('title'):
                    print(post.get('data').get('title'))
