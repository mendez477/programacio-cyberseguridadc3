import tkinter as tk 
from tkinter import ttk 

class tarea:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label=ttk.Label(self.ventana1, text="ingrese su nombre")
        self.label.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entrada=ttk.Entry(self.ventana1, width=25, textvariable=self.nombre)
        self.entrada.grid(column=1, row=0)
        self.paises=tk.StringVar()
        paisesdelcaribe=("republica dominicana","cuba", "jamaica","puerto rico")
        self.combo=ttk.Combobox(self.ventana1, width=15, textvariable=self.paises, values=paisesdelcaribe)
        self.combo.grid(column=0, row=3)
        self.boton=ttk.Button(self.ventana1, width=10, text="aceptar", command=self.mostrar)
        self.boton.grid(column=1, row=6)
        self.ventana1.mainloop()

    def mostrar(self):
        self.ventana1.title("nombre:"+self.nombre.get() + "  pais:"+ self.paises.get())
 
aplicacion=tarea()