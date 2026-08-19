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
    registrar_log
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

        # Lista utilizada como carrito
        self.carrito = []

        self.crear_interfaz()

    # ==================================================
    # INTERFAZ PRINCIPAL
    # ==================================================

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

        # ----------------------------------------------
        # MENÚ
        # ----------------------------------------------

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
            (
                "1. Registrar compra",
                self.mostrar_registro
            ),
            (
                "2. Ver catálogo",
                self.actualizar_catalogo
            ),
            (
                "3. Ver ventas",
                self.mostrar_ventas
            ),
            (
                "4. Ver estadísticas",
                self.mostrar_metricas
            ),
            (
                "5. Ver gráfico",
                self.mostrar_grafico
            ),
            (
                "6. Exportar gráfico",
                self.exportar_png
            ),
            (
                "7. Agregar producto",
                self.mostrar_agregar_producto
            ),
            (
                "8. Generar 10 ventas",
                self.generar_ventas
            ),
            (
                "9. Salir",
                self.ventana.destroy
            )
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

        # ----------------------------------------------
        # CONTENIDO
        # ----------------------------------------------

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

    # ==================================================
    # LIMPIAR CONTENIDO
    # ==================================================

    def limpiar_contenido(self):

        for widget in (
            self.contenido.winfo_children()
        ):

            widget.destroy()

    # ==================================================
    # OPCIÓN 1: REGISTRAR COMPRA
    # ==================================================

    def mostrar_registro(self):

        self.limpiar_contenido()

        self.carrito = []

        titulo = tk.Label(
            self.contenido,
            text="Registrar compra",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        # ----------------------------------------------
        # ENTRADA
        # ----------------------------------------------

        frame_entrada = tk.LabelFrame(
            self.contenido,
            text="Agregar producto a la compra",
            padx=15,
            pady=15
        )

        frame_entrada.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        tk.Label(
            frame_entrada,
            text="Producto:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.producto_combo = ttk.Combobox(
            frame_entrada,
            state="readonly",
            width=30
        )

        productos = []

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
            frame_entrada,
            text="Unidades:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.unidades_entry = tk.Entry(
            frame_entrada,
            width=20
        )

        self.unidades_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Button(
            frame_entrada,
            text="Agregar al carrito",
            width=20,
            command=self.agregar_al_carrito
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        # ----------------------------------------------
        # CARRITO
        # ----------------------------------------------

        frame_carrito = tk.LabelFrame(
            self.contenido,
            text="Productos de la compra",
            padx=10,
            pady=10
        )

        frame_carrito.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        columnas = (
            "id",
            "producto",
            "cantidad",
            "precio",
            "subtotal"
        )

        self.tabla_carrito = ttk.Treeview(
            frame_carrito,
            columns=columnas,
            show="headings",
            height=8
        )

        self.tabla_carrito.heading(
            "id",
            text="ID"
        )

        self.tabla_carrito.heading(
            "producto",
            text="Producto"
        )

        self.tabla_carrito.heading(
            "cantidad",
            text="Cantidad"
        )

        self.tabla_carrito.heading(
            "precio",
            text="Precio"
        )

        self.tabla_carrito.heading(
            "subtotal",
            text="Subtotal"
        )

        self.tabla_carrito.column(
            "id",
            width=80
        )

        self.tabla_carrito.column(
            "producto",
            width=180
        )

        self.tabla_carrito.column(
            "cantidad",
            width=100
        )

        self.tabla_carrito.column(
            "precio",
            width=100
        )

        self.tabla_carrito.column(
            "subtotal",
            width=120
        )

        self.tabla_carrito.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------
        # BOTONES
        # ----------------------------------------------

        botones = tk.Frame(
            self.contenido
        )

        botones.pack(
            pady=10
        )

        tk.Button(
            botones,
            text="Quitar seleccionado",
            width=20,
            command=self.quitar_del_carrito
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            botones,
            text="Vaciar carrito",
            width=20,
            command=self.vaciar_carrito
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            botones,
            text="Registrar compra",
            width=20,
            command=self.registrar_compra
        ).pack(
            side="left",
            padx=5
        )

        self.label_total = tk.Label(
            self.contenido,
            text="Total: $0.00",
            font=("Arial", 14, "bold")
        )

        self.label_total.pack(
            pady=5
        )

    # ==================================================
    # AGREGAR AL CARRITO
    # ==================================================

    def agregar_al_carrito(self):

        try:

            seleccion = (
                self.producto_combo.get()
            )

            if not seleccion:

                raise ValueError(
                    "Debe seleccionar un producto."
                )

            unidades = int(
                self.unidades_entry.get()
            )

            if unidades <= 0:

                raise ValueError(
                    "Las unidades deben ser mayores que cero."
                )

            producto_id = (
                seleccion.split(" - ")[0]
            )

            nombre = datos.obtener_nombre(
                producto_id
            )

            if not datos.producto_existe(
                producto_id
            ):

                raise ValueError(
                    "El producto no existe."
                )

            precio = datos.PRECIOS[
                producto_id
            ]

            # Buscar si el producto
            # ya está en el carrito.

            for producto in self.carrito:

                if (
                    producto["producto_id"]
                    == producto_id
                ):

                    nueva_cantidad = (
                        producto["unidades"]
                        + unidades
                    )

                    if nueva_cantidad > (
                        datos.STOCK[producto_id]
                    ):

                        raise ValueError(
                            "La cantidad supera "
                            "el stock disponible."
                        )

                    producto["unidades"] = (
                        nueva_cantidad
                    )

                    producto["subtotal"] = (
                        nueva_cantidad * precio
                    )

                    self.actualizar_carrito()

                    self.unidades_entry.delete(
                        0,
                        tk.END
                    )

                    return

            if unidades > datos.STOCK[
                producto_id
            ]:

                raise ValueError(
                    "No existe suficiente stock."
                )

            producto_carrito = {
                "producto_id": producto_id,
                "producto": nombre,
                "unidades": unidades,
                "precio": precio,
                "subtotal": precio * unidades
            }

            self.carrito.append(
                producto_carrito
            )

            self.actualizar_carrito()

            self.unidades_entry.delete(
                0,
                tk.END
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==================================================
    # ACTUALIZAR CARRITO
    # ==================================================

    def actualizar_carrito(self):

        for item in (
            self.tabla_carrito.get_children()
        ):

            self.tabla_carrito.delete(
                item
            )

        total = 0

        for producto in self.carrito:

            self.tabla_carrito.insert(
                "",
                "end",
                values=(
                    producto["producto_id"],
                    producto["producto"],
                    producto["unidades"],
                    f"${producto['precio']:.2f}",
                    f"${producto['subtotal']:.2f}"
                )
            )

            total += producto["subtotal"]

        self.label_total.config(
            text=f"Total: ${total:.2f}"
        )

    # ==================================================
    # QUITAR DEL CARRITO
    # ==================================================

    def quitar_del_carrito(self):

        seleccionado = (
            self.tabla_carrito.selection()
        )

        if not seleccionado:

            messagebox.showwarning(
                "Carrito",
                "Seleccione un producto."
            )

            return

        item = self.tabla_carrito.item(
            seleccionado[0]
        )

        producto_id = item["values"][0]

        for producto in self.carrito:

            if (
                producto["producto_id"]
                == producto_id
            ):

                self.carrito.remove(
                    producto
                )

                break

        self.actualizar_carrito()

    # ==================================================
    # VACIAR CARRITO
    # ==================================================

    def vaciar_carrito(self):

        if not self.carrito:

            messagebox.showwarning(
                "Carrito",
                "El carrito ya está vacío."
            )

            return

        self.carrito.clear()

        self.actualizar_carrito()

    # ==================================================
    # REGISTRAR COMPRA COMPLETA
    # ==================================================

    def registrar_compra(self):

        if not self.carrito:

            messagebox.showwarning(
                "Compra",
                "Debe agregar al menos un producto."
            )

            return

        ventas_registradas = []

        total_compra = 0

        try:

            for producto in self.carrito:

                venta, mensaje = registrar_venta(
                    producto["producto_id"],
                    producto["unidades"]
                )

                if venta is None:

                    registrar_log(
                        f"Intento de compra fallido | "
                        f"Producto: "
                        f"{producto['producto_id']} | "
                        f"Unidades: "
                        f"{producto['unidades']} | "
                        f"Motivo: {mensaje}"
                    )

                    raise ValueError(
                        mensaje
                    )

                ventas_registradas.append(
                    venta
                )

                total_compra += (
                    venta["total"]
                )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

            return

        else:

            for venta in ventas_registradas:

                guardar_venta_csv(
                    venta
                )

            messagebox.showinfo(
                "Compra registrada",
                (
                    "Compra registrada correctamente.\n\n"
                    f"Productos: "
                    f"{len(ventas_registradas)}\n"
                    f"Total: ${total_compra:.2f}"
                )
            )

        finally:

            self.carrito.clear()

            self.actualizar_carrito()

            self.actualizar_catalogo()

    # ==================================================
    # OPCIÓN 2: CATÁLOGO
    # ==================================================

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

        while indice < len(
            datos.CATALOGO
        ):

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

    # ==================================================
    # OPCIÓN 3: VENTAS
    # ==================================================

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
            "fecha",
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
            "fecha",
            text="Fecha"
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

        for _, fila in df.iterrows():

            tabla.insert(
                "",
                "end",
                values=(
                    fila["fecha"],
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

    # ==================================================
    # OPCIÓN 4: ESTADÍSTICAS
    # ==================================================

    def mostrar_metricas(self):

        metricas = calcular_metricas()

        if metricas["suma"] == 0:

            messagebox.showwarning(
                "Estadísticas",
                "No existen ventas para analizar."
            )

            return

        mensaje = (
            "INGRESOS TOTALES\n"
            f"${metricas['suma']:.2f}\n\n"
            "PROMEDIO POR VENTA\n"
            f"${metricas['media']:.2f}\n\n"
            "DESVIACIÓN ESTÁNDAR\n"
            f"${metricas['desviacion']:.2f}"
        )

        messagebox.showinfo(
            "Estadísticas",
            mensaje
        )

    # ==================================================
    # OPCIÓN 5: GRÁFICO
    # ==================================================

    def mostrar_grafico(self):

        resultado = generar_grafico()

        if not resultado:

            messagebox.showwarning(
                "Gráfico",
                "No existen ventas para graficar."
            )

    # ==================================================
    # OPCIÓN 6: EXPORTAR PNG
    # ==================================================

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

    # ==================================================
    # OPCIÓN 7: AGREGAR PRODUCTO
    # ==================================================

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

        id_entry = tk.Entry(frame)

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

        nombre_entry = tk.Entry(frame)

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

        precio_entry = tk.Entry(frame)

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

        stock_entry = tk.Entry(frame)

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

    # ==================================================
    # OPCIÓN 8: GENERAR 10 VENTAS
    # ==================================================

    def generar_ventas(self):

        try:

            ventas = generar_ventas_prueba(
                10
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                (
                    "No se pudieron generar "
                    f"las ventas:\n{error}"
                )
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
            (
                f"Se generaron "
                f"{len(ventas)} ventas de prueba."
            )
        )