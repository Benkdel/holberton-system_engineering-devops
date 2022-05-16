#!/usr/bin/python3
"""
    Gather data from an API
    and export it to JSON FILE
"""


if __name__ == '__main__':
    import csv
    import json
    from urllib import request as rq
    from sys import argv as arguments

    users_bio = {}
    todo_list = []
    status_dict = {}
    _url_1 = 'https://jsonplaceholder.typicode.com/users'
    _url_2 = 'https://jsonplaceholder.typicode.com/todos'

    with rq.urlopen(_url_1) as urlObj:
        users_bio = json.loads(urlObj.read())

    with rq.urlopen(_url_2) as urlObj:
        todo_list = json.loads(urlObj.read())

    for user in users_bio:
        tasks = []
        for todo in todo_list:
            if todo['userId'] == user['id']:
                tasks.append({"username": user["name"],
                              "task": todo['title'],
                              "completed": todo['completed']})
        status_dict[user['id']] = tasks

    with open('{}.json'.format('todo_all_employees'), 'w') as json_file:
        json.dump(status_dict, json_file, indent=4)
