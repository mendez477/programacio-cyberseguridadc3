import tkinter as tk
from tkinter import ttk 

class asison:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label=ttk.Label(text="ingrese su usuario:")
        self.label.grid(column=0, row=0)
        self.usuario=tk.StringVar()
        self.entrada=ttk.Entry(self.ventana1, width=30, textvariable=self.usuario)
        self.entrada.grid(column=0, row=1)
        self.label1=ttk.Label(text="ingrese su clave")
        self.label1.grid(column=1, row=0)
        self.passw=tk.StringVar()
        self.entrada2=ttk.Entry(self.ventana1, width=30, textvariable=self.passw, show="*")
        self.entrada2.grid(column=1, row=1)
        self.boton=ttk.Button(self.ventana1, text="ingresar", command=self.ingresar)
        self.boton.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.usuario.get()=="juan" and self.passw.get()=="abc123":
            self.ventana1.title("correcto")
        else:
            self.ventana1.title("incorrecto")

cirujano_nortuno=asison()
