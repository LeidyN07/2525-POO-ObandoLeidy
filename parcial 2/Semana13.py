import tkinter as tk
from tkinter import messagebox

# Función para agregar un elemento a la lista
def agregar():
    item = entrada.get()  # Obtener el texto del campo de entrada
    if item != "":
        lista.insert(tk.END, item)  # Agregar a la lista
        entrada.delete(0, tk.END)   # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Ingrese un valor antes de agregar.")

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=50)
lista.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
