import tkinter as tk 

class esoes:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(text="ingrese un numero:")
        self.label1.grid(column=0, row=0)
        self.dato=tk.StringVar()
        self.entrada=tk.Entry(self.ventana1, width=10, textvariable=self.dato)
        self.entrada.grid(column=0, row=1)
        self.boton=tk.Button(self.ventana1, text="calcular cuadrado", command=self.calculo)
        self.boton.grid(column=0, row=2)
        self.label2=tk.Label(self.ventana1, text="resultado")
        self.label2.grid(column=0, row=3)
        self.ventana1.mainloop()


    def calculo(self):
        valor=int(self.dato.get())
        cuadrado=valor*valor
        self.label2.configure(text=cuadrado)
    
esoeseso=esoes()