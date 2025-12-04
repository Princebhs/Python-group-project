# main.py
 
"""Entry point for the Task List Manager.
 
This file contains a basic console menu loop.
Your team should complete the TODOs and connect the menu
options to the functions in `task_manager.py`.
"""
 
from typing import List
from task_manager import (
    create_task,
    list_tasks,
    filter_tasks_by_status,
    sort_tasks_by_priority,
    mark_task_as_done,
)
from models import Task # Import Task for type hinting and list definition
 
 
def print_menu() -> None:
    """Print the main menu options."""
    print("\n==== Task List Manager ====")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Filter tasks by status")
    print("4. Sort tasks by priority")
    print("5. Mark a task as done")
    print("0. Exit")
 
 
# This list will act as our in-memory "database" of tasks.
TASKS: List[Task] = []
# Global counter for unique IDs
TASK_ID_COUNTER = 1
 
 
def get_next_task_id() -> int:
    """Provides a unique, incrementing ID for new tasks."""
    global TASK_ID_COUNTER
    current_id = TASK_ID_COUNTER
    TASK_ID_COUNTER += 1
    return current_id
 
 
def handle_add_task() -> None:
    """Collect input from the user and add a new task."""
    print("\n-- Add New Task --")
    title = input("Title (required): ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
 
    priority_str = input("Priority (1 = highest, enter a number): ")
    status = "todo"
 
    try:
        # Convert priority_str to int, handle errors simply
        priority = int(priority_str)
        if priority < 1:
            print("Priority must be 1 or greater. Setting to 1.")
            priority = 1
        # Call create_task and append to TASKS
        task_id = get_next_task_id()
        new_task = create_task(task_id=task_id, title=title, priority=priority, status=status)
        TASKS.append(new_task)
        print(f"Task '{title}' (ID: {task_id}) added successfully.")
 
    except ValueError:
        print("Invalid priority input. Please enter a whole number.")
 
 
def handle_list_tasks() -> None:
    """Print all tasks."""
    list_tasks(TASKS)
 
 
def handle_filter_tasks() -> None:
    """Ask for a status and show matching tasks."""
    print("\n-- Filter Tasks by Status --")
    # List valid statuses for clarity
    valid_statuses = ["todo", "in-progress", "done"]
    status = input(f"Enter status ({'/'.join(valid_statuses)}): ").strip().lower()
 
    if status not in valid_statuses:
        print("Invalid status entered. Please choose from: todo, in-progress, or done.")
        return
 
    # Call filter_tasks_by_status(TASKS, status)
    filtered_tasks = filter_tasks_by_status(TASKS, status)
    # Show the results.
    list_tasks(filtered_tasks, header=f"--- Filtered Tasks: {status.upper()} ---")
 
 
def handle_sort_tasks() -> None:
    """Sort tasks by priority and show the result."""
    print("\n-- Tasks Sorted by Priority --")
 
    # Call sort_tasks_by_priority(TASKS). It returns a new sorted list.
    sorted_tasks = sort_tasks_by_priority(TASKS)
    # Show the results.
    list_tasks(sorted_tasks, header="--- All Tasks Sorted by Priority (1 is Highest) ---")
 
 
def handle_mark_task_done() -> None:
    """Mark a specific task as done."""
    print("\n-- Mark Task as Done --")
    if not TASKS:
        print("No tasks available to mark as done.")
        return
    # Show the tasks with an index number
    list_tasks(TASKS) 
    index_str = input("Enter the index number [0, 1, 2...] from the list above to mark as done: ")
    try:
        index = int(index_str)
        # Call mark_task_as_done
        updated_task = mark_task_as_done(TASKS, index)
        if updated_task:
             print(f"SUCCESS: Task '{updated_task.title}' marked as DONE.")
        else:
             print(f"Error: Index {index} is out of range. No task updated.")
 
    except ValueError:
        print("Invalid input. Please enter a valid index number.")
 
 
def main() -> None:
    """Run the main menu loop."""
    while True:
        print_menu()
        choice = input("Choose an option: ")
 
        if choice == "1":
            handle_add_task()
        elif choice == "2":
            handle_list_tasks()
        elif choice == "3":
            handle_filter_tasks()
        elif choice == "4":
            handle_sort_tasks()
        elif choice == "5":
            handle_mark_task_done()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
 
 
if __name__ == "__main__":
    main()