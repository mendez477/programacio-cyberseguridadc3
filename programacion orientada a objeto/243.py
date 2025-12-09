import tkinter as tk 
from tkinter import ttk

class lanotabox:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("prueba del control notebook")
        self.cuaderno=ttk.Notebook(self.ventana1)

        #pagina 1
        self.pagina1=tk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text="button")
        self.label1=ttk.Label(self.pagina1, text="la clase button nos permirte capturar el clic y lanzar un mentodo")
        self.label1.grid(column=0, row=0)
        self.boton1=ttk.Button(self.pagina1, text="ejemplo de boton ")
        self.boton1.grid(column=0, row=1)
        self.boton2=ttk.Button(self.pagina1, text="ejemplo de boton inactivo", state="disable")
        self.boton2.grid(column=0, row=2)

        #pagina2
        self.pagina2=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text="label")
        self.label2=ttk.Label(self.pagina2, text="La clase Label permite mostrar un mensaje en la ventana")
        self.label2.grid(column=0,row=0)
        self.label3=ttk.Label(self.pagina2, text="con los caracteres \\n podemos hacer un salto de línea dentro de la Label")
        self.label3.grid(column=0, row=1)

        #pagina3
        self.pagina3=ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina3, text="entry")
        self.label4=ttk.Label(self.pagina3, text="""En tkinter el control de entrada de datos por teclado se llama Entry.\n
Con este control aparece el típico recuadro que cuando se le da foco aparece el cursor en forma intermitente\n
esperando que el operador escriba algo por teclado.""")
        self.label4.grid(column=0,row=0)
        self.entrada=ttk.Entry(self.pagina3, width=30)
        self.entrada.grid(column=0, row=1)

        self.cuaderno.grid(column=0, row=0)
        self.ventana1.mainloop()


papapa=lanotabox()