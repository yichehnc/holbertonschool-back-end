#!/usr/bin/python3
"""
A script that usses the REST API for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    """
    A function that returns information about his/her TODO list progress.
    """
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]
    user_url = "{}/users/{}".format(url, employee_id)
    EMPLOYEE_NAME = requests.get(user_url).json().get("name")

    todo_url = "{}/users/{}/todos".format(url, employee_id)
    todo_list = requests.get(todo_url).json()
    TOTAL_NUMBER_OF_TASKS = len(todo_list)

    NUMBER_OF_DONE_TASKS = len([todo for todo in todo_list
                                if todo.get("completed")])

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for todo in todo_list:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
