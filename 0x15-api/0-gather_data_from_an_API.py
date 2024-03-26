#!/usr/bin/python3
"""
Retrieves information about an employee's TODO list progress using a REST API.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user info
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user info for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown")

    # Fetch todos
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODOs for employee ID {employee_id}")
        return

    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))

    # Display progress
    print(f"Employee {employee_name} is done with tasks(
            {completed_tasks}/{total_tasks}):")
    for todo in todos_data:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
