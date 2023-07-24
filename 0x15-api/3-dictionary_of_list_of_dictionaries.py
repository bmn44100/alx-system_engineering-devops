#!/usr/bin/python3
"""
module for a Python script to export data
for employee TODO list in the JSON format
"""


import json
import requests
import sys


def employee_username(api_url, employee_id):
    """
    function that gets data from
    employee TODO list in the REST api
    """
    employee_name = requests.get(
        "{}users/{}".format(api_url, employee_id), verify=False)
    employee_list = employee_name.json()
    return employee_list['username']


def employee_todo_list(api_url):
    """
    function that exports data
    for employee TODO list in the JSON format
    """
    employee_list = requests.get(
        "{}todos".format(api_url), verify=False)
    return employee_list.json()


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/'
    dict_employees = {}
    json_dict = {}
    todo_list = employee_todo_list(api_url)

    with open('todo_all_employees.json', 'w') as file:
        user_name = None
        for todo_task in todo_list:
            employee_id = str(todo_task['userId'])
            if employee_id in dict_employees.keys():
                user_name = dict_employees[employee_id]
            else:
                user_name = employee_username(api_url, employee_id)
                dict_employees[employee_id] = user_name
                json_dict[employee_id] = []

            todo = {}
            todo['task'] = todo_task['title']
            todo['completed'] = todo_task['completed']
            todo['username'] = user_name
            json_dict[employee_id].append(todo)

        file.write(json.dumps(json_dict))
