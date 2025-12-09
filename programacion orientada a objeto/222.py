import tkinter as tk

class tarea:
    def __init__(self):
        self.ventana54=tk.Tk()
        self.ventana54.title("la suma")
        self.numero1=tk.StringVar()
        self.entrada=tk.Entry(self.ventana54, width=25,textvariable=self.numero1)
        self.entrada.grid(column=0, row=0, padx=4,pady=4)
        self.numero2=tk.StringVar()
        self.entrada1=tk.Entry(self.ventana54, width=25, textvariable=self.numero2) 
        self.entrada1.grid(column=0, row=2, padx=4, pady=4) 
        self.boton=tk.Button(self.ventana54, text="sumar", command=self.sumatoria)
        self.boton.grid(column=1, row=4)
        self.label1=tk.Label(self.ventana54, text="")
        self.label1.grid(column=0,row=8)
        self.ventana54.mainloop()

    def sumatoria(self):
        valor=int (self.numero1.get())+ int(self.numero2.get())
        self.label1.config(text=valor)


aplicacion=tarea()