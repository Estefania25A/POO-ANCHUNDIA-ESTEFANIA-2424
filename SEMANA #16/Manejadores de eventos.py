import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

tasks = []

# Campo de entrada
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Funciones para añadir, completar y eliminar tareas
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "No puedes añadir una tarea vacía.")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})
        tasks[selected_task_index]["completed"] = True
    except IndexError:
        messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index]
    except IndexError:
        messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea.")

# Botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Atajos de teclado
root.bind('<Return>', lambda event: add_task())
root.bind('<c>', lambda event: complete_task())
root.bind('<d>', lambda event: delete_task())
root.bind('<Delete>', lambda event: delete_task())
root.bind('<Escape>', lambda event: root.quit())

root.mainloop()
