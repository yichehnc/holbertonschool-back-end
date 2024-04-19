#!/usr/bin/python3
"""
A script that usses the REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import csv
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

    with open('{}.csv'.format(USER_ID), mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_list:
            writer.writerow([USER_ID, USERNAME, todo.get("completed"),
                             todo.get("title")])
