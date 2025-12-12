import tkinter as tk
from tkinter import ttk, messagebox
import re
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # vacío si no configuraste contraseña
    database="trabajofinalpool"
)

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Registro de Usuario")

        self.frame = ttk.LabelFrame(self.ventana1, text="Nuevo Usuario")
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        # Usuario
        ttk.Label(self.frame, text="Ingrese su usuario").grid(column=0, row=0)
        self.usuario = tk.StringVar()
        tk.Entry(self.frame, width=30, textvariable=self.usuario).grid(column=0, row=1)

        # Clave
        ttk.Label(self.frame, text="Ingrese su clave").grid(column=0, row=2)
        self.clave = tk.StringVar()
        tk.Entry(self.frame, width=30, textvariable=self.clave, show="*").grid(column=0, row=3)

        # Botón
        ttk.Button(self.frame, text="Ingresar", command=self.ingresar).grid(column=0, row=4, pady=10)

        self.ventana1.mainloop()

    def ingresar(self):
        usuario = self.usuario.get().strip()
        clave = self.clave.get()

        # Validaciones
        if len(clave) < 8:
            messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres")
            return
        if not re.search("[a-z]", clave):
            messagebox.showerror("Error", "La contraseña debe contener al menos una letra minúscula")
            return
        if not re.search(r"[0-9]", clave):
            messagebox.showerror("Error", "La contraseña debe contener al menos un número")
            return
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", clave):
            messagebox.showerror("Error", "La contraseña debe contener al menos un carácter especial")
            return

        # Guardar en la base de datos
        try:
            cursor = conexion.cursor()
            consulta = "INSERT INTO usuarios (usuario, clave) VALUES (%s, %s)"
            valores = (usuario, clave)
            cursor.execute(consulta, valores)
            conexion.commit()
            cursor.close()

            messagebox.showinfo("Éxito", f"Usuario '{usuario}' registrado correctamente en la base de datos")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar en la base de datos: {e}")

if __name__ == "__main__":
    app = Aplicacion()