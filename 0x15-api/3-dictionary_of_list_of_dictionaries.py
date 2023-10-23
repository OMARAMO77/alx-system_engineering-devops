#!/usr/bin/python3
"""Export data in the JSON format.
"""
from json import dumps
import requests


def get_tasks_from_employee(response, employee):
    """---"""
    employee_tasks = list()
    for task in response:
        if task.get('userId') == employee.get('id'):
            task_data = {
                'username': employee.get('username'),
                'task': task.get('title'),
                'completed': task.get('completed'),
            }

            employee_tasks.append(task_data)
    return employee_tasks


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    users_uri = '{}/users'.format(api_url)
    todos_uri = '{}/todos'.format(api_url)
    filename = 'todo_all_employees.json'

    u_res = requests.get(users_uri).json()
    t_res = requests.get(todos_uri).json()

    users_tasks = dict()
    for user in u_res:
        user_id = user.get('id')
        user_tasks = get_tasks_from_employee(t_res, {
            'id': user_id,
            'username': user.get('username')
        })
        users_tasks[user_id] = user_tasks

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(dumps(users_tasks))
