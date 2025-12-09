import tkinter as tk 

class tarea:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.select=tk.IntVar()
        self.check=tk.Checkbutton(self.ventana1, text="chrome", variable=self.select, command=self.todos)
        self.check.grid(column=0, row=0)
        self.select2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1, text="zafari", variable=self.select2, command=self.todos)
        self.check2.grid(column=0, row=1)
        self.select3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1, text="edge", variable=self.select3, command=self.todos)
        self.check3.grid(column=0, row=2)
        self.select4=tk.IntVar()
        self.check4=tk.Checkbutton(self.ventana1, text="fire", variable=self.select4, command=self.todos)
        self.check4.grid(column=0, row=3)
        self.ventana1.mainloop()

    def todos(self):
        cadena=""
        if self.select.get()==1:
            cadena+="chrome -"
        if self.select2.get()==1:
            cadena+="zafari -"
        if self.select3.get()==1:
            cadena+="edge -"
        if self.select4.get()==1:
            cadena+="fire -"

        self.ventana1.title(cadena)

akjskajsk=tarea()
