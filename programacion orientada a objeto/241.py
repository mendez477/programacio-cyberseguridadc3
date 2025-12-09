import tkinter as tk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menu24=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menu24)
        opciones1=tk.Menu(menu24,)
        opciones1.add_command(label="rojo", command=self.fijarrojo)
        opciones1.add_command(label="verde", command=self.fijarverde)
        opciones1.add_command(label="azul", command=self.fijarazul)
        menu24.add_cascade(label="colores",menu=opciones1)
        opciones2=tk.Menu(menu24)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1024x800", command=self.ventanagrande)
        menu24.add_cascade(label="tamaños", menu=opciones2)
        self.ventana1.mainloop()

        
    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarazul(self):
        self.ventana1.configure(background="blue")
    
    def fijarverde(self):
        self.ventana1.configure(background="green")

    def ventanagrande(self):
        self.ventana1.geometry("1024x800")

    def ventanachica(self):
        self.ventana1.geometry("640x480")


fuegocharo=aplicacion()