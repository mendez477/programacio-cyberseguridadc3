import tkinter as tk 

class lamisma:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="ingrese su nombre de usuario")
        self.label1.grid(column=0,row=0)
        self.usuario=tk.StringVar()
        self.entrada=tk.Entry(self.ventana1, width=25, textvariable=self.usuario)
        self.entrada.grid(column=1, row=0)
        self.label2=tk.Label(self.ventana1, text="ingrese la clave")
        self.label2.grid(column=0,row=1)
        self.clave=tk.StringVar()
        self.entrada2=tk.Entry(self.ventana1, width=25, textvariable=self.clave, show="*")
        self.entrada2.grid(column=1, row=1)
        self.boton=tk.Button(self.ventana1, text="ingresar", command=self.ingresar)
        self.boton.grid(column=1, row=4)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.usuario.get()=="juan"  and self.clave.get()=="abc123":
            self.ventana1.title("correcto")

        else:
            self.ventana1.title("incorrecto")

aplicacion=lamisma()