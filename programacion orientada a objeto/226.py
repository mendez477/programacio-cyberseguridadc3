import tkinter as tk

class tarea:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.select=tk.IntVar()
        self.select.set(1)
        self.radio=tk.Radiobutton(self.ventana1, text="rojo", variable=self.select, value=1)
        self.radio.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text="verde", variable=self.select, value=2)
        self.radio2.grid(column=0, row=1)
        self.radio3=tk.Radiobutton(self.ventana1, text="azul", variable=self.select, value=3)
        self.radio3.grid(column=0, row=3)
        self.boton=tk.Button(self.ventana1, text= "cambiar color", command=self.color)
        self.boton.grid(column=1, row=5)
        self.ventana1.mainloop()

    def color(self):
        if self.select.get()==1:
            self.ventana1.configure(bg="red")

        if self.select.get()==2:
            self.ventana1.configure(bg="green")

        if self.select.get()==3:
            self.ventana1.configure(bg="blue")





apli=tarea()