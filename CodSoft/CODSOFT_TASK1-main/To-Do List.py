import os
from datetime import datetime

FILE_NAME = "tasks.txt"

class Task:
    def __init__(self, description, priority='Low', deadline=None, completed=False):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = completed

    def __str__(self):
        status = "[Done]" if self.completed else "[Pending]"
        deadline_str = f" | Deadline: {self.deadline}" if self.deadline else ""
        return f"{self.description} | Priority: {self.priority}{deadline_str} | Status: {status}"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file.readlines():
                description, priority, deadline, completed = line.strip().split('|')
                deadline = deadline if deadline != 'None' else None
                completed = True if completed == 'True' else False
                tasks.append(Task(description, priority, deadline, completed))
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task.description}|{task.priority}|{task.deadline}|{task.completed}\n")

def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    description = input("Enter the task: ")
    priority = input("Enter the priority (Low, Medium, High): ")
    deadline = input("Enter the deadline (YYYY-MM-DD) or press Enter to skip: ")
    
    if deadline:
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return
    
    task = Task(description, priority, deadline)
    tasks.append(task)
    print("Task added.")

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    
    if 0 <= task_num < len(tasks):
        task = tasks[task_num]
        task.description = input(f"Enter the updated task (current: {task.description}): ") or task.description
        task.priority = input(f"Enter the updated priority (Low, Medium, High) (current: {task.priority}): ") or task.priority
        task.deadline = input(f"Enter the updated deadline (YYYY-MM-DD) (current: {task.deadline}): ") or task.deadline
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    
    if 0 <= task_num < len(tasks):
        tasks[task_num].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
