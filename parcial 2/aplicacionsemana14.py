"""
Agenda Personal Bonita y Personalizada
--------------------------------------
- Estilo moderno con colores pastel y tipografía amigable.
- Botones con emojis: ➕ para agregar, 🗑️ para eliminar, 📅 para calendario.
- Treeview con encabezado colorido.
- Entradas y frames claros y organizados.
- Código entendible y comentado.

Requisitos: Python 3.x (sin paquetes externos).
"""

import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import date, datetime

# ---------------------------
# DatePicker simple
# ---------------------------
class DatePicker(tk.Toplevel):
    """Selector de fecha personalizado"""
    def __init__(self, master, callback, init_date=None):
        super().__init__(master)
        self.title("Seleccionar fecha")
        self.resizable(False, False)
        self.callback = callback
        self.configure(bg="#FFFDE7")  # fondo pastel

        # Fecha inicial
        if init_date:
            try:
                self.current_date = date.fromisoformat(init_date)
            except:
                self.current_date = date.today()
        else:
            self.current_date = date.today()
        self.year = self.current_date.year
        self.month = self.current_date.month

        self._build_widgets()
        self.transient(master)
        self.grab_set()
        self.wait_window()

    def _build_widgets(self):
        # Header con botones de mes
        header = tk.Frame(self, bg="#FFFDE7")
        header.pack(padx=8, pady=6, fill="x")
        prev_btn = tk.Button(header, text="<", width=3, command=self._prev_month, bg="#FFECB3")
        prev_btn.pack(side="left")
        self.month_label = tk.Label(header, text="", width=20, bg="#FFFDE7", font=("Segoe UI", 10, "bold"))
        self.month_label.pack(side="left", padx=6)
        next_btn = tk.Button(header, text=">", width=3, command=self._next_month, bg="#FFECB3")
        next_btn.pack(side="left")

        # Días de la semana
        days_frame = tk.Frame(self, bg="#FFFDE7")
        days_frame.pack(padx=8)
        for d in ["Lu","Ma","Mi","Ju","Vi","Sa","Do"]:
            tk.Label(days_frame, text=d, width=4, bg="#FFFDE7").pack(side="left")

        # Cuadrícula de días
        self.calendar_frame = tk.Frame(self, bg="#FFFDE7")
        self.calendar_frame.pack(padx=8, pady=(4,8))

        # Cancelar
        cancel_btn = tk.Button(self, text="Cancelar", command=self.destroy, bg="#FFCDD2")
        cancel_btn.pack(pady=(0,8))

        self._draw_calendar()

    def _draw_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        self.month_label.config(text=f"{calendar.month_name[self.month]} {self.year}")
        cal = calendar.monthcalendar(self.year, self.month)
        for r, week in enumerate(cal):
            for c, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text=" ", width=4, bg="#FFFDE7").grid(row=r, column=c)
                else:
                    tk.Button(self.calendar_frame, text=str(day), width=4,
                              command=lambda d=day: self._select_day(d), bg="#FFF9C4").grid(row=r, column=c)

    def _select_day(self, day):
        selected = date(self.year, self.month, day)
        self.callback(selected.isoformat())
        self.destroy()

    def _prev_month(self):
        self.month -=1
        if self.month < 1:
            self.month = 12
            self.year -=1
        self._draw_calendar()

    def _next_month(self):
        self.month +=1
        if self.month >12:
            self.month =1
            self.year +=1
        self._draw_calendar()

