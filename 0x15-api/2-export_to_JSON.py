#!/usr/bin/python3
"""Export data in the JSON format.
"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{}/users/{}'.format(api_url, user_id)
    todo_uri = '{}/todos'.format(user_uri)
    filename = '{}.json'.format(user_id)

    response = requests.get(user_uri).json()
    username = response.get('username')

    response = requests.get(todo_uri).json()
    task_list = list()
    for elem in response:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': username
        }
        task_list.append(data)

    with open(filename, 'w') as file:
        file.write(dumps({user_id: task_list}))
