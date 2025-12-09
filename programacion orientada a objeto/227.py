import tkinter as tk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.select=tk.IntVar()
        self.check=tk.Checkbutton(self.ventana1, text="python", variable=self.select)
        self.check.grid(column=0, row=0)
        self.select1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text="c++", variable=self.select1)
        self.check1.grid(column=0,row=1)
        self.select2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1, text="Java", variable=self.select2)
        self.check2.grid(column=0, row=2)
        self.boton=tk.Button(self.ventana1, text="verificar", command=self.verificar)
        self.boton.grid(column=0, row=4)
        self.label=tk.Label( text="cantidad:")
        self.label.grid(column=0, row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=0
        if self.select.get()==1:
            cant+=1
        if self.select1.get()==1:
            cant+=1
        if self.select2.get()==1:
            cant+=1
        self.label.configure(text="cantidad:"+str(cant))

aplicacion1=aplicacion()

        