import tkinter as tk 

class tarea:
    def __init__(self):
    
        self.vetana25=tk.Tk()
        self.boton=tk.Button(self.vetana25, text="1", command=self.uno)
        self.boton.grid(column=0,row=0)
        self.boton1=tk.Button(self.vetana25, text="2", command=self.dos)
        self.boton1.grid(column=0,row=1)
        self.boton2=tk.Button(self.vetana25, text="3", command=self.tres)
        self.boton2.grid(column=0,row=2)
        self.boton3=tk.Button(self.vetana25, text="4", command=self.cuatro)
        self.boton3.grid(column=0,row=3)
        self.boton4=tk.Button(self.vetana25, text="5", command=self.cinco)
        self.boton4.grid(column=0,row=4)

        self.numeros=""
        self.label=tk.Label(self.vetana25, text=self.numeros)
        self.label.grid(column=0, row=6)
        self.vetana25.mainloop()

    def uno(self):
        self.numeros=self.numeros+"1"
        self.label.config(text=self.numeros)

    def dos(self):
        self.numeros=self.numeros+"2"
        self.label.config(text=self.numeros)

    def tres(self):
        self.numeros=self.numeros+"3"
        self.label.config(text=self.numeros)

    def cuatro(self):
        self.numeros=self.numeros+"4"
        self.label.config(text=self.numeros)

    def cinco(self):
        self.numeros=self.numeros+"5"
        self.label.config(text=self.numeros)


tareak=tarea()

