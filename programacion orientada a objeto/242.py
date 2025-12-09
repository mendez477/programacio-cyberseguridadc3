import tkinter as tk 
import tkinter.ttk as ttk
import sys

class tarea:
    def __init__(self):
        self.ventana1=tk.Tk()
        menu24=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menu24)
        opciones1=tk.Menu(menu24,)
        opciones1.add_command(label="cambiar tamaño", command=self.cambiartamaño)
        opciones1.add_command(label="salir", command=self.salir)
        menu24.add_cascade(label="opciones",menu=opciones1)

        self.label1=ttk.Label(self.ventana1, text="ingrese ancho")
        self.label1.grid(column=0, row=0)
        self.ancho=tk.StringVar()
        self.entrada1=ttk.Entry(self.ventana1, width=15, textvariable=self.ancho)
        self.entrada1.grid(column=1, row=0)

        self.label2=ttk.Label(self.ventana1, text="ingrese alto")
        self.label2.grid(column=0, row=1)
        self.alto=tk.StringVar()
        self.entrada2=ttk.Entry(self.ventana1, width=15, textvariable=self.alto)
        self.entrada2.grid(column=1, row=1)
        self.boton1=ttk.Button(self.ventana1, text="cambiar tamaño", command=self.cambiartamaño)
        self.boton1.grid(column=0, row=2)

        self.ventana1.mainloop()

    def cambiartamaño(self):
        ancho=self.ancho.get()
        alto=self.alto.get()
        self.ventana1.geometry(ancho+"x"+alto)

    def salir(self):
        sys.exit()

fuegocharo=tarea()