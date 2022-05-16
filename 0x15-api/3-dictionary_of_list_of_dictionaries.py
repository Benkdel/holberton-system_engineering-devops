#!/usr/bin/python3
"""
    Gather data from an API
    and export it to JSON FILE
"""


if __name__ == '__main__':
    import json
    import requests as rq

    users_bio = {}
    todo_list = []
    status_dict = {}
    url_1 = 'https://jsonplaceholder.typicode.com/users'
    url_2 = 'https://jsonplaceholder.typicode.com/todos'

    users_bio = rq.get(url_1).json()
    todo_list = rq.get(url_2).json()

    for user in users_bio:
        tasks = []
        for todo in todo_list:
            if todo['userId'] == user['id']:
                tasks.append({"username": user["username"],
                              "task": todo['title'],
                              "completed": todo['completed']})
        status_dict[user['id']] = tasks

    with open('{}.json'.format('todo_all_employees'), 'w',
              encoding="utf8") as json_file:
        json.dump(status_dict, json_file, indent=4)
