#!/usr/bin/python3
"""
    Gather data from an API
"""


if __name__ == '__main__':
    from urllib import request as rq
    from sys import argv as arguments
    import json

    employeeID = arguments[1]
    user_bio = {}
    todo_list = []
    done_tasks = []

    with rq.urlopen('https://jsonplaceholder.typicode.com/users/{}'.format(employeeID)) as urlObj:
        user_bio = json.loads(urlObj.read())

    with rq.urlopen('https://jsonplaceholder.typicode.com/todos') as urlObj:
        response = json.loads(urlObj.read())
        for r in response:
            if r['userId'] == int(employeeID):
                todo_list.append(r)
                if r['completed'] == True:
                    done_tasks.append(r)
    
    print("Employee {} is done with tasks({}/{}):".format(user_bio['name'], len(done_tasks), len(todo_list)))
    for task in done_tasks:
        print("\t{}".format(task['title']))
