import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana25=tk.Tk()
        self.boton=tk.Button(self.ventana25, width=15, text="varon", command=self.varon)
        self.boton.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana25, width=15, text="mujer", command=self.mujer)
        self.boton1.grid(column=0, row=1)
        self.ventana25.mainloop()

    def varon(self):
        self.ventana25.title("selecciono varon")

    def mujer(self):
        self.ventana25.title("selecciono mujer")



aplicacion25=aplicacion()