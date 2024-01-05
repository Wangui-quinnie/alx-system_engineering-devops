python Scripting Back-end API

Learning objectives include knowing:

** What Bash scripting should not be used for **
Bash scripting may not be the best choice for large and complex applications that require extensive data processing, complex algorithms, and GUI applications. While it's excellent for automating tasks, system administration, and small to medium-sized scripts, other languages may be better suited for complex applications.

** What is an API **
API stands for Application Programming Interface. It's a set of rules and protocols that allows one software application to interact with another. Essentially, it defines the methods and data structures available for the interchange of data among different software components.

** What is a REST API **
REST (Representational State Transfer) API is a type of web service that adheres to the principles of REST architectural style. It uses standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources. REST APIs are stateless, meaning each request from a client contains all the information necessary for the server to fulfill it.

** What are microservices **
Microservices represents a software development technique where an application is structured as a collection of loosely coupled services. Each service is independently deployable and scalable. Microservices allow for the division of large, monolithic systems into smaller, more manageable components.

** what is the CSV format **
CSV (Comma-Separated Values) is a file format that stores tabular data in a plain text form. Each line of the file is a data record, and each record consists of one or more fields, separated by commas. CSV is commonly used for exchanging data between different applications.

** What is the JSON format **
JSON (JavaScript Object Notation) is a lightweight data interchange format. It's easy for humans to read and write, and easy for machines to parse and generate. It's based on a subset of the JavaScript programming language and often used as a data format for web APIs.

** Pythonic naming style **
Package: lowercase, no underscores: mypackage
Module: lowercase, underscores allowed: my_module
Class: CapWords (CamelCase): MyClass
Variable: lowercase, underscores allowed: my_variable
Function: lowercase, underscores allowed: my_function
Constant: Uppercase with underscores: MY_CONSTANT

** Significance of CapWords or CamelCase in Python **
In Python, using CamelCase for class names enhances code readability and maintains consistency across projects that follow the PEP 8 style guide.


	TASKS
0. Gather data from an API
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.

Requirements:

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the employee TODO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)


1. Export to CSV
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv


2. Export to JSON
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json


3. Dictionary of list of dictionaries
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
