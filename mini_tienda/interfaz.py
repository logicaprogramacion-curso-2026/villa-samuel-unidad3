# interfaz.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import datos

from datos import agregar_producto

from ventas import (
    registrar_venta,
    generar_ventas_prueba
)

from archivos import (
    guardar_venta_csv,
    registrar_log,
    cargar_ventas_csv
)

from analisis import (
    cargar_dataframe,
    calcular_metricas,
    generar_grafico,
    exportar_grafico
)

class MiniTiendaApp:

    def __init__(self, ventana):

        self.ventana = ventana

        self.ventana.title(
            "MiniTienda - Sistema de Ventas"
        )

        self.ventana.geometry(
            "1000x700"
        )

        self.ventana.resizable(
            False,
            False
        )

        self.crear_interfaz()

    # --------------------------------------------------
    # INTERFAZ PRINCIPAL
    # --------------------------------------------------

    def crear_interfaz(self):

        titulo = tk.Label(
            self.ventana,
            text="MINITIENDA",
            font=("Arial", 26, "bold")
        )

        titulo.pack(
            pady=15
        )

        subtitulo = tk.Label(
            self.ventana,
            text="Registro y análisis de ventas",
            font=("Arial", 12)
        )

        subtitulo.pack()

        # -------------------------------
        # MENÚ
        # -------------------------------

        menu_frame = tk.LabelFrame(
            self.ventana,
            text="Menú principal",
            padx=10,
            pady=10
        )

        menu_frame.pack(
            padx=20,
            pady=15,
            fill="x"
        )

        botones = [
            ("1. Registrar venta", self.mostrar_registro),
            ("2. Ver catálogo", self.actualizar_catalogo),
            ("3. Ver ventas", self.mostrar_ventas),
            ("4. Ver estadísticas", self.mostrar_metricas),
            ("5. Ver gráfico", self.mostrar_grafico),
            ("6. Exportar gráfico", self.exportar_png),
            ("7. Agregar producto", self.mostrar_agregar_producto),
            ("8. Generar 10 ventas", self.generar_ventas),
            ("9. Salir", self.ventana.destroy)
        ]

        for indice, (
            texto,
            comando
        ) in enumerate(botones):

            fila = indice // 4
            columna = indice % 4

            tk.Button(
                menu_frame,
                text=texto,
                width=20,
                command=comando
            ).grid(
                row=fila,
                column=columna,
                padx=5,
                pady=5
            )

        # -------------------------------
        # ÁREA DE CONTENIDO
        # -------------------------------

        self.contenido = tk.Frame(
            self.ventana
        )

        self.contenido.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        self.actualizar_catalogo()

    # --------------------------------------------------
    # LIMPIAR CONTENIDO
    # --------------------------------------------------

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    # --------------------------------------------------
    # OPCIÓN 1
    # --------------------------------------------------

    def mostrar_registro(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Registrar venta",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        frame = tk.Frame(
            self.contenido
        )

        frame.pack(
            pady=20
        )

        tk.Label(
            frame,
            text="Producto:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.producto_combo = ttk.Combobox(
            frame,
            state="readonly",
            width=30
        )

        productos = []

        # FOR
        for producto_id, nombre in datos.CATALOGO:

            productos.append(
                f"{producto_id} - {nombre}"
            )

        self.producto_combo["values"] = productos

        self.producto_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            frame,
            text="Unidades:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.unidades_entry = tk.Entry(
            frame,
            width=20
        )

        self.unidades_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Button(
            frame,
            text="Registrar",
            width=20,
            command=self.registrar
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

    # --------------------------------------------------
    # REGISTRAR VENTA
    # --------------------------------------------------

    def registrar(self):

        try:

            seleccion = self.producto_combo.get()

            if not seleccion:

                raise ValueError(
                    "Debe seleccionar un producto."
                )

            unidades = int(
                self.unidades_entry.get()
            )

            producto_id = (
                seleccion.split(" - ")[0]
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

            return

        else:

            venta, mensaje = registrar_venta(
                producto_id,
                unidades
            )

        finally:

            self.unidades_entry.delete(
                0,
                tk.END
            )

        if venta is None:

            registrar_log(
                f"Intento de venta fallido | "
                f"Producto: {producto_id} | "
                f"Unidades: {unidades} | "
                f"Motivo: {mensaje}"
            )

            messagebox.showerror(
                "Venta no registrada",
                mensaje
            )

            return

        guardar_venta_csv(
            venta
        )

        messagebox.showinfo(
            "Venta registrada",
            (
                f"Producto: {venta['producto']}\n"
                f"Unidades: {venta['unidades']}\n"
                f"Descuento: ${venta['descuento']:.2f}\n"
                f"Total: ${venta['total']:.2f}"
            )
        )

    # --------------------------------------------------
    # OPCIÓN 2
    # --------------------------------------------------

    def actualizar_catalogo(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Catálogo de productos",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        columnas = (
            "id",
            "producto",
            "precio",
            "stock"
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings",
            height=15
        )

        tabla.heading(
            "id",
            text="ID"
        )

        tabla.heading(
            "producto",
            text="Producto"
        )

        tabla.heading(
            "precio",
            text="Precio"
        )

        tabla.heading(
            "stock",
            text="Stock"
        )

        tabla.column(
            "id",
            width=100
        )

        tabla.column(
            "producto",
            width=250
        )

        tabla.column(
            "precio",
            width=150
        )

        tabla.column(
            "stock",
            width=150
        )

        tabla.pack(
            fill="both",
            expand=True
        )

        # WHILE
        indice = 0

        while indice < len(datos.CATALOGO):

            producto_id, nombre = (
                datos.CATALOGO[indice]
            )

            tabla.insert(
                "",
                "end",
                values=(
                    producto_id,
                    nombre,
                    f"${datos.PRECIOS[producto_id]:.2f}",
                    datos.STOCK[producto_id]
                )
            )

            indice += 1

    # --------------------------------------------------
    # OPCIÓN 3
    # --------------------------------------------------

    def mostrar_ventas(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Ventas registradas",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        df = cargar_dataframe()

        if df.empty:

            tk.Label(
                self.contenido,
                text="No existen ventas registradas."
            ).pack(
                pady=30
            )

            return

        columnas = (
            "producto",
            "unidades",
            "precio",
            "descuento",
            "total"
        )

        tabla = ttk.Treeview(
            self.contenido,
            columns=columnas,
            show="headings",
            height=15
        )

        tabla.heading(
            "producto",
            text="Producto"
        )

        tabla.heading(
            "unidades",
            text="Unidades"
        )

        tabla.heading(
            "precio",
            text="Precio"
        )

        tabla.heading(
            "descuento",
            text="Descuento"
        )

        tabla.heading(
            "total",
            text="Total"
        )

        # FOR
        for _, fila in df.iterrows():

            tabla.insert(
                "",
                "end",
                values=(
                    fila["producto"],
                    fila["unidades"],
                    f"${float(fila['precio_unitario']):.2f}",
                    f"${float(fila['descuento']):.2f}",
                    f"${float(fila['total']):.2f}"
                )
            )

        tabla.pack(
            fill="both",
            expand=True
        )

    # --------------------------------------------------
    # OPCIÓN 4
    # --------------------------------------------------

    def mostrar_metricas(self):

        metricas = calcular_metricas()

        if metricas["suma"] == 0:

            messagebox.showwarning(
                "Estadísticas",
                "No existen ventas para analizar."
            )

            return

        mensaje = (
            f"INGRESOS TOTALES\n"
            f"${metricas['suma']:.2f}\n\n"
            f"PROMEDIO POR VENTA\n"
            f"${metricas['media']:.2f}\n\n"
            f"DESVIACIÓN ESTÁNDAR\n"
            f"${metricas['desviacion']:.2f}"
        )

        messagebox.showinfo(
            "Estadísticas",
            mensaje
        )

    # --------------------------------------------------
    # OPCIÓN 5
    # --------------------------------------------------

    def mostrar_grafico(self):

        resultado = generar_grafico()

        if not resultado:

            messagebox.showwarning(
                "Gráfico",
                "No existen ventas para graficar."
            )

    # --------------------------------------------------
    # OPCIÓN 6
    # --------------------------------------------------

    def exportar_png(self):

        resultado = exportar_grafico()

        if resultado:

            messagebox.showinfo(
                "Gráfico exportado",
                "Se creó el archivo ingresos.png"
            )

        else:

            messagebox.showwarning(
                "Gráfico",
                "No existen ventas para exportar."
            )

    # --------------------------------------------------
    # OPCIÓN 7
    # --------------------------------------------------

    def mostrar_agregar_producto(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Agregar nuevo producto",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        frame = tk.Frame(
            self.contenido
        )

        frame.pack(
            pady=20
        )

        tk.Label(
            frame,
            text="ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8
        )

        id_entry = tk.Entry(
            frame
        )

        id_entry.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            frame,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8
        )

        nombre_entry = tk.Entry(
            frame
        )

        nombre_entry.grid(
            row=1,
            column=1,
            padx=10
        )

        tk.Label(
            frame,
            text="Precio:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8
        )

        precio_entry = tk.Entry(
            frame
        )

        precio_entry.grid(
            row=2,
            column=1,
            padx=10
        )

        tk.Label(
            frame,
            text="Stock:"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=8
        )

        stock_entry = tk.Entry(
            frame
        )

        stock_entry.grid(
            row=3,
            column=1,
            padx=10
        )

        def guardar_producto():

            try:

                producto_id = (
                    id_entry.get()
                    .strip()
                    .upper()
                )

                nombre = (
                    nombre_entry.get()
                    .strip()
                )

                precio = float(
                    precio_entry.get()
                )

                stock = int(
                    stock_entry.get()
                )

                if not producto_id:
                    raise ValueError(
                        "El ID no puede estar vacío."
                    )

                if not nombre:
                    raise ValueError(
                        "El nombre no puede estar vacío."
                    )

                if precio <= 0:
                    raise ValueError(
                        "El precio debe ser mayor que cero."
                    )

                if stock < 0:
                    raise ValueError(
                        "El stock no puede ser negativo."
                    )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

                return

            # TRY / EXCEPT / ELSE
            else:

                agregado = agregar_producto(
                    producto_id,
                    nombre,
                    precio,
                    stock
                )

                if not agregado:

                    messagebox.showerror(
                        "Error",
                        "Ese ID ya existe."
                    )

                    return

                messagebox.showinfo(
                    "Producto agregado",
                    "Producto agregado correctamente."
                )

                self.actualizar_catalogo()

            # FINALLY
            finally:

                id_entry.focus()

        tk.Button(
            frame,
            text="Agregar producto",
            width=20,
            command=guardar_producto
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            pady=15
        )
        
    def generar_ventas(self):
    
        try:

            ventas = generar_ventas_prueba(10)

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudieron generar las ventas:\n{error}"
            )

            return

        else:

            for venta in ventas:

                guardar_venta_csv(
                    venta
                )

        finally:

            self.actualizar_catalogo()

        messagebox.showinfo(
            "Ventas generadas",
            f"Se generaron {len(ventas)} ventas de prueba."
        )