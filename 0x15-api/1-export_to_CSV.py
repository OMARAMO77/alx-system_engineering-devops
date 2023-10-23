#!/usr/bin/python3
"""Export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{}/users/{}'.format(api_url, user_id)
    todo_uri = '{}/todos'.format(user_uri)
    filename = '{}.csv'.format(user_id)

    response = requests.get(user_uri).json()
    username = response.get('username')

    response = requests.get(todo_uri).json()

    with open(filename, 'w') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in response:
            status = elem.get('completed')
            title = elem.get('title')
            writer.writerow([user_id, username, status, title])
