import tkinter as tk
import sys

class esamisma:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("prueba")
        self.ventana1.geometry("300x500")
        self.label1=tk.Label(self.ventana1, text="sistema de facturacion")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1, text="2018")
        self.label2.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="finalizar", command=self.finalizar)
        self.boton1.grid(column=0, row=2)
        self.ventana1.resizable(False, False)
        self.ventana1.mainloop()


    def finalizar(self):
        sys.exit(0)


aja=esamisma()