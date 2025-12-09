import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="ingrese su nombre")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entrada=tk.Entry(self.ventana1, width=20, textvariable=self.dato)
        self.entrada.grid(column=1, row=0)
        self.boton1=tk.Button(self.ventana1, text="ingresar", command=self.ingresar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        self.ventana1.title(self.dato.get())


aplicacion12=aplicacion()