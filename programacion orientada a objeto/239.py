import tkinter as tk
from tkinter import ttk

class simeven:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label=ttk.Label(self.ventana1, text="seleccione un dia de la semana")
        self.label.grid(column=0, row=0)
        self.opcion=tk.StringVar()
        diasdelasemana=("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
        self.comboy=ttk.Combobox(self.ventana1, width=15, textvariable=self.opcion, values=diasdelasemana)
        self.comboy.current(0)
        self.comboy.grid(column=0, row=1)
        self.boton=ttk.Button(self.ventana1, text="recuperar", command=self.recuperar)
        self.boton.grid(column=0, row=2)
        self.label1=ttk.Label(text="dia seleccionado")
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label1.configure(text=self.opcion.get())


aquitenemotos=simeven()
