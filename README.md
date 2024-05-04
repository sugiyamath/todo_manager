# todo_manager

This is a simple command-line TODO list application written in Python.

## Features

- Add tasks to the TODO list.
- List all tasks in the TODO list.
- Mark a task as "doing".
- Mark a task as "done" and remove it from the TODO list.
- Load and save tasks from/to a file.
- Load and save task history from/to a file.

## Files

- `todo.txt`: This file stores the current TODO list.
- `todo_history.txt`: This file stores the history of tasks.

## Functions

- `load_todo()`: Load tasks from `todo.txt`.
- `save_todo()`: Save tasks to `todo.txt`.
- `load_history()`: Load task history from `todo_history.txt`.
- `save_history()`: Save task history to `todo_history.txt`.
- `add_todo(todo)`: Add a task to the TODO list.
- `list_todo()`: List all tasks in the TODO list.
- `do_todo(i)`: Mark a task as "doing".
- `done_todo(i)`: Mark a task as "done" and remove it from the TODO list.

## Usage

Run the script with a command and a parameter:

```bash
./todo.py <cmd> <param>
```

Commands:
- add <todo name>: Add a task.
- list: List all tasks.
- do <todo ID>: Mark a task as “doing”.
- done <todo ID>: Mark a task as “done”.


## Example
./todo.py add "Write README.md"
./todo.py list
./todo.py do 0
./todo.py done 0