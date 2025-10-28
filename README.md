# To-Do List Manager - Midterm Project Report

## Project Information
**Name:** Radian Try Darmawan
**Student ID:** 113021220
**Project Title:** To-Do List Manager
**Course:** Windows Programming
**Semester:** 2nd Semester
**Institution:** Asia University (Taiwan)
**Programming Language:** Python 3
**GUI Framework:** Tkinter
**Date:** 2025

---

## 1. Project Overview

### 1.1 Introduction
This project is a **To-Do List Manager** application developed using Python's Tkinter library. The application provides a simple yet effective way for users to manage their daily tasks with features including adding tasks, deleting tasks, marking tasks as complete or incomplete, and persistent storage using JSON file format.

### 1.2 Project Objectives
The main objectives of this project are:
- Create a user-friendly graphical interface for task management
- Implement CRUD (Create, Read, Update, Delete) operations for tasks
- Enable persistent data storage using JSON format
- Provide visual feedback for task status and priority levels
- Apply beginner to intermediate level programming concepts

---

## 2. Features and Functionality

### 2.1 Core Features (Midterm Requirements)
1. **Add Task** - Users can add new tasks with name, priority, and due date
2. **Delete Task** - Remove selected tasks from the list
3. **Mark Task** - Toggle tasks between complete and incomplete status
4. **Save/Load from File** - Automatic data persistence using `tasks.json`

### 2.2 Additional Features
1. **Priority Levels** - Three priority levels: High, Medium, Low
2. **Due Date Tracking** - Optional due date field for each task
3. **Color-Coded Display** - Visual distinction by priority and completion status:
   - Red text for High priority tasks
   - Orange text for Medium priority tasks
   - Green text for Low priority tasks
   - Gray text for completed tasks
4. **Task Details View** - Double-click to view full task information
5. **Clear All Function** - Remove all tasks with confirmation
6. **Keyboard Shortcuts** - Quick access to common functions
7. **Status Bar** - Helpful hints and instructions

### 2.3 User Interface Elements
- **Input Frame** - For adding new tasks with name, priority, and due date
- **List Display** - Shows all tasks with formatting and color coding
- **Action Buttons** - Clear, labeled buttons for all operations
- **Scrollbar** - For handling large number of tasks
- **Status Bar** - User guidance and tips

---

## 3. Technical Implementation

### 3.1 Technology Stack
- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework (built-in with Python)
- **JSON** - Data storage format
- **datetime** - Timestamp management

### 3.2 File Structure
```
Midterm/
├── todo_list_manager.py    # Main application file
├── tasks.json              # Data storage (auto-generated)
└── README.md               # Project documentation
```

### 3.3 Data Structure
Each task is stored as a JSON object with the following fields:
```json
{
    "name": "Task name",
    "priority": "High/Medium/Low",
    "due_date": "YYYY-MM-DD or No due date",
    "completed": false,
    "created_at": "YYYY-MM-DD HH:MM:SS"
}
```

### 3.4 Key Functions

#### Data Management Functions
- `load_tasks()` - Load tasks from JSON file
- `save_tasks(tasks)` - Save tasks to JSON file
- `refresh_task_list()` - Update the display with current tasks

#### Task Operation Functions
- `add_task()` - Add new task with validation
- `delete_task()` - Remove selected task with confirmation
- `toggle_task_status()` - Mark task as complete/incomplete
- `clear_all_tasks()` - Delete all tasks
- `view_task_details()` - Display detailed task information

---

## 4. User Guide

### 4.1 Getting Started
1. Run the application: `python todo_list_manager.py`
2. The application window will open
3. Data file `tasks.json` will be created automatically

### 4.2 Adding a Task
1. Enter task name in the "Task Name" field
2. Select priority level from dropdown (High/Medium/Low)
3. (Optional) Enter due date in YYYY-MM-DD format
4. Click "Add Task" button or press F1/Enter

### 4.3 Managing Tasks
- **Mark Complete/Incomplete**: Select a task and click "Mark Complete/Incomplete"
- **Delete Task**: Select a task and click "Delete Selected" or press Delete key
- **View Details**: Double-click on any task to see full information
- **Clear All**: Click "Clear All" to remove all tasks (with confirmation)

### 4.4 Keyboard Shortcuts
- `Enter` or `F1` - Add new task
- `Delete` - Delete selected task
- `ESC` - Exit application
- `Double-Click` - View task details

---

## 5. Code Highlights

### 5.1 Input Validation
The application includes comprehensive input validation:
- Task name cannot be empty
- Priority must be selected
- User-friendly error messages with focus management

```python
if not task_name:
    messagebox.showerror("Error", "Task name cannot be empty.")
    task_entry.focus_set()
    return
```

### 5.2 Data Persistence
Automatic JSON file handling with error prevention:
```python
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)
```

### 5.3 Visual Feedback
Color-coded task display based on status:
```python
if task["completed"]:
    task_listbox.itemconfig(idx, fg="gray")
elif priority == "High":
    task_listbox.itemconfig(idx, fg="red")
```

---

## 6. Screenshots and Examples

