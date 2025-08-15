"""
Verificación de pregunta correcta de tres opciones
"""

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Verificación de pregunta")
        self.ventana1.geometry("300x300")
        #Creación de enunciado de pregunta 
        self.label1=tk.Label(self.ventana1,text="Pregunta Nr01:")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana1,text="La suma de 10+5:")
        self.label2.grid(column=0, row=1)
        #Opciones de la pregunta
        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=tk.Radiobutton(self.ventana1,text="A) 20", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=2)
        self.radio2=tk.Radiobutton(self.ventana1,text="B) 17", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=3)
        self.radio3=tk.Radiobutton(self.ventana1,text="C) 15", variable=self.seleccion, value=3)
        self.radio3.grid(column=0, row=4)
        self.boton1=tk.Button(self.ventana1, text="Comprobar respuesta", command=self.mostrarresultado)
        self.boton1.grid(column=0, row=5)
        self.label3=tk.Label(self.ventana1,text="opcion seleccionada")
        self.label3.grid(column=0, row=6)
        self.ventana1.mainloop()

    def mostrarresultado(self):
        if self.seleccion.get()==3:
            self.label3.configure(text="Su respuesta es correcta")
        else:
            self.label3.configure(text="Su respuesta es incorrecta")

aplicacion1=Aplicacion()