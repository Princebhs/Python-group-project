# Python Project – Task List Manager

## Overview

You will build a console-based Task List Manager in Python.

The focus is on:
- Practising basic data structures (lists, dictionaries, simple classes)
- Implementing and testing simple algorithms (search, sort, filter)
- Working as a team on a small, realistic codebase

The scaffold provides starter files and function signatures. Your job is to fill in the implementations and improve the design where you can.


## Learning Goals
- Use Python lists and dictionaries to model tasks
- Implement simple algorithms (e.g. filter by status, sort by priority)
- Write clear, readable functions with docstrings
- Coordinate work in a small team (merging, reviewing, dividing tasks)

## Features to Implement

A "task" has at least:
- `id` (int)
- `title` (string)
- `priority` (int, e.g. 1–5 where 1 is highest priority)
- `status` (string, e.g. "todo", "in-progress", "done")

Your Task List Manager should support (via a text-based menu):

1. Add a new task
2. List all tasks
3. Filter tasks by status (e.g. show only "todo")
4. Sort tasks by priority
5. Mark a task as done

You do not need to store data permanently (no database or files required), but you *may* add simple save/load later if there is time.

## Files Provided

- `main.py` – entry point with a basic menu loop and TODO markers
- `models.py` – contains a simple `Task` class skeleton
- `task_manager.py` – functions for creating, listing, filtering, sorting, and updating tasks

## Suggested Team Task Split

- Person A: Implement `Task` class in `models.py`
- Person B: Implement create/list functions in `task_manager.py`
- Person C: Implement filter and sort functions in `task_manager.py`
- Person D: Implement update/mark-done function and integrate with menu in `main.py`
- Person E (if present): Testing, input validation, code review, and small refactors

## Getting Started with Git

Run these commands once per team from this folder:

```bash
git init
git add .
git commit -m "Initial commit"
```
Ensure one of the team regularly commits to the repository. Use simple commits for now, unless you want to experiement with branch and merge.

## What To Do

1. Read through all three Python files to understand the structure.
2. Decide which TODOs each team member will own.
3. Implement the required functions.
4. Run the program regularly, test menu options, and fix any bugs.
5. If time allows, add one or two small "nice-to-have" features (see below).

## Nice-to-Have Ideas (Optional)

If you finish the core requirements early, consider:

- Add simple input validation (e.g. reject empty titles, invalid priorities)
- Add a "delete task" option
- Add a way to save tasks to a JSON file and load them again
- Add colourful output using simple ANSI codes (or keep it plain if this is confusing)

## Running the Project

From the `python-project` folder, run:

```bash
python main.py
```

---

Use clear names, small functions, and lots of comments where helpful. Focus on *readable* code rather than clever tricks.