# ---------------------------
# Aplicación principal
# ---------------------------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        root.title("📅 Agenda Personal")
        root.geometry("700x450")
        root.configure(bg="#FFF8E1")

        self.events = []  # lista de eventos
        self._next_id = 1

        self._build_ui()
        self._populate_sample()  # datos de ejemplo

    def _build_ui(self):
        # --- Estilo ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('Treeview', background="#FFF3E0", foreground="black", rowheight=28, fieldbackground="#FFF3E0")
        style.configure('Treeview.Heading', background="#FFB74D", foreground="white", font=('Segoe UI', 10, 'bold'))

        # --- Frame de lista ---
        list_frame = tk.Frame(self.root, bg="#FFF8E1")
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        columns = ("fecha", "hora", "desc")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("desc", text="Descripción")
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=70, anchor="center")
        self.tree.column("desc", width=480, anchor="w")
        self.tree.pack(side="left", fill="both", expand=True)
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="left", fill="y")

        # --- Frame de entradas ---
        bottom_frame = tk.Frame(self.root, bg="#FFF8E1")
        bottom_frame.pack(fill="x", padx=10, pady=(0,10))

        entry_frame = tk.LabelFrame(bottom_frame, text="Agregar nuevo evento", bg="#FFFDE7", font=("Segoe UI", 10, "bold"), padx=10, pady=10)
        entry_frame.pack(side="left", fill="x", expand=True)

        # Fecha
        tk.Label(entry_frame, text="Fecha:", bg="#FFFDE7").grid(row=0, column=0, sticky="w")
        self.fecha_var = tk.StringVar()
        tk.Entry(entry_frame, textvariable=self.fecha_var, width=14).grid(row=0, column=1, padx=4)
        tk.Button(entry_frame, text="📅", command=self._open_datepicker, bg="#FFE082").grid(row=0, column=2, padx=4)

        # Hora
        tk.Label(entry_frame, text="Hora:", bg="#FFFDE7").grid(row=1, column=0, sticky="w")
        self.hora_var = tk.StringVar()
        tk.Entry(entry_frame, textvariable=self.hora_var, width=14).grid(row=1, column=1, padx=4)

        # Descripción
        tk.Label(entry_frame, text="Descripción:", bg="#FFFDE7").grid(row=2, column=0, sticky="nw")
        self.desc_var = tk.StringVar()
        tk.Entry(entry_frame, textvariable=self.desc_var, width=40).grid(row=2, column=1, columnspan=2, pady=4, sticky="w")

        # --- Frame de botones ---
        actions_frame = tk.Frame(bottom_frame, bg="#FFF8E1")
        actions_frame.pack(side="right", padx=4)

        tk.Button(actions_frame, text="➕ Agregar Evento", command=self._on_add, bg="#81C784", fg="white").pack(fill="x", pady=(0,6))
        tk.Button(actions_frame, text="🗑️ Eliminar Evento", command=self._on_delete, bg="#E57373", fg="white").pack(fill="x", pady=(0,6))
        tk.Button(actions_frame, text="Salir ❌", command=self.root.quit, bg="#B0BEC5").pack(fill="x")

        self.desc_var.trace_add("write", lambda *args: None)  # placeholder

    # ---------------------------
    # Funciones de DatePicker
    # ---------------------------
    def _open_datepicker(self):
        DatePicker(self.root, callback=lambda d: self.fecha_var.set(d), init_date=self.fecha_var.get())

    # ---------------------------
    # Validación y agregar
    # ---------------------------
    def _validate_time(self, timestr):
        try:
            datetime.strptime(timestr, "%H:%M")
            return True
        except:
            return False

    def _on_add(self):
        fecha = self.fecha_var.get().strip()
        hora = self.hora_var.get().strip()
        desc = self.desc_var.get().strip()
        if not fecha:
            messagebox.showwarning("Fecha requerida", "Introduce la fecha del evento.")
            return
        try:
            date.fromisoformat(fecha)
        except:
            messagebox.showerror("Fecha inválida", "Formato inválido. Usa YYYY-MM-DD o selecciona desde el calendario.")
            return
        if not hora or not self._validate_time(hora):
            messagebox.showerror("Hora inválida", "Formato de hora inválido. Usa HH:MM")
            return
        if not desc:
            messagebox.showwarning("Descripción requerida", "Introduce una descripción.")
            return

        # Agregar evento
        event = {"id": self._next_id, "fecha": fecha, "hora": hora, "desc": desc}
        self._next_id += 1
        self.events.append(event)
        self.tree.insert("", "end", iid=str(event["id"]), values=(fecha, hora, desc))
        self.fecha_var.set("")
        self.hora_var.set("")
        self.desc_var.set("")

    # ---------------------------
    # Eliminar evento
    # ---------------------------
    def _on_delete(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Selecciona un evento", "Selecciona primero el evento a eliminar.")
            return
        item_id = sel[0]
        values = self.tree.item(item_id, "values")
        if messagebox.askyesno("Confirmar eliminación", f"¿Eliminar este evento?\n{values[0]} {values[1]} - {values[2]}"):
            self.tree.delete(item_id)
            self.events = [e for e in self.events if str(e["id"]) != item_id]

    # ---------------------------
    # Ejemplo de datos iniciales
    # ---------------------------
    def _populate_sample(self):
        sample = [
            {"fecha": date.today().isoformat(), "hora": "09:00", "desc": "Estudiar Matemáticas"},
            {"fecha": date.today().isoformat(), "hora": "15:00", "desc": "Reunión equipo"},
            {"fecha": date.today().isoformat(), "hora": "18:30", "desc": "Ejercicio / caminar"},
        ]
        for s in sample:
            s["id"] = self._next_id
            self._next_id +=1
            self.events.append(s)
            self.tree.insert("", "end", iid=str(s["id"]), values=(s["fecha"], s["hora"], s["desc"]))


# ---------------------------
# Ejecutar aplicación
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
