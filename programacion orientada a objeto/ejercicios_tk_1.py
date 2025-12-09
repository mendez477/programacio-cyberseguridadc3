import tkinter as tk 

class tarea:

    def __init__(self):
        self.ventana27=tk.Tk()
        self.label12=tk.Label(text="bienvenido maestro")
        self.label12.grid(column=0, row=0)
        self.label125=tk.Label(text="gusta una taza de cafe?")
        self.label125.grid(column=1, row=1)
        self.ventana27.mainloop()

tareatk=tarea()