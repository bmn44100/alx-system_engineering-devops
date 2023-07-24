#!/usr/bin/python3
"""
module for a Python script to export data
for employee TODO list in the CSV format
"""

import csv
import requests
import sys


def todolist_csv():
    """
    function that exports data
    for employee TODO list in the CSV format
    """
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(employee_id)).json()
    list = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(employee_id)).json()
    employee_name = employee.get("username")
    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        todo_file = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in list:
            todo_file.writerow([employee_id, employee_name,
                           task.get("completed"), task.get("title")])

if __name__ == "__main__":
    todolist_csv()
