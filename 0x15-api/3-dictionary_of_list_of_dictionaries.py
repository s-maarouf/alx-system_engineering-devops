#!/usr/bin/python3

"""Module All Gather data from an API to JSON"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    users_res = requests.get(url).json()
    data = {}
    for user in users_res:
        emp_id = user.get("id")
        emp_username = user.get("username")
        todo_url = url + str(emp_id) + "/todos"
        todo_res = requests.get(todo_url).json()
        data[emp_id] = []
        for todo in todo_res:
            data[emp_id].append({"username": emp_username,
                                 "task": todo.get("title"),
                                 "completed": todo.get("completed")})

    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(data, json_file)
