import tkinter as tk

class tarea:
    def __init__(self):
        self.ventana27=tk.Tk()
        
        self.dato25=tk.StringVar()
        self.entrada=tk.Entry(self.ventana27, textvariable=self.dato25)
        self.entrada.grid(column=0, row=2)
        self.boton=tk.Button(self.ventana27, text="aceptar", command=self.copiar)
        self.boton.grid(column=0, row=4)
        self.labe1=tk.Label(self.ventana27, text="")
        self.labe1.grid(column=0, row=6)
        self.ventana27.mainloop()



    def copiar(self):
        copiarq=self.dato25.get()
        self.labe1.config(text=copiarq)

tarea25=tarea()