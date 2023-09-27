import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

# Function to delete a task
def delete_task():
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)
        tasks.pop(selected_task)
    except IndexError:
        pass

# Create and configure widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Add Task", width=40, command=add_task)
button_add.pack()

button_delete = tk.Button(root, text="Delete Task", width=40, command=delete_task)
button_delete.pack()

# Run the main event loop
root.mainloop()
