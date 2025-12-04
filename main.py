"""Entry point for the Task List Manager.

This file contains a basic console menu loop.
Your team should complete the TODOs and connect the menu
options to the functions in `task_manager.py`.
"""

from task_manager import (
    create_task,
    list_tasks,
    filter_tasks_by_status,
    sort_tasks_by_priority,
    mark_task_as_done,
)


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
# Each element should be a Task instance (see models.py).
TASKS = []  # TODO: decide as a team if this should stay global.


def handle_add_task() -> None:
    """Collect input from the user and add a new task.

    TODO: Use create_task(...) from task_manager to build a Task
    and append it to TASKS.
    """
    print("\n-- Add New Task --")
    title = input("Title: ")
    priority_str = input("Priority (1 = highest): ")
    status = "todo"  # start everything as todo by default

    # TODO: convert priority_str to int, handle errors simply
    # TODO: call create_task and append to TASKS


def handle_list_tasks() -> None:
    """Print all tasks.

    TODO: Call list_tasks(TASKS) and print them nicely.
    You can either print here, or let list_tasks handle printing.
    """
    print("\n-- All Tasks --")
    # TODO: implement using task_manager.list_tasks


def handle_filter_tasks() -> None:
    """Ask for a status and show matching tasks."""
    print("\n-- Filter Tasks by Status --")
    status = input("Enter status (todo/in-progress/done): ")

    # TODO: call filter_tasks_by_status(TASKS, status)
    # and show the results.


def handle_sort_tasks() -> None:
    """Sort tasks by priority and show the result."""
    print("\n-- Tasks Sorted by Priority --")

    # TODO: call sort_tasks_by_priority(TASKS)
    # Decide as a team: sort in-place, or return a new list?


def handle_mark_task_done() -> None:
    """Mark a specific task as done.

    TODO: Ask the user which task to mark as done.
    A simple approach is to show the tasks with an index number
    (0, 1, 2, ...) and ask the user to enter the index.
    Then call mark_task_as_done.
    """
    print("\n-- Mark Task as Done --")
    # TODO: implement using mark_task_as_done(TASKS, index)
    if not TASKS:
        print("No available tasks")
        


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
