"""
Cálculo de número mayor con interfaz gráfica
"""
#Importar la libreria 
import tkinter as tk

#Creción de clase

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Calculo de nro mayor")
        self.ventana1.geometry("300x200")
        #Creación de labels ingreso valores 
        self.label1=tk.Label(self.ventana1,text="Ingrese V1:")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1,text="Ingrese V2:")
        self.label2.grid(column=1, row=0)
        #Ingreso de cuadros de texto 
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        #Presentación de resultado 
        self.label3=tk.Label(self.ventana1,text="Resultado")
        self.label3.grid(column=2, row=1)
        #Boton que ejecuta acción
        self.boton1=tk.Button(self.ventana1, text="Calcular mayor", command=self.calcularmayor)
        self.boton1.grid(column=0, row=2)
        self.ventana1.mainloop()

        #Funcion de calcula mayor
    def calcularmayor(self):
        valor1=float(self.dato1.get())
        valor2=float(self.dato2.get())
        if (valor1 > valor2):
            self.label3.configure(text=f"El nro mayor es {valor1}")
        else:
             self.label3.configure(text=f"El nro mayor es {valor2}")

#Instancia de clase
aplicacion1=Aplicacion()