import sys
import os
from datetime import datetime

def print_list():
    if not os.path.exists("todo.txt"):
        print("Todo list is empty!")
    else:
        with open("todo.txt", "r") as file:
            lines = file.readlines()
            print("Todo List:")
            for i, line in enumerate(lines):
                print(f"{i+1}. {line.strip()}")

def add_task(task, due_date=None, priority=None):
    task_string = task
    if due_date:
        task_string += f" (Due: {due_date})"
    if priority:
        task_string += f" [Priority: {priority}]"
    with open("todo.txt", "a") as file:
        file.write(task_string + "\n")
    print("Task added successfully!")

def remove_task(task_number):
    tasks = []
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    if task_number <= len(tasks):
        del tasks[task_number - 1]
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number")

def complete_task(task_number):
    tasks = []
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    if task_number <= len(tasks):
        task = tasks[task_number - 1].strip()
        tasks[task_number - 1] = f"{task} - Completed\n"
        with open("todo.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number")

def clear_completed():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
    incomplete_tasks = [task for task in tasks if "- Completed" not in task]
    with open("todo.txt", "w") as file:
        file.writelines(incomplete_tasks)
    print("Completed tasks cleared!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [option] [task]")
        return

    option = sys.argv[1]

    if option == "list":
        print_list()
    elif option == "add":
        if len(sys.argv) < 3:
            print("Please provide a task to add")
        else:
            task = sys.argv[2]
            due_date = None
            priority = None
            if "-d" in sys.argv:
                due_date_index = sys.argv.index("-d") + 1
                due_date = sys.argv[due_date_index]
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid due date format. Please use YYYY-MM-DD.")
                    return
            if "-p" in sys.argv:
                priority_index = sys.argv.index("-p") + 1
                priority = sys.argv[priority_index]
            add_task(task, due_date, priority)
    elif option == "remove":
        if len(sys.argv) < 3:
            print("Please provide the task number to remove")
        else:
            try:
                task_number = int(sys.argv[2])
                remove_task(task_number)
            except ValueError:
                print("Invalid task number")
    elif option == "complete":
        if len(sys.argv) < 3:
            print("Please provide the task number to mark as completed")
        else:
            try:
                task_number = int(sys.argv[2])
                complete_task(task_number)
            except ValueError:
                print("Invalid task number")
    elif option == "clear":
        clear_completed()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
