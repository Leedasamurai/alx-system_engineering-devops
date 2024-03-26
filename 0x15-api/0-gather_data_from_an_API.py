#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    url_user = '{}/users/{}'.format(base_url, employee_id)
    url_todos = '{}/todos?userId={}'.format(base_url, employee_id)

    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)

    if user_response.status_code != 200:
        print("Error: User data not found")
        sys.exit(1)

    if todos_response.status_code != 200:
        print("Error: TODO data not found")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get('completed'))

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
        completed_tasks, total_tasks))
    for todo in todos_data:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
