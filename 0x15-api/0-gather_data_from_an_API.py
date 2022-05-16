#!/usr/bin/python3
""" Gather data from an API """


if __name__ == "__main__":
    import requests
    from sys import argv

    employeeID = argv[1]
    user_bio = {}
    todo_list = []
    done_tasks = []
    url_1 = 'https://jsonplaceholder.typicode.com/users'
    url_2 = 'https://jsonplaceholder.typicode.com/todos'

    user_bio = requests.get('{}/{}'.format(url_1, employeeID)).json()
    todo_response = requests.get(url_2).json()

    for r in todo_response:
        if r.get('userId') == int(employeeID):
            todo_list.append(r)
            if r.get('completed') is True:
                done_tasks.append(r)

    print("Employee {} is done with tasks({}/{}):".format(
        user_bio.get('name'), len(done_tasks), len(todo_list)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
