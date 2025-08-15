import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
        self.ventana1.geometry("300x200")
        self.label1=tk.Label(self.ventana1, text=self.valor ,padx=10  , pady=10)
        self.label1.grid(column=3, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1, text="Incrementar", padx=10  , pady=10, command=self.incrementar)
        self.boton1.grid(column=1, row=0)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", padx=10  , pady=10, command=self.decrementar)
        self.boton2.grid(column=2, row=0)

        self.ventana1.mainloop()


    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


aplicacion1=Aplicacion()