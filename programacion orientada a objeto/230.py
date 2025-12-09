import tkinter as tk

class fruta:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.lista=tk.Listbox(self.ventana1)
        self.lista.grid(column=0, row=0)
        self.lista.insert(0,"papa")
        self.lista.insert(1,"manzana")
        self.lista.insert(2,"pera")
        self.lista.insert(3,"sandia")
        self.lista.insert(4, "naranja")
        self.lista.insert(5,"melon")
        self.boton=tk.Button(self.ventana1, text="recuperar", command=self.recuperar)
        self.boton.grid(column=0,row=1)
        self.label=tk.Label(text="seleccionado:")
        self.label.grid(column=0, row=2)
        self.ventana1.mainloop()

    def recuperar(self):
        if len (self.lista.curselection())!=0:
            self.label.configure(text=self.lista.get(self.lista.curselection()[0]))


fruta1=fruta()