#!/usr/bin/python3
"""
Uses given REST API for a given employee ID
and returns information about his/her TODO list.
"""

import requests
import sys

if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    user_url = requests.get(url, timeout=5)
    name = user_url.json().get('name')
    another_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_url = requests.get(another_url, timeout=5)
    todo_list = todo_url.json()
    done = 0
    total = 0
    list_done = []

    for task in todo_list:
        if task.get('userId') == int(sys.argv[1]):
            if task.get('completed'):
                list_done.append(task['title'])
                done += 1
            total += 1

    print(f'Employee {name} is done with tasks({done}/{total})')

    for title in list_done:
        print(f'\t {title}')
