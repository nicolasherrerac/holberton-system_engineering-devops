#!/usr/bin/python3
"""script to export data in the JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    user_dict = {}
    user_name = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        user_name[user_id] = user.get('username')
    for task in todo:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict['username'] = user_name.get(user_id)
        user_dict.get(user_id).append(task_dict)
    with open("todo_all_employees.json", 'w') as jsfile:
        json.dump(user_dict, jsfile)
