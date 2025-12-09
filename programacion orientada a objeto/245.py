#Mediante dos controles de tipo LabelFrame implementar la siguiente interfaz visual
import tkinter as tk 
import tkinter.ttk as ttk

class tarea:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="articulo")
        self.labelframe1.grid(column=0, row=0, padx=20, pady=20)
        self.label1=ttk.Label(self.labelframe1, text="codigo del articulo")
        self.label1.grid(column=0, row=0)
        self.codigo=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelframe1, width=15, textvariable=self.codigo)
        self.entrada1.grid(column=1, row=0)
        self.label2=ttk.Label(self.labelframe1, text="descripcion")
        self.label2.grid(column=0, row=1)
        self.descripcion=tk.StringVar()
        self.entrada2=ttk.Entry(self.labelframe1, width=15, textvariable=self.descripcion)
        self.entrada2.grid(column=1, row=1)
        self.label3=ttk.Label(self.labelframe1, text="precio")
        self.label3.grid(column=0, row=2)
        self.precio=tk.StringVar()
        self.entrada3=ttk.Entry(self.labelframe1, width=15, textvariable=self.precio)
        self.entrada3.grid(column=1, row=2)
        self.labelframe2=ttk.LabelFrame(self.ventana1, text="operaciones")
        self.labelframe2.grid(column=0, row=1, padx=20, pady=20)
        self.boton1=ttk.Button(self.labelframe2, text="alta")
        self.boton1.grid(column=0, row=0, padx=10, pady=10)
        self.boton2=ttk.Button(self.labelframe2, text="baja")
        self.boton2.grid(column=1, row=0, padx=10, pady=10)
        self.boton3=ttk.Button(self.labelframe2, text="modificacion")
        self.boton3.grid(column=2, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

fuegocharo=tarea()
