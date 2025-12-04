# models.py
 
from dataclasses import dataclass
from typing import Literal
 
# Define allowed statuses for clarity
Status = Literal["todo", "in-progress", "done"]
 
 
@dataclass
class Task:
    """Represents a to-do task.
 
    id is managed by the application logic (e.g., in main.py or task_manager.py).
    """
    id: int
    title: str
    priority: int
    status: Status = "todo"
 
    def __str__(self) -> str:
        """Friendly string representation for printing."""
        return f"[ID: {self.id:03d}] {self.title:<30} | Priority: {self.priority} | Status: {self.status.upper()}"