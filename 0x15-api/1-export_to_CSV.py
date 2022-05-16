#!/usr/bin/python3
"""
    Gather data from an API
    and export it to CSV
"""


if __name__ == '__main__':
    import csv
    import requests as rq
    from sys import argv

    employeeID = argv[1]
    user_bio = {}
    todo_list = []
    status_list = []
    _url_1 = 'https://jsonplaceholder.typicode.com/users'
    _url_2 = 'https://jsonplaceholder.typicode.com/todos'

    user_bio = rq.get('{}/{}'.format(_url_1, employeeID)).json()
    todo_response = rq.get(_url_2).json()

    for r in response:
        if r['userId'] == int(employeeID):
            todo_list.append(r)

    for task in todo_list:
        row = [employeeID, user_bio['name'], task['completed'], task['title']]
        status_list.append(row)

    with open('{}.csv'.format(employeeID), 'w') as csv_file:
        csv.writer(csv_file, delimiter=',',
                   quoting=csv.QUOTE_ALL).writerows(status_list)
