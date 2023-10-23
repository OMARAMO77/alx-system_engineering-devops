#!/usr/bin/python3
"""Display information about TODO list of an Employee.
"""
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{}/users/{}'.format(api_url, user_id)
    todo_uri = '{}/todos'.format(user_uri)

    response = requests.get(user_uri).json()
    name = response.get('name')

    response = requests.get(todo_uri).json()
    total = len(response)

    completed = sum([elem['completed'] is True for elem in response])

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for elem in response:
        if elem.get('completed') is True:
            print("\t {}".format(elem.get('title')))
