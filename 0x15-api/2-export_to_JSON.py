#!/usr/bin/python3
""" A script that export data in JSON format."""


import json
import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee and exports
    it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("username")

        # Fetch TODO list for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare JSON file name
        json_filename = f"{employee_id}.json"

        # Prepare JSON structure
        json_data = {
            str(employee_id): [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                }
                for task in todos_data
            ]
        }
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file)

        print(f"Data exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)
