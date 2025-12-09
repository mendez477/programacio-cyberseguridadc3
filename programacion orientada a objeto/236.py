import tkinter as tk
from tkinter import ttk

class esoeseso:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio=ttk.Radiobutton(self.ventana1, text="varon", variable=self.seleccion, value=1)
        self.radio.grid(column=0, row=0)
        self.radio1=ttk.Radiobutton(self.ventana1, text="mujer", variable=self.seleccion, value=2)
        self.radio1.grid(column=0, row=1)
        self.boton=ttk.Button(self.ventana1, text="seleccionar", command=self.mostrar)
        self.boton.grid(column=0,row=4)
        self.label=ttk.Label(text="")
        self.label.grid(column=0, row=5)
        self.ventana1.mainloop()

    def mostrar(self):
        if self.seleccion.get()==1:
            self.label.configure(text="ha seleccionado varon")

        if self.seleccion.get()==2:
            self.label.configure(text="usted ha seleccionado mujer")

elsklk=esoeseso()

