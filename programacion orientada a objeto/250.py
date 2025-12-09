import tkinter as tk
from tkinter import messagebox as mb
import sys

class apicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.ventana1.mainloop()

    def agregar_menu(self):
        self.menu24=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menu24)
        self.opciones=tk.Menu(self.menu24, tearoff=0)
        self.opciones.add_command(label="salir", command=self.salir)
        self.menu24.add_cascade(label="opciones", menu=self.opciones)


    def salir(self):
        respuesta=mb.askyesno("cuidado", "quieres salir del programa")
        if respuesta==True:
            sys.exit()

klklk=apicacion()