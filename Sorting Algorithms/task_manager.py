import argparse
import datetime
import json
import logging as log
import time

# Initialize logging
log.basicConfig(filename='tasks.log', level=log.INFO, format='%(asctime)s - %(message)s')

# Load tasks from JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(title, description, due_date):
    tasks = load_tasks()
    tasks.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'status': 'pending'
    })
    save_tasks(tasks)
    log.info(f"Task '{title}' added with due date {due_date}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks, start=1):
        print(f"Task {index}:")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Status: {task['status']}")
        print()

# Complete a task
def complete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]['status'] = 'completed'
        save_tasks(tasks)
        log.info(f"Task '{tasks[index - 1]['title']}' marked as completed")
    else:
        print("Invalid task index")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        save_tasks(tasks)
        log.info(f"Task '{deleted_task['title']}' deleted")
    else:
        print("Invalid task index")

# CLI setup
parser = argparse.ArgumentParser(description='Task Manager')
parser.add_argument('command', choices=['add', 'list', 'complete', 'delete'], help='Command to execute')
parser.add_argument('--title', help='Task title')
parser.add_argument('--description', help='Task description')
parser.add_argument('--due-date', help='Task due date (YYYY-MM-DD)')
parser.add_argument('--index', type=int, help='Task index')

args = parser.parse_args()

# Execute commands
if args.command == 'add':
    add_task(args.title, args.description, args.due_date)
elif args.command == 'list':
    list_tasks()
elif args.command == 'complete':
    complete_task(args.index)
elif args.command == 'delete':
    delete_task(args.index)

"""
Usage:
Adding a task:

csharp
Copy code
python task_manager.py add --title "Complete project" --description "Finish project report" --due-date 2024-07-01
Listing tasks:

Copy code
python task_manager.py list
Completing a task:

css
Copy code
python task_manager.py complete --index 1
Deleting a task:

perl
Copy code
python task_manager.py delete --index 1
"""
