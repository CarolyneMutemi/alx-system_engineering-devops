#!/usr/bin/python3
"""
Eexport data from the given API in the CSV format.
"""
from collections import OrderedDict
import csv
import requests
import sys

if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}'
    user_url = requests.get(url, timeout=5)
    userId = user_url.json().get('id')
    userName = user_url.json().get('username')
    another_url = 'https://jsonplaceholder.typicode.com/todos/'
    todo_url = requests.get(another_url, timeout=5)
    info = OrderedDict()
    info['USER_ID'] = f'"{userId}"'
    info['USERNAME'] = f'"{userName}"'

    with open(f'{sys.argv[1]}.csv', 'w', encoding='utf-8') as file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        file_writer = csv.DictWriter(file, fieldnames=fieldnames,
                                     quoting=csv.QUOTE_NONE, quotechar=None)
        for task in todo_url.json():
            if task.get('userId') == int(sys.argv[1]):
                info["TASK_COMPLETED_STATUS"] = f"\"{task.get('completed')}\""
                info["TASK_TITLE"] = f"\"{task.get('title')}\""
                file_writer.writerow(info)
