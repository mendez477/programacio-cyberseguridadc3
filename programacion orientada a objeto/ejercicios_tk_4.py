import tkinter as tk 
from tkinter import ttk

class tarea:
    def __init__(self):
        self.ventana24=tk.Tk()
        self.lista=tk.Listbox(self.ventana24)
        self.lista.grid(column=0, row=3)
        self.lane=tk.Label(self.ventana24, text="Lista de compras:")
        self.lane.grid(column=0, row=0)
        self.lista.insert(0,"ajo")
        self.lista.insert(1,"mantequilla")
        self.lista.insert(2,"queso")
        self.lista.insert(3,"manzana")
        self.lista.insert(4, "jamon")
        self.lista.insert(5,"canela")
        self.lista.insert(6,"limon")
        self.mas=tk.StringVar()
        self.entrada=tk.Entry(self.ventana24, textvariable=self.mas)
        self.boton=tk.Button(self.ventana24, text="nuevo", width=25, command=self.nuevo_producto)
        self.entrada.grid(column=1, row=5)
        self.boton.grid(column=1, row=6)
        self.lane2=tk.Label(self.ventana24, text="nuevo producto")
        self.lane2.grid(column=0, row=5)
        self.ventana24.mainloop()

    def nuevo_producto(self):
        nuevo=self.mas.get()
        if nuevo.strip():
            self.lista.insert(tk.END,nuevo)
            self.mas.set("")

aplicacion=tarea()