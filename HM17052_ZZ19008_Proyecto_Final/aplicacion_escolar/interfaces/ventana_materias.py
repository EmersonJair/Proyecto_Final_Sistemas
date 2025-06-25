# --- START OF FILE interfaces/ventana_materias.py ---

import tkinter as tk
from tkinter import messagebox

class VentanaMaterias(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Materias del Alumno")
        self.geometry("500x300")
        self.resizable(False, False)
        self.config(bg="#ECECEC")

        self.transient(parent)
        self.grab_set()

        self.crear_widgets()

    def crear_widgets(self):
        main_frame = tk.Frame(self, bg="#E0E0E0", bd=2, relief="groove")
        main_frame.place(x=20, y=40, width=460, height=240)
        
        label_alumno = tk.Label(self, text="  ALUMNO  ", bg="white", relief="ridge", bd=2, font=("Arial", 10, "bold"))
        label_alumno.place(x=40, y=30)
        
        btn_matematicas = tk.Button(main_frame, text="MATEMATICA", command=lambda: self.materia_seleccionada("Matemática"))
        btn_matematicas.place(x=50, y=30)
        
        btn_ingles = tk.Button(main_frame, text="INGLES", command=lambda: self.materia_seleccionada("Inglés"))
        btn_ingles.place(x=300, y=30)
        
        btn_ciencias = tk.Button(main_frame, text="CIENCIAS", command=lambda: self.materia_seleccionada("Ciencias"))
        btn_ciencias.place(x=180, y=100)

        btn_sociales = tk.Button(main_frame, text="SOCIALES", command=lambda: self.materia_seleccionada("Sociales"))
        btn_sociales.place(x=50, y=170)
        
        btn_lenguaje = tk.Button(main_frame, text="LENGUAJE", command=lambda: self.materia_seleccionada("Lenguaje"))
        btn_lenguaje.place(x=300, y=170)

    def materia_seleccionada(self, nombre_materia):
        messagebox.showinfo("Materia Seleccionada", f"Se ha registrado el interés en la materia:\n\n{nombre_materia}", parent=self)

# --- END OF FILE interfaces/ventana_materias.py ---