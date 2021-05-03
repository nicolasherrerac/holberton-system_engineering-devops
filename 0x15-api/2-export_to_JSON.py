#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = int(argv[1])

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()

    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id)).json()

    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = user.get('username')
        tasks.append(task_dict)
    json_file = {}
    json_file[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsfile:
        json.dump(json_file, jsfile)
