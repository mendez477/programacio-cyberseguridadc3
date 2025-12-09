import tkinter as tk

class lafrutanotaehfregadera:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scroll=tk.Scrollbar(self.ventana1,orient=tk.VERTICAL)
        self.lista=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll.set)
        self.lista.grid(column=0, row=0)
        self.scroll.configure(command=self.lista.yview)
        self.scroll.grid(column=1, row=0, sticky='NS')
        self.lista.insert(0,"papa")
        self.lista.insert(1,"manzana")
        self.lista.insert(2,"pera")
        self.lista.insert(3,"sandia")
        self.lista.insert(4, "naranja")
        self.lista.insert(5,"melon")
        self.lista.insert(6,"kiwi")
        self.lista.insert(7,"fresa")
        self.lista.insert(8,"cereza")
        self.lista.insert(9,"mango")
        self.lista.insert(10,"guayaba")
        self.boton=tk.Button(self.ventana1, text="recuperar", command=self.recuperar)
        self.boton.grid(column=0, row=1)
        self.labael=tk.Label(self.ventana1, text="seleccionado:")
        self.labael.grid(column=0, row=2)
        self.ventana1.mainloop()

    def recuperar(self):
        if len (self.lista.curselection())!=0:
            todas=''
            for posicion in self.lista.curselection():
                todas+=self.lista.get(posicion)+"\n"
            self.labael.configure(text=todas)


esoeseso=lafrutanotaehfregadera()

