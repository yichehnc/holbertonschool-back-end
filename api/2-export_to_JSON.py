#!/usr/bin/python3
"""
A script that usses the REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    """
    A function that returns information about his/her TODO list progress.
    """
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user_url = "{}/users/{}".format(url, employee_id)
    user_data = requests.get(user_url).json()
    EMPLOYEE_NAME = user_data.get("name")
    USERNAME = user_data.get("username")
    USER_ID = user_data.get("id")

    todo_url = "{}/user/{}/todos".format(url, employee_id)
    todo_list = requests.get(todo_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    NUMBER_OF_DONE_TASKS = len([todo for todo in todo_list
                                if todo.get("completed")])

    tasks = [{
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": USERNAME
        } for todo in todo_list]

    todo_data = {USER_ID: tasks}

    with open('{}.json'.format(USER_ID), mode='w') as f:
        json.dump(todo_data, f)
