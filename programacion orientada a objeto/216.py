import tkinter as tk

class klk:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.valor = 1
        self.ventana1.title("controles button y label")

        self.label1 = tk.Label(self.ventana1, text=str(self.valor))
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="blue")
        # BOTONES
        self.boton1 = tk.Button(self.ventana1, text="incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2 = tk.Button(self.ventana1, text=" decrementar", command=self.decrementar )
        self.boton2.grid(column=0, row=2)
       
        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)


    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)

klk1=klk()
