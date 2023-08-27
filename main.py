import tkinter as tk
from tkinter import messagebox, simpledialog

# Class for the graphical user interface
class GUI:
    def __init__(self):
        # Initialize the task manager
        self.task_manager = TaskManager()

        # Initialize the main application window
        self.root = tk.Tk()
        self.root.title("Task Manager")

        # ... [Other initialization code] ...

    # Method to open the settings window
    def open_settings(self):
        # Create a new window for settings
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")

        # ... [Settings window UI code] ...

    # Method to save the selected theme from settings
    def save_settings(self, theme):
        self.theme = theme
        self.apply_theme()

    # Method to apply the selected theme
    def apply_theme(self):
        # ... [Theme application code] ...

    # ... [Other methods] ...

    # Method to run the GUI application
    def run(self):
        self.apply_theme()
        self.root.mainloop()

# Class to represent a task
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

# Class to manage tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def get_all_tasks(self):
        # ... [Code to list all tasks] ...

    def mark_task_completed(self, task_idx):
        # ... [Code to mark a task as completed] ...

    def remove_task(self, task_idx):
        # ... [Code to remove a task] ...

    def get_task_by_index(self, task_idx):
        # ... [Code to get a task by index] ...

# Main entry point of the program
if __name__ == "__main__":
    gui = GUI()
    gui.run()
