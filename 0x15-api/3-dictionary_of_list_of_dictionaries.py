#!/usr/bin/python3
"""
Records all tasks from all employees.
"""

import json
import requests

if __name__ == '__main__':
    all_users = {}
    url = 'https://jsonplaceholder.typicode.com/users'
    users_url = requests.get(url, timeout=5)
    another_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_url = requests.get(another_url, timeout=5)

    for users in users_url.json():
        userId = users.get('id')
        userName = users.get('username')
        all_users[str(userId)] = []
        for task in todo_url.json():
            task_dict = {}
            if task.get('userId') == userId:
                task_dict["username"] = userName
                task_dict["task"] = task.get('title')
                task_dict["completed"] = task.get('completed')
                all_users[str(userId)].append(task_dict)

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(all_users, file)
