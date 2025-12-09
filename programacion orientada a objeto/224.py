import tkinter as tk 

class perreria:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.select=tk.IntVar()
        self.select.set(2)
        self.radio=tk.Radiobutton(self.ventana1,text="varon", variable=self.select, value=1)
        self.radio.grid(column=0, row=0)
        self.radio1=tk.Radiobutton(self.ventana1, text="mujer", variable=self.select,value=2)
        self.radio1.grid(column=0, row=1)
        self.boton=tk.Button(self.ventana1, text="mostrar seleccion", command=self.mostrar)
        self.boton.grid(column=0, row=3)
        self.label=tk.Label(text="opcion seleccionada")
        self.label.grid(column=0, row=5)
        self.ventana1.mainloop()

    def mostrar(self):
        if self.select.get()==1:
            self.label.configure(text="usted es un caballero")
        if self.select.get()==2:
            self.label.configure(text="usted es una dama")

esoeseso=perreria()