# --- START OF FILE interfaces/ventana_login.py ---

import tkinter as tk
from tkinter import messagebox

class VentanaLogin(tk.Toplevel):
    """
    Define la ventana de inicio de sesión (Login).
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Member Login")
        self.geometry("350x450")
        self.resizable(False, False)
        self.config(bg="lightgray")

        # Hacer la ventana modal (bloquea la ventana principal)
        self.transient(parent)
        self.grab_set()

        self.crear_widgets()

    def crear_widgets(self):
        main_frame = tk.Frame(self, bg="white", bd=1, relief="solid")
        main_frame.pack(pady=40, padx=40, fill="both", expand=True)

        header_frame = tk.Frame(main_frame, bg="#0078D7", height=60)
        header_frame.pack(fill="x")
        header_label = tk.Label(header_frame, text="Member login", bg="#0078D7", fg="white", font=("Arial", 16, "bold"))
        header_label.place(relx=0.5, rely=0.5, anchor="center")

        form_frame = tk.Frame(main_frame, bg="white", padx=20, pady=20)
        form_frame.pack(fill="both", expand=True)

        tk.Label(form_frame, text="Username", bg="white", fg="gray", font=("Arial", 10)).pack(anchor="w")
        self.entry_usuario = tk.Entry(form_frame, font=("Arial", 12), width=25, bd=1, relief="solid")
        self.entry_usuario.pack(pady=(0, 15), ipady=5)

        tk.Label(form_frame, text="Password", bg="white", fg="gray", font=("Arial", 10)).pack(anchor="w")
        self.entry_password = tk.Entry(form_frame, show="*", font=("Arial", 12), width=25, bd=1, relief="solid")
        self.entry_password.pack(pady=(0, 10), ipady=5)
        
        options_frame = tk.Frame(form_frame, bg="white")
        options_frame.pack(fill="x")
        
        self.remember_me = tk.IntVar()
        tk.Checkbutton(options_frame, text="Remember me", variable=self.remember_me, bg="white").pack(side="left")
        tk.Label(options_frame, text="Forgot your password?", fg="#0078D7", bg="white", cursor="hand2").pack(side="right")

        login_button = tk.Button(form_frame, text="LOGIN", command=self.validar_login, bg="#0078D7", fg="white", font=("Arial", 12, "bold"), bd=0, width=25, height=2)
        login_button.pack(pady=20)
        
        self.entry_usuario.focus_set()

    def validar_login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if not usuario or not password:
            messagebox.showwarning("Campos Vacíos", "Por favor, ingrese usuario y contraseña.", parent=self)
            return

        if usuario == "admin" and password == "12345":
            messagebox.showinfo("Login Exitoso", f"Bienvenido, {usuario}!", parent=self)
            self.destroy()
            self.parent.deiconify()
            self.parent.abrir_sistema_escolar()
        else:
            messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos.", parent=self)

# --- END OF FILE interfaces/ventana_login.py ---