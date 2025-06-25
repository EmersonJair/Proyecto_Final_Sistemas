# --- START OF FILE main.py ---

import tkinter as tk
from interfaces.ventana_login import VentanaLogin
from interfaces.ventana_sistema import VentanaSistema

class App(tk.Tk):
    """
    Clase principal que controla el flujo de la aplicación.
    """
    def __init__(self):
        super().__init__()
        self.title("Aplicación Principal")
        self.withdraw()  # Ocultamos la ventana raíz principal al inicio

        # Iniciar con la ventana de login
        VentanaLogin(self)

    def abrir_sistema_escolar(self):
        """
        Este método es llamado desde la ventana de login cuando
        las credenciales son correctas.
        """
        VentanaSistema(self)

    def cerrar_aplicacion(self):
        """Cierra toda la aplicación."""
        self.quit()

if __name__ == "__main__":
    app = App()
    app.mainloop()

# --- END OF FILE main.py ---