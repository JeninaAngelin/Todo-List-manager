import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("|")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['task']} {status}")

def mark_complete(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the to-do list manager."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()