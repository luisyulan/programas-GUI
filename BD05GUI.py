import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class CRUDApp:
    def __init__(self):
        # Configuración de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("CRUD con MySQL y Treeview")
        self.ventana.geometry("600x400")

        # Conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bd1"
        )
        self.cursor = self.conexion.cursor()

        # Crear la tabla si no existe
        self.crear_tabla()

        # Interfaz gráfica
        self.crear_interfaz()

        # Cargar datos iniciales en la tabla
        self.actualizar_tabla()

        self.ventana.mainloop()

    def crear_tabla(self):
        """Crea la tabla en la base de datos si no existe."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS articulos (
                codigo INT AUTO_INCREMENT PRIMARY KEY,
                descripcion VARCHAR(100) NOT NULL,
                precio FLOAT NOT NULL
            )
        """)
        self.conexion.commit()

    def crear_interfaz(self):
        """Crea los elementos de la interfaz gráfica."""
        # Frame para los campos de entrada
        frame_entrada = ttk.Frame(self.ventana)
        frame_entrada.pack(pady=10)

        # Campos de entrada
        ttk.Label(frame_entrada, text="Descripción:").grid(row=0, column=0, padx=5, pady=5)
        self.descripcion = tk.StringVar()
        ttk.Entry(frame_entrada, textvariable=self.descripcion, width=30).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_entrada, text="Precio:").grid(row=1, column=0, padx=5, pady=5)
        self.precio = tk.StringVar()
        ttk.Entry(frame_entrada, textvariable=self.precio, width=30).grid(row=1, column=1, padx=5, pady=5)

        # Botones de CRUD
        ttk.Button(frame_entrada, text="Agregar", command=self.agregar).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(frame_entrada, text="Actualizar", command=self.actualizar).grid(row=2, column=1, padx=5, pady=5)
        ttk.Button(frame_entrada, text="Eliminar", command=self.eliminar).grid(row=2, column=2, padx=5, pady=5)

        # Treeview para mostrar los datos
        self.tabla = ttk.Treeview(self.ventana, columns=("Código", "Descripción", "Precio"), show="headings")
        self.tabla.heading("Código", text="Código")
        self.tabla.heading("Descripción", text="Descripción")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Evento para seleccionar un registro de la tabla
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_registro)

    def actualizar_tabla(self):
        """Actualiza los datos en la tabla Treeview."""
        # Limpiar la tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Obtener datos de la base de datos
        self.cursor.execute("SELECT codigo, descripcion, precio FROM articulos")
        filas = self.cursor.fetchall()

        # Insertar datos en la tabla
        for fila in filas:
            self.tabla.insert("", tk.END, values=fila)

    def agregar(self):
        """Agrega un nuevo artículo a la base de datos."""
        descripcion = self.descripcion.get()
        precio = self.precio.get()

        if not descripcion or not precio:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showwarning("Error", "El precio debe ser un número válido")
            return

        # Insertar en la base de datos
        self.cursor.execute("INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)", (descripcion, precio))
        self.conexion.commit()

        # Actualizar la tabla y limpiar campos
        self.actualizar_tabla()
        self.descripcion.set("")
        self.precio.set("")

    def seleccionar_registro(self, event):
        """Selecciona un registro de la tabla para actualizar o eliminar."""
        seleccionado = self.tabla.selection()
        if seleccionado:
            valores = self.tabla.item(seleccionado, "values")
            self.descripcion.set(valores[1])
            self.precio.set(valores[2])

    def actualizar(self):
        """Actualiza un artículo en la base de datos."""
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro para actualizar")
            return

        codigo = self.tabla.item(seleccionado, "values")[0]
        descripcion = self.descripcion.get()
        precio = self.precio.get()

        if not descripcion or not precio:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        try:
            precio = float(precio)
        except ValueError:
            messagebox.showwarning("Error", "El precio debe ser un número válido")
            return

        # Actualizar en la base de datos
        self.cursor.execute("UPDATE articulos SET descripcion = %s, precio = %s WHERE codigo = %s", (descripcion, precio, codigo))
        self.conexion.commit()

        # Actualizar la tabla y limpiar campos
        self.actualizar_tabla()
        self.descripcion.set("")
        self.precio.set("")

    def eliminar(self):
        """Elimina un artículo de la base de datos."""
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro para eliminar")
            return

        codigo = self.tabla.item(seleccionado, "values")[0]

        # Eliminar de la base de datos
        self.cursor.execute("DELETE FROM articulos WHERE codigo = %s", (codigo,))
        self.conexion.commit()

        # Actualizar la tabla
        self.actualizar_tabla()

# Iniciar la aplicación
app = CRUDApp()