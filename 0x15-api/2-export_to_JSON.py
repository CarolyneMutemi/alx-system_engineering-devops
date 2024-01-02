#!/usr/bin/python3
"""
Exports data in the JSON format from the given API.
"""

import json
import requests
import sys

if __name__ == '__main__':
    userId = sys.argv[1]
    user_dict = {}
    user_dict[userId] = []

    url = f'https://jsonplaceholder.typicode.com/users/{userId}'
    user_url = requests.get(url, timeout=5)
    username = user_url.json().get('username')
    another_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_url = requests.get(another_url, timeout=5)

    for task in todo_url.json():
        if task.get('userId') == int(userId):
            task_dict = {}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            task_dict["username"] = username
            user_dict[userId].append(task_dict)

    with open(f'{userId}.json', 'w', encoding='utf-8') as file:
        json.dump(user_dict, file)
