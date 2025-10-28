#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# ---------------- JSON Database ----------------
DATA_FILE = "tasks.json"

# Create file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# ---------------- Helper Functions ----------------
def load_tasks():
    """Load tasks from JSON file"""
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh_task_list():
    """Refresh the task listbox with current tasks"""
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()

    for idx, task in enumerate(tasks):
        # Format: [✓] Task name (Priority) - Due: date
        status = "✓" if task["completed"] else " "
        priority = task["priority"]
        task_name = task["name"]
        due_date = task.get("due_date", "No due date")

        display_text = f"[{status}] {task_name} ({priority}) - Due: {due_date}"
        task_listbox.insert(tk.END, display_text)

        # Change color based on completion status
        if task["completed"]:
            task_listbox.itemconfig(idx, fg="gray")
        elif priority == "High":
            task_listbox.itemconfig(idx, fg="red")
        elif priority == "Medium":
            task_listbox.itemconfig(idx, fg="orange")
        else:
            task_listbox.itemconfig(idx, fg="green")

# ---------------- Add Task Function ----------------
def add_task(event=None):
    """Add a new task to the list"""
    task_name = task_entry.get().strip()
    priority = priority_var.get()
    due_date = due_date_entry.get().strip()

    # Validation
    if not task_name:
        messagebox.showerror("Error", "Task name cannot be empty.")
        task_entry.focus_set()
        return

    if priority == "Select Priority":
        messagebox.showerror("Error", "Please select a priority level.")
        priority_combo.focus_set()
        return

    # Load existing tasks
    tasks = load_tasks()

    # Create new task
    new_task = {
        "name": task_name,
        "priority": priority,
        "due_date": due_date if due_date else "No due date",
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Add and save
    tasks.append(new_task)
    save_tasks(tasks)

    # Refresh display
    refresh_task_list()

    # Clear input fields
    task_entry.delete(0, tk.END)
    priority_var.set("Select Priority")
    due_date_entry.delete(0, tk.END)
    task_entry.focus_set()

    messagebox.showinfo("Success", "Task added successfully!")

# ---------------- Delete Task Function ----------------
def delete_task():
    """Delete selected task from the list"""
    selected_indices = task_listbox.curselection()

    if not selected_indices:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return

    # Confirm deletion
    confirm = messagebox.askyesno("Confirm Delete",
                                   "Are you sure you want to delete this task?")
    if not confirm:
        return

    # Get selected index
    index = selected_indices[0]

    # Load tasks and delete
    tasks = load_tasks()
    deleted_task = tasks.pop(index)
    save_tasks(tasks)

    # Refresh display
    refresh_task_list()

    messagebox.showinfo("Success", f"Task '{deleted_task['name']}' deleted successfully!")

# ---------------- Mark Task as Complete/Incomplete ----------------
def toggle_task_status():
    """Toggle completion status of selected task"""
    selected_indices = task_listbox.curselection()

    if not selected_indices:
        messagebox.showwarning("Warning", "Please select a task to mark.")
        return

    # Get selected index
    index = selected_indices[0]

    # Load tasks and toggle status
    tasks = load_tasks()
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks(tasks)

    # Refresh display
    refresh_task_list()

    status = "completed" if tasks[index]["completed"] else "incomplete"
    messagebox.showinfo("Success", f"Task marked as {status}!")

# ---------------- Clear All Tasks ----------------
def clear_all_tasks():
    """Clear all tasks from the list"""
    tasks = load_tasks()

    if not tasks:
        messagebox.showinfo("Info", "No tasks to clear.")
        return

    confirm = messagebox.askyesno("Confirm Clear",
                                   "Are you sure you want to delete ALL tasks?")
    if confirm:
        save_tasks([])
        refresh_task_list()
        messagebox.showinfo("Success", "All tasks cleared!")

# ---------------- View Task Details ----------------
def view_task_details(event=None):
    """View details of selected task"""
    selected_indices = task_listbox.curselection()

    if not selected_indices:
        return

    index = selected_indices[0]
    tasks = load_tasks()
    task = tasks[index]

    details = f"""
Task Details:
━━━━━━━━━━━━━━━━━━━━
Name: {task['name']}
Priority: {task['priority']}
Due Date: {task['due_date']}
Status: {'Completed' if task['completed'] else 'Pending'}
Created: {task['created_at']}
    """

    messagebox.showinfo("Task Details", details)

# ---------------- Initialize Window ----------------
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("700x500")
root.resizable(False, False)

# ---------------- Variables ----------------
task_var = tk.StringVar()
priority_var = tk.StringVar(value="Select Priority")
due_date_var = tk.StringVar()

# ---------------- Keyboard Shortcuts ----------------
root.bind("<Escape>", lambda e: root.destroy())
root.bind("<F1>", add_task)
root.bind("<Delete>", lambda e: delete_task())
root.bind("<Return>", add_task)
root.bind("<Double-Button-1>", view_task_details)

# ---------------- Top Frame (Input Area) ----------------
input_frame = tk.LabelFrame(root, text="Add New Task", padx=10, pady=10)
input_frame.pack(fill="x", padx=10, pady=10)

# Task Name
tk.Label(input_frame, text="Task Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
task_entry = tk.Entry(input_frame, textvariable=task_var, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

# Priority
tk.Label(input_frame, text="Priority:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
priority_combo = ttk.Combobox(input_frame, textvariable=priority_var, state="readonly",
                              values=["Select Priority", "High", "Medium", "Low"],
                              width=15)
priority_combo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Due Date
tk.Label(input_frame, text="Due Date:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
due_date_entry = tk.Entry(input_frame, textvariable=due_date_var, width=15)
due_date_entry.grid(row=1, column=3, sticky="w", padx=5, pady=5)
tk.Label(input_frame, text="(YYYY-MM-DD)", fg="gray").grid(row=1, column=4, sticky="w")

# Add Button
add_button = tk.Button(input_frame, text="Add Task (F1)", command=add_task,
                       bg="#4CAF50", fg="white", width=15)
add_button.grid(row=2, column=1, pady=10)

# Configure column weights
input_frame.columnconfigure(1, weight=1)

# ---------------- Middle Frame (Task List) ----------------
list_frame = tk.LabelFrame(root, text="Task List", padx=10, pady=10)
list_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Scrollbar and Listbox
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                          font=("Courier", 10), height=12)
task_listbox.pack(fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

# ---------------- Bottom Frame (Action Buttons) ----------------
button_frame = tk.Frame(root, padx=10, pady=10)
button_frame.pack(fill="x")

tk.Button(button_frame, text="Mark Complete/Incomplete", command=toggle_task_status,
          bg="#2196F3", fg="white", width=20).pack(side="left", padx=5)

tk.Button(button_frame, text="Delete Selected (Del)", command=delete_task,
          bg="#f44336", fg="white", width=20).pack(side="left", padx=5)

tk.Button(button_frame, text="View Details", command=view_task_details,
          bg="#FF9800", fg="white", width=15).pack(side="left", padx=5)

tk.Button(button_frame, text="Clear All", command=clear_all_tasks,
          bg="#9E9E9E", fg="white", width=12).pack(side="right", padx=5)

# ---------------- Status Bar ----------------
status_bar = tk.Label(root, text="Double-click a task to view details | Press ESC to exit",
                     bd=1, relief="sunken", anchor="w")
status_bar.pack(fill="x", side="bottom")

# ---------------- Initial Load ----------------
refresh_task_list()
task_entry.focus_set()

# ---------------- Run Application ----------------
root.mainloop()
