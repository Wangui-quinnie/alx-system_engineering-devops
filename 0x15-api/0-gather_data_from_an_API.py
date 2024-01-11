#!/usr/bin/python3
""" Script that reurns information about an employee's TODO list
progress given his/her employee ID.
"""
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    None: Displays the employee's TODO list progress in the specified format.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    url = f'{base_url}/{employee_id}/todos'

    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)

        employee_url = f'{base_url}/{employee_id}'
        employee_response = requests.get(employee_url)
        employee_name = employee_response.json()['name']

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}): ")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print('Failed to retrieve data')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
