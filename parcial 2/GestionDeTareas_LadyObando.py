import tkinter as tk
from tkinter import messagebox

# --- CONFIGURACIÓN PRINCIPAL ---
root = tk.Tk()
root.title("Gestión de Tareas 💖")
root.geometry("420x520")
root.config(bg="#ffeef5")  # Fondo rosado pastel
root.resizable(False, False)

# --- FUNCIONES ---
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Escribe una tarea antes de agregarla 💌")

def marcar_completada(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tarea = lista_tareas.get(index)
        if tarea.startswith("💗 "):
            lista_tareas.delete(index)
            lista_tareas.insert(index, tarea[2:])
            lista_tareas.itemconfig(index, fg="#2e2e2e", font=("Comic Sans MS", 11, "normal"))
        else:
            lista_tareas.delete(index)
            lista_tareas.insert(index, "💗 " + tarea)
            lista_tareas.itemconfig(index, fg="#ff6699", font=("Comic Sans MS", 11, "overstrike"))

def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar 💔")

def cerrar_app(event=None):
    if messagebox.askyesno("Salir", "¿Deseas cerrar tu lista de tareas? 💕"):
        root.destroy()

# --- ENCABEZADO ---
titulo = tk.Label(
    root,
    text="🌸 Gestión de Tareas 🌸",
    bg="#ffeef5",
    fg="#ff4081",
    font=("Comic Sans MS", 18, "bold")
)
titulo.pack(pady=15)

# --- ENTRADA DE NUEVA TAREA ---
frame_entrada = tk.Frame(root, bg="#ffeef5")
frame_entrada.pack(pady=10)

entrada_tarea = tk.Entry(
    frame_entrada,
    width=25,
    font=("Comic Sans MS", 11),
    bd=2,
    relief="solid",
    fg="#333"
)
entrada_tarea.grid(row=0, column=0, padx=5, ipady=5)

btn_agregar = tk.Button(
    frame_entrada,
    text="Agregar 💕",
    bg="#ff8fab",
    fg="white",
    activebackground="#ff5c8d",
    font=("Comic Sans MS", 10, "bold"),
    width=10,
    relief="flat",
    command=agregar_tarea
)
btn_agregar.grid(row=0, column=1, padx=5)

# --- LISTA DE TAREAS ---
lista_tareas = tk.Listbox(
    root,
    width=40,
    height=12,
    selectmode=tk.SINGLE,
    font=("Comic Sans MS", 11),
    bg="#fffafc",
    fg="#2e2e2e",
    bd=2,
    relief="solid",
    highlightcolor="#ff8fab"
)
lista_tareas.pack(pady=15)

# --- BOTONES DE ACCIÓN ---
frame_botones = tk.Frame(root, bg="#ffeef5")
frame_botones.pack(pady=5)

btn_completar = tk.Button(
    frame_botones,
    text="✅ Completada",
    bg="#c8e6c9",
    fg="#2e7d32",
    activebackground="#81c784",
    font=("Comic Sans MS", 10, "bold"),
    width=13,
    relief="flat",
    command=marcar_completada
)
btn_completar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(
    frame_botones,
    text="🗑 Eliminar",
    bg="#ff8fab",
    fg="white",
    activebackground="#f06292",
    font=("Comic Sans MS", 10, "bold"),
    width=13,
    relief="flat",
    command=eliminar_tarea
)
btn_eliminar.grid(row=0, column=1, padx=10)

# --- PIE DE PÁGINA ---
footer = tk.Label(
    root,
    text="💜 ¡Gracias por pintar esta tarea, Lady Obando! 💜",
    bg="#ffeef5",
    fg="#a64ca6",
    font=("Comic Sans MS", 9, "italic")
)
footer.pack(side="bottom", pady=15)

# --- ATAJOS DE TECLADO ---
root.bind("<Return>", agregar_tarea)
root.bind("<c>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

# --- EJECUTAR ---
root.mainloop()
