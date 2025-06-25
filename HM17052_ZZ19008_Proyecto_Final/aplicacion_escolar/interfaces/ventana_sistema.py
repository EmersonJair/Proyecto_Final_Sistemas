# --- START OF FILE interfaces/ventana_sistema.py ---

import tkinter as tk
from tkinter import ttk, messagebox
from .ventana_materias import VentanaMaterias # Importación relativa

# Datos de ejemplo
DATOS_ALUMNOS = [
    (1, "Jorge Alvarez Santana", "Licenciatura en Sistemas Computacionales", "Matutino"),
    (2, "Hugo Flores Alvarez", "Licenciatura en Psicología", "Vespertino"),
    (3, "Irma Hernández Escamilla", "Licenciatura en Derecho", "Vespertino"),
    (4, "Claudia Alvarez Hernández", "Licenciatura en Trabajo Social", "Nocturno"),
    (5, "Josue Israel Alvarez", "Medicina", "Matutino")
]

class VentanaSistema(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("El Sistema Escolar")
        self.geometry("700x450")

        self.crear_widgets()
        self.cargar_datos_en_tabla()
        
        self.protocol("WM_DELETE_WINDOW", self.parent.cerrar_aplicacion)

    def crear_widgets(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        movimientos_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Movimientos", menu=movimientos_menu)
        movimientos_menu.add_command(label="Ver Materias del Alumno", command=self.abrir_ventana_materias)
        movimientos_menu.add_separator()
        movimientos_menu.add_command(label="Salir", command=self.parent.cerrar_aplicacion)
        
        reportes_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Reportes", menu=reportes_menu)
        reportes_menu.add_command(label="Imprimir Lista", command=lambda: messagebox.showinfo("Imprimir", "Función no implementada.", parent=self))

        form_frame = tk.Frame(self, padx=10, pady=10)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="Matrícula", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_matricula = tk.Entry(form_frame, state="readonly", width=40)
        self.entry_matricula.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Nombre", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre = tk.Entry(form_frame, state="readonly", width=40)
        self.entry_nombre.grid(row=1, column=1, padx=5)

        tk.Label(form_frame, text="Carrera", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_carrera = tk.Entry(form_frame, state="readonly", width=40)
        self.entry_carrera.grid(row=2, column=1, padx=5)

        tk.Label(form_frame, text="Turno", font=("Arial", 12, "bold")).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_turno = tk.Entry(form_frame, state="readonly", width=40)
        self.entry_turno.grid(row=3, column=1, padx=5)
        
        table_frame = tk.Frame(self, padx=10, pady=10)
        table_frame.pack(fill="both", expand=True)

        columnas = ("matricula", "nombre", "carrera", "turno")
        self.tabla = ttk.Treeview(table_frame, columns=columnas, show="headings")
        
        self.tabla.heading("matricula", text="Matrícula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("carrera", text="Carrera")
        self.tabla.heading("turno", text="Turno")
        
        self.tabla.column("matricula", width=60, anchor="center")
        self.tabla.column("nombre", width=200)
        self.tabla.column("carrera", width=250)
        self.tabla.column("turno", width=100)
        
        self.tabla.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        self.tabla.bind("<<TreeviewSelect>>", self.mostrar_seleccion_en_formulario)

    def cargar_datos_en_tabla(self):
        for alumno in DATOS_ALUMNOS:
            self.tabla.insert("", "end", values=alumno)

    def mostrar_seleccion_en_formulario(self, event):
        for selected_item in self.tabla.selection():
            item = self.tabla.item(selected_item)
            record = item['values']
            
            for entry, value in zip([self.entry_matricula, self.entry_nombre, self.entry_carrera, self.entry_turno], record):
                entry.config(state="normal")
                entry.delete(0, tk.END)
                entry.insert(0, value)
                entry.config(state="readonly")
    
    def abrir_ventana_materias(self):
        if not self.tabla.selection():
            messagebox.showwarning("Sin Selección", "Por favor, seleccione un alumno de la tabla.", parent=self)
            return
        VentanaMaterias(self)

# --- END OF FILE interfaces/ventana_sistema.py ---