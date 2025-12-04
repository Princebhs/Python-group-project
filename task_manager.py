# task_manager.py
 
from typing import List, Optional
 
# Assuming models.py is defined in the same directory
from models import Task
 
 
def create_task(task_id: int, title: str, priority: int, status: str = "todo") -> Task:
    """Create and return a new Task instance."""
    return Task(id=task_id, title=title, priority=priority, status=status)
 
 
def list_tasks(tasks: List[Task], header: str = "--- Current Tasks ---") -> None:
    """Print all tasks to the console.
 
    Keep the formatting simple but clear.
    """
    if not tasks:
        print("\n(The task list is currently empty or filter returned no results.)")
        return
 
    print(f"\n{header}")
    for task in tasks:
        # Uses the Task.__str__ method for clean formatting
        print(task)
    print("-" * len(header))
 
 
def filter_tasks_by_status(tasks: List[Task], status: str) -> List[Task]:
    """Return a new list containing only tasks with the given status."""
    status_lower = status.lower()
    # Use a list comprehension for concise filtering
    filtered_list = [task for task in tasks if task.status.lower() == status_lower]
    return filtered_list

 
def sort_tasks_by_priority(tasks: List[Task]) -> List[Task]:
    """Return a new list of tasks sorted by priority (ascending).
 
    Decision: We return a *new* list to avoid unexpectedly modifying
    the global TASKS list in the main application.
    """
    # Use the sorted() function with a lambda key to sort by the 'priority' attribute
    # Default ascending order means 1 (highest priority) comes first.
    sorted_list = sorted(tasks, key=lambda task: task.priority)
    return sorted_list
 
 
def mark_task_as_done(tasks: List[Task], index: int) -> Optional[Task]:
    """Mark the task at the given index as done.
 
    Looks up by the *list index* and updates the task status to "done".
    Returns the updated task or None if the index is invalid.
    """
    try:
        # The index should be the position in the current list
        task_to_update = tasks[index]
        task_to_update.status = "done"
        return task_to_update
    except IndexError:
        return None
s=create_task(1,'fasfasf',1,'a')
print(s)