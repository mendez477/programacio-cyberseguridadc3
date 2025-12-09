import tkinter as tk

class aplicaccion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.select=tk.IntVar()
        self.check=tk.Checkbutton(self.ventana1, text="estas de acuerdo con los terminos y condiciones?",
                                   variable=self.select,command=self.cambiar_estado)
        self.check.grid(column=0, row=0)
        self.boton=tk.Button(self.ventana1, text="entra", state="disabled", command=self.ingresar)
        self.boton.grid(column=0, row=1)
        self.ventana1.mainloop()

    def cambiar_estado(self):
        if self.select.get()==1:
            self.boton.configure(state="normal")
        if self.select.get()==0:
            self.boton.configure(state="disabled")

    def ingresar(self):
        self.ventana1.title("ingresando....")

aplicaccion1=aplicaccion()
