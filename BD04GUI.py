import tkinter as tk
import mysql.connector
from tkinter import ttk, messagebox
from datetime import datetime


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Sistema de Gestión")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        # -------------------Configuración de Página 1-------------------
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Ingresa datos")

        # Labels
        self.label1 = ttk.Label(self.pagina1, text="Ingrese Descrip.: ")
        self.label1.grid(column=0, row=0)
        self.label2 = ttk.Label(self.pagina1, text="Ingrese Precio: ")
        self.label2.grid(column=1, row=0)
        self.label13 = ttk.Label(self.pagina1, text="Stock: ")
        self.label13.grid(column=2, row=0)

        # Entry
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.pagina1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)

        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.pagina1, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        self.dato7 = tk.StringVar()
        self.entry7 = tk.Entry(self.pagina1, width=10, textvariable=self.dato7)
        self.entry7.grid(column=2, row=1)

        # Botón para ingresar datos
        self.boton1 = ttk.Button(self.pagina1, text="Ingresar", command=self.ingresa)
        self.boton1.grid(column=0, row=2)

        # Label para mostrar resultados
        self.label3 = ttk.Label(self.pagina1, text="Resultado")
        self.label3.grid(column=1, row=2)

        # -------------------Configuración Página 2-------------------
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Listar")

        # Crear la Tabla de datos 
        self.tree = ttk.Treeview(self.pagina2, columns=("ID", "Descripcion", "Precio", "stock"), show="headings")

        # Definir encabezados
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("stock", text="stock")

        # Definir tamaño de columnas
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Descripcion", width=200, anchor="w")
        self.tree.column("Precio", width=100, anchor="center")
        self.tree.column("stock", width=50, anchor="center")

        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(self.pagina2, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # -------------------Configuración Página 3-------------------
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Buscar y Actualizar")

        # Buscar
        self.label7 = ttk.Label(self.pagina3, text="Producto: ")
        self.label7.grid(column=0, row=0)
        self.dato3 = tk.StringVar()
        self.entry3 = tk.Entry(self.pagina3, width=10, textvariable=self.dato3)
        self.entry3.grid(column=1, row=0)
        self.boton2 = ttk.Button(self.pagina3, text="Buscar", command=self.buscar)
        self.boton2.grid(column=2, row=0)

        # Tabla de consulta 
        self.tree02 = ttk.Treeview(self.pagina3, columns=("ID", "Descripcion", "Precio", "stock"), show="headings")

        # Definir encabezados
        self.tree02.heading("ID", text="ID")
        self.tree02.heading("Descripcion", text="Descripcion")
        self.tree02.heading("Precio", text="Precio")
        self.tree02.heading("stock", text="stock")

        # Definir tamaño de columnas
        self.tree02.column("ID", width=50, anchor="center")
        self.tree02.column("Descripcion", width=200, anchor="w")
        self.tree02.column("Precio", width=100, anchor="center")
        self.tree02.column("stock", width=50, anchor="center")

        self.tree02.grid(row=1, column=0, sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(self.pagina3, orient=tk.VERTICAL, command=self.tree02.yview)
        self.tree02.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        # Evento de selección en tree02
        self.tree02.bind("<<TreeviewSelect>>", self.seleccionar_producto)

        # Actualizar
        self.label9 = ttk.Label(self.pagina3, text="Código: ")
        self.label9.grid(column=0, row=2)
        self.dato4 = tk.StringVar()
        self.entry4 = tk.Entry(self.pagina3, width=10, textvariable=self.dato4)
        self.entry4.grid(column=1, row=2)

        self.label10 = ttk.Label(self.pagina3, text="Nueva Descripción: ")
        self.label10.grid(column=0, row=3)
        self.dato5 = tk.StringVar()
        self.entry5 = tk.Entry(self.pagina3, width=10, textvariable=self.dato5)
        self.entry5.grid(column=1, row=3)

        self.label11 = ttk.Label(self.pagina3, text="Nuevo Precio: ")
        self.label11.grid(column=0, row=4)
        self.dato6 = tk.StringVar()
        self.entry6 = tk.Entry(self.pagina3, width=10, textvariable=self.dato6)
        self.entry6.grid(column=1, row=4)

        # Cuadro de stock
        self.label15 = ttk.Label(self.pagina3, text="Nuevo Stock: ")
        self.label15.grid(column=0, row=5)
        self.dato15 = tk.StringVar()
        self.entry15 = tk.Entry(self.pagina3, width=10, textvariable=self.dato15)
        self.entry15.grid(column=1, row=5)

        self.boton3 = ttk.Button(self.pagina3, text="Actualizar", command=self.actualizar)
        self.boton3.grid(column=0, row=6)

        self.label12 = ttk.Label(self.pagina3, text="")
        self.label12.grid(column=1, row=6)

        # -------------------Configuración Página 4 (Ventas)-------------------
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Ventas")
        self.configurar_pagina4()

        self.cuaderno1.grid(column=0, row=0)

        # Llamada a listar para actualizar la lista al iniciar
        self.listar()
        self.listar_ventas()  # Llamar a listar_ventas para cargar las ventas al iniciar

        self.ventana1.mainloop()

    def ingresa(self):
        valor01 = self.dato1.get()
        try:
            valor02 = float(self.dato2.get())  # Convierte el precio a float
            valor03 = int(self.dato7.get())
        except ValueError:
            self.label3.configure(text="Error: Precio inválido")
            return

        # Conexión a la base de datos
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()

        # Inserción de datos
        sql = "INSERT INTO articulos(descripcion, precio, stock) VALUES (%s, %s, %s)"
        datos = (valor01, valor02, valor03)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()   

        self.label3.configure(text="Datos ingresados correctamente")

        # Llamar a listar() para actualizar la lista de artículos
        self.listar()

    def listar(self):
        self.tree.delete(*self.tree.get_children())
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()
        cursor1.execute("SELECT codigo, descripcion, precio, stock FROM articulos")
        for productos in cursor1:
            self.tree.insert('', tk.END, values=productos)

        conexion1.close()   

    def buscar(self):
        self.tree02.delete(*self.tree02.get_children())
        valor05 = str(self.dato3.get())
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()
        cursor1.execute(f"SELECT codigo, descripcion, precio, stock FROM articulos WHERE descripcion LIKE '{valor05}%'")

        for productos in cursor1:
            self.tree02.insert('', tk.END, values=productos)

        conexion1.close()   

    def seleccionar_producto(self, event):
        # Obtener el item seleccionado
        seleccionado = self.tree02.selection()
        if seleccionado:
            # Obtener los valores del item seleccionado
            valores = self.tree02.item(seleccionado, 'values')
            # Llenar los campos de actualización con los valores seleccionados
            self.dato4.set(valores[0])  # Código
            self.dato5.set(valores[1])  # Descripción
            self.dato6.set(valores[2])  # Precio
            self.dato15.set(valores[3])  # Stock

    def actualizar(self):
        codigo = self.dato4.get()
        nueva_descripcion = self.dato5.get()
        nuevo_precio = self.dato6.get()
        nuevo_stock = self.dato15.get()

        if not codigo or not nueva_descripcion or not nuevo_precio or not nuevo_stock:
            self.label12.configure(text="Error: Todos los campos son requeridos")
            return

        try:
            nuevo_precio = float(nuevo_precio)  # Convierte el precio a float
            nuevo_stock = int(nuevo_stock)  # Convierte el stock a entero
        except ValueError:
            self.label12.configure(text="Error: Precio o stock inválido")
            return

        # Conexión a la base de datos
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()

        # Actualización de datos
        sql = "UPDATE articulos SET descripcion = %s, precio = %s, stock = %s WHERE codigo = %s"
        datos = (nueva_descripcion, nuevo_precio, nuevo_stock, codigo)
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()   

        self.label12.configure(text="Producto actualizado correctamente")

        # Llamar a listar() para actualizar la lista de artículos
        self.listar()

    def configurar_pagina4(self):
        # Campos para ventas
        ttk.Label(self.pagina4, text="Código Producto:").grid(column=0, row=0)
        self.codigo_venta = tk.StringVar()
        ttk.Entry(self.pagina4, width=10, textvariable=self.codigo_venta).grid(column=1, row=0)

        ttk.Label(self.pagina4, text="Cantidad:").grid(column=0, row=1)
        self.cantidad_venta = tk.StringVar()
        ttk.Entry(self.pagina4, width=10, textvariable=self.cantidad_venta).grid(column=1, row=1)

        ttk.Button(self.pagina4, text="Registrar Venta", command=self.registrar_venta).grid(column=0, row=2)

        # Tabla de ventas
        self.tree_ventas = ttk.Treeview(self.pagina4, columns=("ID", "Producto", "Cantidad", "Total", "Fecha"), show="headings")
        self.tree_ventas.heading("ID", text="ID")
        self.tree_ventas.heading("Producto", text="Producto")
        self.tree_ventas.heading("Cantidad", text="Cantidad")
        self.tree_ventas.heading("Total", text="Total")
        self.tree_ventas.heading("Fecha", text="Fecha")
        
        self.tree_ventas.column("ID", width=50, anchor="center")
        self.tree_ventas.column("Producto", width=150, anchor="w")
        self.tree_ventas.column("Cantidad", width=80, anchor="center")
        self.tree_ventas.column("Total", width=80, anchor="center")
        self.tree_ventas.column("Fecha", width=120, anchor="center")
        self.tree_ventas.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
        

    def listar_ventas(self):
        # Limpiar la tabla de ventas
        self.tree_ventas.delete(*self.tree_ventas.get_children())

        # Conexión a la base de datos
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()

        # Obtener las ventas
        cursor1.execute("SELECT id, descripcion, cantidad, total, fecha_venta FROM ventas")
        for venta in cursor1:
            self.tree_ventas.insert('', tk.END, values=venta)

        conexion1.close()

    def registrar_venta(self):
        codigo = self.codigo_venta.get()
        cantidad = self.cantidad_venta.get()

        if not codigo or not cantidad:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor que 0")
                return
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")
            return

        # Conexión a la base de datos
        conexion1 = mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="", 
            database="bd1"
        )
        cursor1 = conexion1.cursor()

        # Verificar stock y obtener precio
        cursor1.execute(f"SELECT stock, precio, descripcion FROM articulos WHERE codigo = {codigo}")
        producto = cursor1.fetchone()

        if not producto:
            messagebox.showerror("Error", "Producto no encontrado")
            conexion1.close()
            return

        stock_actual, precio, descripcion = producto

        if stock_actual < cantidad:
            messagebox.showerror("Error", "Stock insuficiente")
            conexion1.close()
            return

        # Calcular total
        total = precio * cantidad

        # Registrar la venta
        cursor1.execute(
            "INSERT INTO ventas (codigo_producto, descripcion, cantidad, precio_unitario, total) VALUES (%s, %s, %s, %s, %s)",
            (codigo, descripcion, cantidad, precio, total)
        )

        # Disminuir el stock
        nuevo_stock = stock_actual - cantidad
        cursor1.execute(f"UPDATE articulos SET stock = {nuevo_stock} WHERE codigo = {codigo}")

        conexion1.commit()
        conexion1.close()

        messagebox.showinfo("Éxito", "Venta registrada correctamente")
        self.codigo_venta.set("")
        self.cantidad_venta.set("")
        self.listar_ventas()  # Actualizar la tabla de ventas después de registrar una nueva venta


aplicacion1 = Aplicacion()