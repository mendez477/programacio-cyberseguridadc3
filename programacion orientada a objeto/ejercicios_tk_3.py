import tkinter as tk

class tarea:
    def __init__(self):
        self.ventana47=tk.Tk()
        self.label1=tk.Label(self.ventana47, text="Ingrese Un Numero:")
        self.label1.grid(column=0,row=0)
        self.numero=tk.StringVar()
        self.entrtada=tk.Entry(self.ventana47, textvariable=self.numero)
        self.entrtada.grid(column=1, row=0)
        self.label21=tk.Label(self.ventana47, text="Ingrese Un Numero:")
        self.label21.grid(column=0,row=1)
        self.numero2=tk.StringVar()
        self.entrtada2=tk.Entry(self.ventana47, textvariable=self.numero2)
        self.entrtada2.grid(column=1,row=1)
        self.boton=tk.Button(self.ventana47, text="sumar", command=self.hacersuma)
        self.boton.grid(column=0, row=4)
        self.label45=tk.Label(self.ventana47, text="")
        self.label45.grid(column=0, row=5)
        self.ventana47.mainloop()


    def hacersuma(self):
        valor=int(self.numero.get())+ int(self.numero2.get())
        self.label45.config(text=f"la suma es igual a: {valor}")        


tarea555=tarea()                                                                 