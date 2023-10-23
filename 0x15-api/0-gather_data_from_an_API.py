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

    user = requests.get(url + "/{}".format(user_id)).json()
    todos = [t for t in json_response if t.get("userId") == int(user_id)]
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
