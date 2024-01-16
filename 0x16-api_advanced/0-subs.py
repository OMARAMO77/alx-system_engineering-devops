#!/usr/bin/python3
"""
Returns the total number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    api_uri = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = { 'User-Agent': 'azer/1.0 (by /u/omar)' }
    res = requests.get(api_uri, headers=headers)
    if res.status_code == 200:
        subscribers = res.json()['data']['subscribers']
        return subscribers
    else:
        return 0
