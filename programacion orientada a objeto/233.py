import tkinter as tk 

class aplicacio:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="ingrese su nombre")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entrada=tk.Entry(self.ventana1, width=30,textvariable=self.nombre)
        self.entrada.grid(column=0, row=1)
        self.label2=tk.Label(self.ventana1, text="seleccione un pais")
        self.label2.grid(column=0, row=2)
        self.lista=tk.Listbox(self.ventana1)
        self.lista.grid(column=0, row=3)
        self.lista.insert(0, "puerto rico")
        self.lista.insert(1, "cuba")
        self.lista.insert(2,"jamaica")
        self.lista.insert(3,"haiti")
        self.lista.insert(4,"mexico")
        self.boton=tk.Button(self.ventana1, text="listo", command=self.mostrar)
        self.boton.grid(column=1, row=5)
        self.ventana1.mainloop()

    def mostrar(self):
        if (len (self.lista.curselection()))!=0:
            self.ventana1.title("nombre:"+self.nombre.get()+"  pais:"+self.lista.get(self.lista.curselection()[0]))


aplicacion12=aplicacio()