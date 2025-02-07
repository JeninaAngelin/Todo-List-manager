## Key Components

### 1. **File Handling (tasks.txt)**
   - **Purpose**: The tasks are stored in a file to ensure persistence, meaning tasks will be saved even after the program exits.
   - **Functions**:
     - `load_tasks()`: Loads tasks from the file when the program starts.
     - `save_tasks()`: Saves the tasks back to the file whenever there is a change (like adding or marking a task as complete).

### 2. **Core Functions**
   - **`add_task()`**:
     - Prompts the user to input a new task.
     - Adds the task to the list with a default status of "not completed" (`False`).
     - Saves the updated task list to the file.
   - **`view_tasks()`**:
     - Displays all tasks with their current status.
     - If the task is completed, it shows ✅; otherwise, it shows ❌.
   - **`mark_complete()`**:
     - Displays the list of tasks for the user to choose from.
     - Asks the user to input the task number they want to mark as completed.
     - Validates the task number and updates the status to "completed" (`True`).
     - Saves the updated list back to the file.

### 3. **Error Handling**
   - **Input Validation**:
     - When marking a task as completed, it checks that the entered task number is valid (within the range of available tasks).
     - If the user enters a non-integer value, a `ValueError` is caught, and an error message is shown.
   - **File Existence Check**:
     - Before loading tasks, the program checks if the task file exists using `os.path.exists()`. This prevents errors if the file doesn't exist at first launch.

### 4. **User Interaction (main() function)**
   - **Main Menu**:
     - The program runs in a loop, showing a menu with options:
       1. Add a task
       2. View tasks
       3. Mark task as complete
       4. Exit the program
   - **Choice Handling**:
     - Based on the user's choice, the corresponding function (`add_task`, `view_tasks`, `mark_complete`, or exit) is called.

### 5. **Running the Program**
   - The program starts by calling the `main()` function, which loads the tasks, displays the menu, and allows the user to interact with the system.

---

## Example Flow:
- **Start Program**:
  - On running, the program loads the tasks from the file (if it exists).
  - It displays the main menu for the user to select an action.
  
- **Add Task**:
  - When selecting "1️⃣ Add Task", the user is prompted to enter a task, and it gets added to the list.
  
- **View Tasks**:
  - Selecting "2️⃣ View Tasks" shows all tasks with their current status.
  
- **Mark Task Complete**:
  - Selecting "3️⃣ Mark Task Complete" lets the user pick a task number, and it marks the task as completed.
  
- **Exit**:
  - Selecting "4️⃣ Exit" will end the program.

---

## Summary of Concepts:
This project demonstrates several key Python concepts:
- **Variables and Data Types**: Managing task data in lists and dictionaries.
- **Control Flow**: Using `if-else` and loops for task management and user interaction.
- **Functions and Modules**: Structuring code into functions like `add_task()`, `view_tasks()`, and `mark_complete()`.
- **Collections**: Using lists and dictionaries to store and manage tasks.
- **File Handling**: Reading from and writing to a file (`tasks.txt`) for task persistence.
- **Error Handling**: Handling invalid input and file-related errors with `try-except` and validation checks.
