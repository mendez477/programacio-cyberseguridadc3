import tkinter as tk
from tkinter import ttk

class lacallebotafuego:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("controles button y label")
        self.label=ttk.Label(self.ventana1, text=self.valor)
        self.label.grid(column=0,row=0)
        self.label.configure(foreground="red")
        self.boton=ttk.Button(self.ventana1,text="ingremetar", command=self.incremetar)
        self.boton.grid(column=0, row=1)
        self.boton1=ttk.Button(self.ventana1, text="incrementar", command=self.disminuir)
        self.boton1.grid(column=0, row=2)
        self.ventana1.mainloop()
    
    def incremetar(self):
        self.valor=self.valor+1
        self.label.config(text=self.valor)

    def disminuir(self):
        self.valor=self.valor-1
        self.label.config(text=self.valor)

esomismo=lacallebotafuego()

