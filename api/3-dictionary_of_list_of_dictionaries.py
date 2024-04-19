#!/usr/bin/python3
"""
A script that usses the REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users".format(url)
    user_data = requests.get(user_url).json()

    all_data = {}

    for user in user_data:
        USERNAME = user.get("username")
        USER_ID = user.get("id")

        todo_url = "{}/users/{}/todos".format(url, USER_ID)
        todo_list = requests.get(todo_url).json()

        tasks = [{"username": USERNAME,
                  "task": todo.get("title"),
                  "completed": todo.get("completed")}
                 for todo in todo_list]

        all_data[USER_ID] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_data, f)
