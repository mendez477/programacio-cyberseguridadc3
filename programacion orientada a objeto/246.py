import tkinter as tk 
from tkinter import ttk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton=ttk.Button(self.ventana1, text="boton1")
        self.boton.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton1=ttk.Button(self.ventana1, text="boton2")
        self.boton1.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton2=ttk.Button(self.ventana1, text="boton3")
        self.boton2.pack(side=tk.TOP, fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana1, text="boton4")
        self.boton3.pack(side=tk.LEFT)
        self.boton4=ttk.Button(self.ventana1, text="boton5")
        self.boton4.pack(side=tk.RIGHT)
        self.boton5=ttk.Button(self.ventana1, text="boton6")
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana1, text="boton7")
        self.boton6.pack(side=tk.RIGHT)
        self.ventana1.mainloop()

apple=aplicacion()
