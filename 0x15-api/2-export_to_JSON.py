#!/usr/bin/python3

"""A script that returns information about his/her TODO list
progress and saves it to a CSV file"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    completed_url = "https://jsonplaceholder.typicode.com/todos/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)

    user_response = requests.get(user_url)
    completed_response = requests.get(completed_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    completed_data = completed_response.json()
    todos_data = todos_response.json()

    file_name = employee_id + ".json"
    data = {employee_id: []}
    for todo in todos_data:
        data[employee_id].append({
            "task": todo.get('title'),
            "completed": todo.get("completed"),
            "username": user_data.get('username')})
    with open(file_name, mode='w') as f:
        json.dump(data, f)