### 6.1 Main Interface
The application features a clean, organized layout with three main sections:
- Top: Input area for adding new tasks
- Middle: Task list display with scrollbar
- Bottom: Action buttons for task management

### 6.2 Task Display Format
```
[✓] Complete homework (High) - Due: 2025-03-15
[ ] Buy groceries (Medium) - Due: 2025-03-10
[ ] Call dentist (Low) - Due: No due date
```

### 6.3 Sample Task Details
```
Task Details:
━━━━━━━━━━━━━━━━━━━━
Name: Complete homework
Priority: High
Due Date: 2025-03-15
Status: Completed
Created: 2025-03-01 10:30:00
```

---

## 7. Testing and Validation

### 7.1 Test Cases Performed
1. ✓ Add task with all fields filled
2. ✓ Add task without due date
3. ✓ Add task with empty name (error validation)
4. ✓ Add task without priority selected (error validation)
5. ✓ Delete task with confirmation
6. ✓ Cancel delete operation
7. ✓ Mark task as complete
8. ✓ Mark task as incomplete
9. ✓ View task details
10. ✓ Clear all tasks
11. ✓ Application restart (data persistence)
12. ✓ Keyboard shortcuts functionality

### 7.2 Test Results
All test cases passed successfully. The application handles edge cases appropriately and maintains data integrity across sessions.

---

## 8. Challenges and Solutions

### 8.1 Challenge 1: Data Persistence
**Problem:** Ensuring data is saved correctly and loaded on startup
**Solution:** Implemented automatic JSON file creation and validation

### 8.2 Challenge 2: Visual Feedback
**Problem:** Distinguishing between task priorities and statuses
**Solution:** Used color coding system (red, orange, green, gray)

### 8.3 Challenge 3: User Experience
**Problem:** Making the interface intuitive for beginners
**Solution:** Added keyboard shortcuts, status bar hints, and confirmation dialogs

---

## 9. Future Enhancements

### 9.1 Potential Improvements
1. **Task Categories** - Organize tasks by category (Work, Personal, Shopping, etc.)
2. **Search Functionality** - Search tasks by name or priority
3. **Sort Options** - Sort by priority, due date, or creation date
4. **Task Editing** - Modify existing tasks without deleting
5. **Notifications** - Reminder alerts for tasks due soon
6. **Export Function** - Export tasks to CSV or PDF
7. **Dark Mode** - Alternative color scheme option
8. **Task Notes** - Add detailed descriptions to tasks
9. **Recurring Tasks** - Support for daily/weekly/monthly tasks
10. **Statistics** - Display completion rates and productivity metrics

---

## 10. Conclusion

### 10.1 Learning Outcomes
This project successfully demonstrates:
- GUI development using Tkinter
- File I/O operations with JSON
- Event-driven programming
- Input validation and error handling
- User experience design principles
- Code organization and documentation

### 10.2 Personal Reflection
Developing this To-Do List Manager provided valuable hands-on experience with Python GUI programming. The project reinforced concepts of data persistence, user interface design, and software development best practices. The application meets all midterm requirements while providing additional features for enhanced usability.

### 10.3 Project Success
The application successfully fulfills all midterm requirements:
- ✓ Add tasks
- ✓ Delete tasks
- ✓ Mark tasks as complete/incomplete
- ✓ Save and load data from file
- ✓ User-friendly interface
- ✓ Proper error handling

---

## 11. References and Resources

### 11.1 Documentation
- Python Official Documentation: https://docs.python.org/3/
- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
- JSON in Python: https://docs.python.org/3/library/json.html

### 11.2 Learning Resources
- Tkinter GUI programming tutorials
- Python file handling documentation
- Software design patterns and best practices

---

## Appendix A: Installation and Requirements

### System Requirements
- Python 3.6 or higher
- Operating System: Windows/Mac/Linux
- No additional packages required (uses built-in libraries)

### Installation Steps
1. Ensure Python 3.x is installed on your system
2. Download `todo_list_manager.py`
3. Run using command: `python todo_list_manager.py`
4. The application will create `tasks.json` automatically

---

## Appendix B: Source Code Structure

### Main Components
1. **Import Section** - Required libraries
2. **Database Setup** - JSON file initialization
3. **Helper Functions** - Data management utilities
4. **Core Functions** - Task operations (add, delete, mark, etc.)
5. **GUI Setup** - Window and widget configuration
6. **Event Bindings** - Keyboard shortcuts
7. **Application Loop** - Main event loop

### Code Organization
- Clear function names following Python conventions
- Comprehensive comments for each section
- Consistent indentation and formatting
- Error handling with user-friendly messages

---

## Appendix C: Troubleshooting

### Common Issues and Solutions

**Issue 1: Application won't start**
Solution: Verify Python 3.x is installed and tkinter is available

**Issue 2: Tasks not saving**
Solution: Check file permissions in the application directory

**Issue 3: Display issues**
Solution: Ensure proper screen resolution and DPI settings

**Issue 4: JSON file corrupted**
Solution: Delete `tasks.json` and restart application (creates new file)

---

**End of Report**
