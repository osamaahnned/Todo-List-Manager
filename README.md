# Todo List Manager
#### Video Demo:  https://youtu.be/vFR-sfJGPSQ
#### Description:
The Command-Line Todo List Manager is a Python script designed to help users organize their tasks efficiently through a command-line interface. In this README.md file, we will delve into the code, exploring its functionality, structure, implementation details, and usage instructions. By the end of this document, you'll have a thorough understanding of how the todo list manager works and how to utilize it effectively.## Features

- Add tasks with optional due dates and priorities.
- List all tasks with their due dates and priorities.
- Remove tasks by task number.
- Mark tasks as completed.
- Clear all completed tasks.

## Functionally
At its core, the Command-Line Todo List Manager provides several key features:

Add Tasks: Users can add tasks to the list, optionally specifying due dates and priorities.
List Tasks: All tasks in the todo list are displayed along with their due dates and priorities.
Remove Tasks: Users can remove tasks from the list by specifying the task number.
Mark Tasks as Completed: Tasks can be marked as completed, adding a "completed" flag to the task.
Clear Completed Tasks: All completed tasks can be removed from the list in one go.
These features aim to provide users with a comprehensive tool for managing their tasks effectively from the command line.
## Code Structure

The codebase consists of a single Python script, todo.py, which contains functions responsible for different aspects of todo list management. Let's break down the structure of the code:

Function Definitions: The script starts by defining functions such as print_list(), add_task(), remove_task(), complete_task(), clear_completed(), and main(). These functions encapsulate specific actions related to todo list management.

Main Function: The main() function serves as the entry point of the script. It parses command-line arguments and calls the appropriate functions based on the user's input.

Functionality Implementation: Each function is responsible for a specific aspect of todo list management. For example, print_list() reads tasks from the todo.txt file and prints them to the console, while add_task() adds a new task to the todo.txt file with optional due dates and priorities.

File Handling: The script utilizes file I/O operations to read from and write to a text file (todo.txt) where tasks are stored. File handling functions such as open(), read(), and write() are used to manipulate the todo list file.
## Implementation Details
Let's dive deeper into the implementation details of the key functionalities:

File Handling: File handling is crucial for reading and writing tasks to the todo list file (todo.txt). The script opens the file in read or write mode using the open() function and performs read or write operations as needed. Tasks are stored as lines in the text file, with each line representing a single task.

Command-Line Arguments: The script accepts command-line arguments to determine the desired action and provide additional options when adding tasks. Command-line arguments include options like list, add, remove, complete, and clear, each triggering a specific functionality.

Error Handling: Error handling mechanisms are implemented to handle invalid input and potential errors during file I/O operations. The script uses conditional statements and exception handling to ensure smooth execution and provide informative error messages to the user.


## Usage
To use the Command-Line Todo List Manager, follow these steps:

1. Open a Terminal: Open a terminal or command prompt on your system.

2. Navigate to the Directory: Navigate to the directory containing the todo.py script using the cd command.

3. Execute Commands: Use the appropriate command-line arguments to perform desired operations, such as adding, listing, removing, completing, or clearing tasks.

Example usage:


1. **List all tasks**: `python todo.py list`
   - Displays all tasks in the todo list.

2. **Add a task**: `python todo.py add <task_description> [-d due_date] [-p priority]`
   - Adds a new task to the list. Optional parameters include due date (YYYY-MM-DD format) and priority.

3. **Remove a task**: `python todo.py remove <task_number>`
   - Removes the task with the specified number from the list.

4. **Mark a task as completed**: `python todo.py complete <task_number>`
   - Marks the task with the specified number as completed.

5. **Clear completed tasks**: `python todo.py clear`
   - Removes all completed tasks from the list.

## Example
python todo.py add "Complete CS50 problem set" -d 2024-04-30 -p High
python todo.py list
python todo.py complete 1
python todo.py clear

## Code Explaination
**Functionality**: The code is organized into functions that handle different aspects of the todo list management, such as adding, listing, removing, and completing tasks.
**File Handling**: The todo list is stored in a text file named todo.txt, and file I/O operations are used to read from and write to this file.
**Command-Line Arguments**: The script accepts command-line arguments to determine which operation to perform and provides options for adding tasks with due dates and priorities.
**Error Handling**: The code includes error handling for invalid input, such as incorrect task numbers or date formats.
**Modularity**: The code is modular and easy to extend. Additional features or improvements can be added with minimal changes to the existing codebase.

## Conclusion
In this README.md file, we've explored the Command-Line Todo List Manager codebase, covering its functionality, structure, implementation details, and usage instructions. The script provides users with a powerful tool for managing tasks efficiently from the command line, utilizing file handling, command-line arguments, and error handling mechanisms. With this comprehensive understanding, users can effectively utilize the todo list manager to organize their tasks and boost productivity.
