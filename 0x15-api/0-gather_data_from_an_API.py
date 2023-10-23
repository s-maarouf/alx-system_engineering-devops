#!/usr/bin/python3

"""A script that returns information about his/her TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    json_response = response.json()
    name = json_response.get("name")

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    json_response = response.json()

    total_tasks = 0
    done_tasks = 0
    tasks_titles = []

    for task in json_response:
        if task.get("userId") == int(user_id):
            total_tasks += 1
            if task.get("completed"):
                done_tasks += 1
                tasks_titles.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_tasks, total_tasks))
    for title in tasks_titles:
        print("\t {}".format(title))
