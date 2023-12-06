#!/usr/bin/python3

"""A script that returns information about his/her todo list progress"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = len([task for task in todos_data if task.get('completed')])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          done_tasks, total_tasks))

    for task in todos_data:
        if task['completed']:
            print("\t " + task['title'])
