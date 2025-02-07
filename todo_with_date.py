import os
from datetime import datetime

# File to store tasks
TASK_FILE = "tasks_new.txt"

def load_tasks():
    """Load tasks from file."""
    tasks = {}
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                date, task, status = line.strip().split("|")
                if date not in tasks:
                    tasks[date] = []
                tasks[date].append({"task": task, "completed": status == "True"})
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as file:
        for date, tasks_list in tasks.items():
            for task in tasks_list:
                file.write(f"{date}|{task['task']}|{task['completed']}\n")

def add_task(tasks):
    """Add a new task."""
    date = input("Enter the date for the task (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
        return

    task = input("Enter a new task: ")
    if date not in tasks:
        tasks[date] = []
    tasks[date].append({"task": task, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    """View all tasks for a specific date."""
    date = input("Enter the date to view tasks (YYYY-MM-DD): ")
    if date in tasks:
        print(f"\nTasks for {date}:")
        for i, task in enumerate(tasks[date], start=1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. {task['task']} {status}")
    else:
        print("⚠️ No tasks available for this date.")

def mark_complete(tasks):
    """Mark a task as completed."""
    date = input("Enter the date to mark tasks as complete (YYYY-MM-DD): ")
    if date in tasks:
        view_tasks(tasks)
        try:
            task_num = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= task_num < len(tasks[date]):
                tasks[date][task_num]['completed'] = True
                save_tasks(tasks)
                print("✅ Task marked as completed!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")
    else:
        print("⚠️ No tasks available for this date.")

def main():
    """Main function to run the to-do list manager."""
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List Manager")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task Complete")
        print("4️⃣ Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
