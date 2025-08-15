# Importar la librería
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Agregar alumnos")
        self.ventana1.geometry("300x200")

        # Creación de labels ingreso valores 
        self.label1 = tk.Label(self.ventana1, text="Nombre:")
        self.label1.grid(column=0, row=0)

        self.label2 = tk.Label(self.ventana1, text="Nota:")
        self.label2.grid(column=0, row=1)

        # Ingreso de valores
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        # Lista de alumnos
        self.lista = []

        # Botón para agregar alumnos
        self.boton1 = tk.Button(self.ventana1, text="Agregar", command=self.agregaestudiante)
        self.boton1.grid(column=0, row=2)

        # Mostrar lista de alumnos
        self.label3 = tk.Label(self.ventana1, text="Resultado:")
        self.label3.grid(column=0, row=3, columnspan=2)

        self.ventana1.mainloop()

    def agregaestudiante(self):
        nombre = self.dato1.get()
        try:
            nota = float(self.dato2.get())
            self.lista.append((nombre, nota))

            # Mostrar todos los alumnos en la etiqueta
            texto_resultado = "Lista de alumnos:\n" + "\n".join([f"{n[0]}: {n[1]}" for n in self.lista])
            self.label3.configure(text=texto_resultado)
        except ValueError:
            self.label3.configure(text="Error: Nota no válida")

# Instancia de clase
aplicacion1 = Aplicacion()
