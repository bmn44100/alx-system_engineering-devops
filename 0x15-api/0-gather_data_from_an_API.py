#!/usr/bin/python3
"""
module for a Python script that, using this REST API, for a
given employee ID, returns information about his/her
TODO list progress
"""

import requests
import sys


def todo_list():
    """
    function that, for a given employee ID returns
    information about his/her TODO list progress.
    """
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id)).json()
    tr = "https://jsonplaceholder.typicode.com/todos?userId={}&&completed=true"
    employee_todo = requests.get(tr.format(employee_id)).json()
    list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(employee_id)).json()
    employee_name = employee.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(employee_todo), len(list)))
    for task in list:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))

if __name__ == "__main__":
    todo_list()
