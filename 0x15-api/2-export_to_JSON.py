#!/usr/bin/python3
"""
    Gather data from an API
    and export it to JSON FILE
"""


if __name__ == '__main__':
    import json
    import requests as rq
    from sys import argv as arguments

    employeeID = arguments[1]
    user_bio = {}
    todo_list = []
    status_dict = {}
    status_dict[employeeID] = []
    url_1 = 'https://jsonplaceholder.typicode.com/users'
    url_2 = 'https://jsonplaceholder.typicode.com/todos'

    user_bio = rq.get('{}/{}'.format(url_1, employeeID)).json()
    todo_response = rq.get(url_2).json()

    for r in todo_response:
        if r['userId'] == int(employeeID):
            todo_list.append(r)

    for task in todo_list:
        row = {"task": task['title'], "completed": task['completed'],
               "username": user_bio['username']}
        status_dict[employeeID].append(row)

    with open('{}.json'.format(employeeID), 'w') as json_file:
        json.dump(status_dict, json_file, indent=4)
