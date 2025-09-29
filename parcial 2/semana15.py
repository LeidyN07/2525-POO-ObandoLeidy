import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Funciones principales
# -------------------------------

def add_task(event=None):
    """Añadir nueva tarea a la lista"""
    task = entry.get().strip()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        status_label.config(text="Tarea añadida con éxito ✅", fg="green")
    else:
        status_label.config(text="No puedes añadir una tarea vacía ⚠️", fg="red")


def mark_completed(event=None):
    """Marcar la tarea seleccionada como completada"""
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)

        # Si ya tiene el check, no lo duplicamos
        if not task.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, f"✔ {task}")
            status_label.config(text="Tarea completada 🎉", fg="blue")
    except IndexError:
        status_label.config(text="Selecciona una tarea para marcarla ⚠️", fg="red")


def delete_task(event=None):
    """Eliminar la tarea seleccionada"""
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        status_label.config(text="Tarea eliminada 🗑️", fg="orange")
    except IndexError:
        status_label.config(text="Selecciona una tarea para eliminarla ⚠️", fg="red")


# -------------------------------
# Interfaz Gráfica
# -------------------------------
root = tk.Tk()
root.title("Mi Lista de Tareas 📝")
root.geometry("400x450")
root.config(bg="#f0f8ff")  # Fondo azul claro

# Campo de entrada
entry = tk.Entry(root, font=("Arial", 14), bg="#e6f7ff")
entry.pack(pady=10, padx=10, fill="x")

# Botones
btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=add_task, bg="#a3d2ca")
add_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(btn_frame, text="Marcar Completada", command=mark_completed, bg="#5eaaa8")
complete_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=delete_task, bg="#f05945")
delete_btn.grid(row=0, column=2, padx=5)

# Lista de tareas
listbox = tk.Listbox(root, font=("Arial", 14), selectbackground="#ffdab9")
listbox.pack(pady=10, padx=10, fill="both", expand=True)

# Mensajes de estado
status_label = tk.Label(root, text="", bg="#f0f8ff", fg="red", font=("Arial", 10, "italic"))
status_label.pack(pady=5)

# -------------------------------
# Eventos extra
# -------------------------------
entry.bind("<Return>", add_task)          # Enter añade tarea
listbox.bind("<Double-1>", mark_completed) # Doble clic marca tarea
root.bind("<Delete>", delete_task)         # Tecla Delete elimina tarea

# -------------------------------
# Iniciar aplicación
# -------------------------------
root.mainloop()
