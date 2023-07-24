#!/usr/bin/python3
"""
module for a Python script to export data
for employee TODO list in the JSON format
"""

import json
import requests
import sys


def todolist_json():
    """
    function that exports data
    for employee TODO list in the JSON format
    """
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employee_id)).json()
    list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(employee_id)).json()
    employee_name = employee.get("username")
    with open("{}.json".format(employee_id), "w") as json_file:
        task_data = {employee_id: []}
        for todo_task in list:
            todo_tasks = {"task": todo_task.get("title"),
                          "completed": todo_task.get("completed"),
                          "username": employee_name}
            task_data[employee_id].append(todo_tasks)
        json.dump(task_data, json_file)


if __name__ == "__main__":
    todolist_json()
