import tkinter as tk
from tkinter import messagebox, simpledialog

print("Made by terminal coding! https://www.youtube.com/channel/UCk-dlnkUaRonMEyG-tsbioQ")

class GUI:
    def __init__(self):
        self.task_manager = TaskManager()

        self.root = tk.Tk()
        self.root.title("Task Manager")

        # Theme settings
        self.theme = "white"  # Default theme is white

        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=2, column=0, sticky=tk.E)

        self.title_label = tk.Label(self.root, text="Title:")
        self.title_label.grid(row=0, column=0, sticky=tk.W)

        self.title_entry = tk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.desc_label = tk.Label(self.root, text="Description:")
        self.desc_label.grid(row=1, column=0, sticky=tk.W)

        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, sticky=tk.W)

        self.list_button = tk.Button(self.root, text="List Tasks", command=self.list_tasks)
        self.list_button.grid(row=1, column=3, sticky=tk.W)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=3, sticky=tk.W)

        # Font settings
        fontsize = self.get_font_size()
        font = ("Arial", fontsize)

        self.title_label.configure(font=font)
        self.desc_label.configure(font=font)
        self.title_entry.configure(font=font)
        self.desc_entry.configure(font=font)
        self.settings_button.configure(font=font)
        self.add_button.configure(font=font)
        self.list_button.configure(font=font)
        self.complete_button.configure(font=font)

        self.root.bind("<Configure>", self.on_window_resize)

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")

        theme_label = tk.Label(settings_window, text="Select Theme:")
        theme_label.pack()

        theme_var = tk.StringVar(value=self.theme)
        theme_radio_white = tk.Radiobutton(settings_window, text="White", variable=theme_var, value="white")
        theme_radio_white.pack()
        theme_radio_black = tk.Radiobutton(settings_window, text="Black", variable=theme_var, value="black")
        theme_radio_black.pack()

        save_button = tk.Button(settings_window, text="Save", command=lambda: self.save_settings(theme_var.get()))
        save_button.pack()

    def save_settings(self, theme):
        self.theme = theme
        self.apply_theme()

    def apply_theme(self):
        if self.theme == "black":
            self.root.configure(background="black")
            self.settings_button.configure(foreground="black", background="black", highlightbackground="black")
            self.add_button.configure(foreground="black", background="black", highlightbackground="black")
            self.list_button.configure(foreground="black", background="black", highlightbackground="black")
            self.complete_button.configure(foreground="black", background="black", highlightbackground="black")
            self.title_entry.configure(foreground="white", background="black")
            self.desc_entry.configure(foreground="white", background="black")
        else:
            self.root.configure(background="white")
            self.settings_button.configure(foreground="black", background="white", highlightbackground="white")
            self.add_button.configure(foreground="black", background="white", highlightbackground="white")
            self.list_button.configure(foreground="black", background="white", highlightbackground="white")
            self.complete_button.configure(foreground="black", background="white", highlightbackground="white")
            self.title_entry.configure(foreground="black", background="white")
            self.desc_entry.configure(foreground="black", background="white")

        fontsize = self.get_font_size()
        font = ("Arial", fontsize)

        self.title_label.configure(font=font)
        self.desc_label.configure(font=font)
        self.title_entry.configure(font=font)
        self.desc_entry.configure(font=font)
        self.settings_button.configure(font=font)
        self.add_button.configure(font=font)
        self.list_button.configure(font=font)
        self.complete_button.configure(font=font)

    def get_font_size(self):
        window_width = self.root.winfo_width()
        fontsize = max(int(window_width / 40), 10)  # Adjust the divisor to control the font size
        return fontsize

    def on_window_resize(self, event):
        self.apply_theme()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()

        if title == "":
            messagebox.showwarning("Warning", "Please enter a task title.")
            return

        self.task_manager.add_task(title, description)
        messagebox.showinfo("Success", f"Task '{title}' has been added successfully.")

        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def list_tasks(self):
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            messagebox.showinfo("No Tasks", "You have no tasks.")
        else:
            task_list = "\n".join(tasks)
            messagebox.showinfo("Task List", task_list)

    def complete_task(self):
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            messagebox.showinfo("No Tasks", "You have no tasks.")
            return

        task_idx = simpledialog.askinteger("Complete Task", "Enter the index of the task to mark as completed:")

        if task_idx is None:
            return

        try:
            task_title = self.task_manager.mark_task_completed(task_idx)
            messagebox.showinfo("Success", f"Task '{task_title}' marked as completed.")

            # Delete the completed task from the list
            self.task_manager.remove_task(task_idx)

        except IndexError:
            messagebox.showwarning("Warning", "Invalid task index. Please provide a valid task index.")

    def run(self):
        self.apply_theme()
        self.root.mainloop()


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def get_all_tasks(self):
        return [
            f"{idx + 1}. {task.title}: {task.description} ({'Completed' if task.completed else 'Not Completed'})"
            for idx, task in enumerate(self.tasks)]

    def mark_task_completed(self, task_idx):
        task = self.get_task_by_index(task_idx)
        task.mark_completed()
        return task.title

    def remove_task(self, task_idx):
        del self.tasks[task_idx]

    def get_task_by_index(self, task_idx):
        return self.tasks[task_idx]


if __name__ == "__main__":
    gui = GUI()
    gui.run()
