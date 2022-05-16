#!/usr/bin/python3
"""
    Gather data from an API
    and export it to JSON FILE
"""


if __name__ == '__main__':
    import csv
    import json
    from sys import argv as arguments
    from urllib import request as rq

    employeeID = arguments[1]
    user_bio = {}
    todo_list = []
    status_dict = {}
    status_dict[employeeID] = []
    _url_1 = 'https://jsonplaceholder.typicode.com/users'
    _url_2 = 'https://jsonplaceholder.typicode.com/todos'

    with rq.urlopen('{}/{}'.format(_url_1, employeeID)) as urlObj:
        user_bio = json.loads(urlObj.read())

    with rq.urlopen(_url_2) as urlObj:
        response = json.loads(urlObj.read())
        for r in response:
            if r['userId'] == int(employeeID):
                todo_list.append(r)

    for task in todo_list:
        row = {"task": task['title'], "completed": task['completed'],
               "username": user_bio['name']}
        status_dict[employeeID].append(row)

    with open('{}.json'.format(employeeID), 'w') as json_file:
        json.dump(status_dict, json_file, indent=4)
