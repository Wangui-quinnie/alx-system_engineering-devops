#!/usr/bin/python3
""" Script to export data in the CSV format. """

import csv
import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Retrieves and displays the employee's TODO list progress in
    the specified format.
    Additionally, exports the data to a CSV file.

    Args:
    employee_id (int): The ID of the employee.

    Returns:
    None: Displays the employee's TODO list progress and exports
    the data to a CSV file.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    url = f'{base_url}/{employee_id}/todos'

    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()

        employee_url = f'{base_url}/{employee_id}'
        employee_response = requests.get(employee_url)
        employee_name = employee_response.json()['name']

        csv_filename = f'{employee_id}.csv'

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME",
                                "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for todo in todos:
                if todo['completed']:
                    task_completed_status = 'True'
                else:
                    task_completed_status = 'False'
                csv_writer.writerow([employee_id, employee_name,
                                    task_completed_status, todo['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
