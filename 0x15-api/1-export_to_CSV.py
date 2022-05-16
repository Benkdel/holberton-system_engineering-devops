#!/usr/bin/python3
"""
    Gather data from an API
    and export it to CSV
"""


if __name__ == '__main__':
    import csv
    import json
    from sys import argv as arguments
    from urllib import request as rq

    employeeID = arguments[1]
    user_bio = {}
    todo_list = []
    status_list = []
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
        row = [employeeID, user_bio['name'], task['completed'], task['title']]
        status_list.append(row)

    with open('{}.csv'.format(employeeID), 'w') as csv_file:
        csv.writer(csv_file, delimiter=',',
                   quoting=csv.QUOTE_ALL).writerows(status_list)
