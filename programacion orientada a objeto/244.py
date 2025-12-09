import tkinter as tk
from tkinter import ttk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe=ttk.LabelFrame(self.ventana1, text="Login:")
        self.labelframe.grid(column=0,row=0, padx=5, pady=10)
        self.login()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="operaciones")
        self.labelframe1.grid(column=0,row=1, padx=5, pady=10) 
        self.operaciones()
    
    def login(self):
        self.label=ttk.Label(self.labelframe, text="nombre de usuario:")
        self.label.grid(column=0, row=0, padx=4, pady=4)
        self.entrada=ttk.Entry(self.labelframe,)
        self.entrada.grid(column=1, row=0, padx=4, pady=4)
        self.label1=ttk.Label(self.labelframe, text=("ingrese la clave "))
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.entrada1=ttk.Entry(self.labelframe, show="*")
        self.entrada1.grid(column=1, row=1, padx=4, pady=4)
        self.boton=ttk.Button(self.labelframe, text="ingresar")
        self.boton.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        self.boton1=ttk.Button(self.labelframe1, text="agregar usuario")
        self.boton1.grid(column=0, row=0, padx=4,  pady=4)
        self.boton3=ttk.Button(self.labelframe1, text="modificar usuario")
        self.boton3.grid(column=1,row=0, padx=4, pady=4)
        self.boton4=ttk.Button(self.labelframe1, text="borrar usuario")
        self.boton4.grid(column=2, row=0, padx=4, pady=4)


        self.ventana1.mainloop()

aplicacion21=aplicacion()
