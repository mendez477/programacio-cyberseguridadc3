import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox as mb

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelfrma=ttk.LabelFrame(self.ventana1, text="suma de numeros")
        self.labelfrma.grid(column=0, row=0, padx=10, pady=10)
        self.agregar_componentes()
        self.agregar_menu()
        self.ventana1.mainloop()

    def agregar_componentes(self):
        self.label1=ttk.Label(self.labelfrma, text= "ingrese un valor")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.numero=tk.StringVar()
        self.entrada=ttk.Entry(self.labelfrma, textvariable=self.numero)
        self.entrada.grid(column=1, row=0, padx=5, pady=5)
        self.label2=ttk.Label(self.labelfrma, text="ingrese un valor")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.numero1=tk.StringVar()
        self.entrada1=ttk.Entry(self.labelfrma, width=20, textvariable=self.numero1)
        self.entrada1.grid(column=1, row=1, padx=5, pady=5)
        self.boton=ttk.Button(self.labelfrma, text="sumar", command=self.sumar)
        self.boton.grid(column=1, row=2, padx=5, pady=5, sticky="we")

    def agregar_menu(self):
        self.menu24=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menu24)
        self.opciones=tk.Menu(self.menu24, tearoff=0)
        self.opciones.add_command(label="acerca de ...", command=self.acerca)
        self.menu24.add_cascade(label="opciones", menu=self.opciones)

    def sumar(self):
        if self.numero.get()=="" or self.numero1.get()=="":
            mb.showerror("cuidado","no puede dejar los cuadros de entrada vacio")
        else: 
            suma=int(self.entrada.get())+ int(self.entrada1.get())
            self.ventana1.title("la suma es "+str(suma))

        
    def acerca(self):
        mb.showinfo("informacion", "este programa fue desarrolado para el apredizaje de python")



aplicacionsas=aplicacion()