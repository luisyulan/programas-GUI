import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba del control Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        #-------------------Configuración de Pag nr1-------------------
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Suma")
        #Valores de label
        self.label1=ttk.Label(self.pagina1, text="Ingrese Prime valor: ")
        self.label1.grid(column=0, row=0)
        self.label2=ttk.Label(self.pagina1, text="Ingrese Segundo valor: ")
        self.label2.grid(column=1, row=0)
        #Entry 
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.pagina1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.pagina1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        #boton de suma
        self.boton1=ttk.Button(self.pagina1, text="Suma" , command=self.suma)
        self.boton1.grid(column=0, row=2)
        #label de resultado 
        self.label3=ttk.Label(self.pagina1, text="Resultado ")
        self.label3.grid(column=1, row=2)
        #Entry 
        #-------------------Configuración Pag nr2---------------------------------------------------------
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Resta")
        self.label4=ttk.Label(self.pagina2, text="Ingrese Prime valor: ")
        self.label4.grid(column=0, row=0)
        self.label5=ttk.Label(self.pagina2, text="Ingrese Segundo valor: ")
        self.label5.grid(column=1, row=0)
        #Entry 
        self.dato3=tk.StringVar()
        self.entry3=tk.Entry(self.pagina2, width=10, textvariable=self.dato3)
        self.entry3.grid(column=0, row=1)
        self.dato4=tk.StringVar()
        self.entry4=tk.Entry(self.pagina2, width=10, textvariable=self.dato4)
        self.entry4.grid(column=1, row=1)
        #boton de suma
        self.boton2=ttk.Button(self.pagina2, text="Resta" , command=self.resta)
        self.boton2.grid(column=0, row=2)
        #label de resultado 
        self.label6=ttk.Label(self.pagina2, text="Resultado ")
        self.label6.grid(column=1, row=2)

        #-------------------Configuración Pag nr3---------------------------------------------------------
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Entry")
        self.label7=ttk.Label(self.pagina3, text="""En tkinter el control de entrada de datos por teclado se llama Entry.\n
Con este control aparece el típico recuadro que cuando se le da foco aparece el cursor en forma intermitente\n
esperando que el operador escriba algo por teclado.""")
        self.label7.grid(column=0, row=0)
        self.entry5=tk.Entry(self.pagina3, width=30)
        self.entry5.grid(column=0, row=1)

        self.cuaderno1.grid(column=0, row=0)   


        self.ventana1.mainloop()
    def suma(self):
        valor01=int(self.dato1.get())
        valor02=int(self.dato2.get())
        suma=valor01+valor02
        self.label3.configure(text=suma)
    def resta(self):
        valor01=int(self.dato3.get())
        valor02=int(self.dato4.get())
        resta=valor01-valor02
        self.label6.configure(text=resta)


aplicacion1=Aplicacion()