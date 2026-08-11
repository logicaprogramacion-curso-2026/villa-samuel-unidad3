import threading
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

from evaluacion import EvaluacionDocente
from reporte import guardar_reporte, generar_texto_reporte


class AppEvaluacionDocente(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Evaluación Docente con IA")
        self.geometry("850x750")
        self.minsize(700, 600)

        self.actividades_lista = []
        self.resultados_ultimo_analisis = None

        self.crear_interfaz()

    def crear_interfaz(self):
        # --- Datos del Docente ---
        frame_datos = ttk.LabelFrame(self, text=" Datos del Docente ")
        frame_datos.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame_datos, text="Nombre del Docente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.txt_nombre = ttk.Entry(frame_datos, width=40)
        self.txt_nombre.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame_datos, text="Materia / Asignatura:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.txt_materia = ttk.Entry(frame_datos, width=40)
        self.txt_materia.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # --- Actividades ---
        frame_actividades = ttk.LabelFrame(self, text=" Actividades a Evaluar ")
        frame_actividades.pack(fill="both", expand=True, padx=10, pady=5)

        ttk.Label(frame_actividades, text="Escriba la descripción de la actividad:").pack(anchor="w", padx=5, pady=2)

        self.txt_actividad_input = scrolledtext.ScrolledText(frame_actividades, height=3, wrap="word")
        self.txt_actividad_input.pack(fill="x", padx=5, pady=2)

        btn_agregar = ttk.Button(frame_actividades, text="➕ Agregar Actividad", command=self.agregar_actividad)
        btn_agregar.pack(anchor="e", padx=5, pady=2)

        ttk.Label(frame_actividades, text="Actividades registradas:").pack(anchor="w", padx=5, pady=2)

        frame_listbox = ttk.Frame(frame_actividades)
        frame_listbox.pack(fill="both", expand=True, padx=5, pady=2)

        self.listbox_actividades = tk.Listbox(frame_listbox, height=4)
        scrollbar_listbox = ttk.Scrollbar(frame_listbox, orient="vertical", command=self.listbox_actividades.yview)
        self.listbox_actividades.configure(yscrollcommand=scrollbar_listbox.set)

        self.listbox_actividades.pack(side="left", fill="both", expand=True)
        scrollbar_listbox.pack(side="right", fill="y")

        btn_eliminar = ttk.Button(frame_actividades, text="🗑️ Eliminar Seleccionada", command=self.eliminar_actividad)
        btn_eliminar.pack(anchor="e", padx=5, pady=2)

        # --- Acciones y Estado ---
        frame_acciones = ttk.Frame(self)
        frame_acciones.pack(fill="x", padx=10, pady=5)

        self.btn_analizar = ttk.Button(frame_acciones, text="⚡ Analizar con IA", command=self.iniciar_analisis)
        self.btn_analizar.pack(side="left", padx=5)

        self.lbl_estado = ttk.Label(frame_acciones, text="Listo.", font=("Arial", 9, "italic"))
        self.lbl_estado.pack(side="left", padx=10)

        # --- Reporte de Resultados ---
        frame_resultados = ttk.LabelFrame(self, text=" Informe de Evaluación ")
        frame_resultados.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_reporte = scrolledtext.ScrolledText(frame_resultados, wrap="word")
        self.txt_reporte.pack(fill="both", expand=True, padx=5, pady=5)

        self.btn_guardar = ttk.Button(
            frame_resultados, 
            text="💾 Guardar Reporte (JSON/TXT)", 
            command=self.guardar_resultado,
            state="disabled"
        )
        self.btn_guardar.pack(anchor="e", padx=5, pady=5)

    def agregar_actividad(self):
        texto = self.txt_actividad_input.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Atención", "Ingrese un texto descriptivo para la actividad.")
            return

        self.actividades_lista.append(texto)
        self.listbox_actividades.insert(tk.END, f"Actividad {len(self.actividades_lista)}: {texto[:70]}...")
        self.txt_actividad_input.delete("1.0", tk.END)

    def eliminar_actividad(self):
        seleccion = self.listbox_actividades.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione una actividad de la lista.")
            return

        idx = seleccion[0]
        self.actividades_lista.pop(idx)

        self.listbox_actividades.delete(0, tk.END)
        for i, act in enumerate(self.actividades_lista, start=1):
            self.listbox_actividades.insert(tk.END, f"Actividad {i}: {act[:70]}...")

    def iniciar_analisis(self):
        nombre = self.txt_nombre.get().strip()
        materia = self.txt_materia.get().strip()

        if not nombre or not materia:
            messagebox.showerror("Campos incompletos", "Por favor ingrese el nombre del docente y la materia.")
            return

        if not self.actividades_lista:
            messagebox.showerror("Sin actividades", "Debe agregar al menos una actividad antes de continuar.")
            return

        self.btn_analizar.config(state="disabled")
        self.lbl_estado.config(text="⏳ Conectando con Ollama y procesando el informe... Por favor espere.")

        # Uso de threading para evitar el congelamiento de la ventana durante la petición a Ollama
        threading.Thread(target=self.procesar_analisis, args=(nombre, materia), daemon=True).start()

    def procesar_analisis(self, nombre, materia):
        sistema = EvaluacionDocente(nombre, materia, self.actividades_lista)
        resultados = sistema.analizar()

        self.after(0, self.finalizar_analisis, nombre, materia, resultados)

    def finalizar_analisis(self, nombre, materia, resultados):
        self.btn_analizar.config(state="normal")

        if resultados is None:
            self.lbl_estado.config(text="❌ Error en el proceso.")
            messagebox.showerror(
                "Error de Evaluación", 
                "No se pudo completar el análisis.\n\n"
                "Asegúrese de que Ollama esté ejecutándose en http://localhost:11434 "
                "y que el modelo responda correctamente."
            )
            return

        self.resultados_ultimo_analisis = (nombre, materia, self.actividades_lista.copy(), resultados)
        self.lbl_estado.config(text="✅ Análisis completado con éxito.")
        self.btn_guardar.config(state="normal")

        reporte_texto = generar_texto_reporte(nombre, materia, self.actividades_lista, resultados)
        self.txt_reporte.delete("1.0", tk.END)
        self.txt_reporte.insert(tk.END, reporte_texto)

    def guardar_resultado(self):
        if not self.resultados_ultimo_analisis:
            return

        nombre, materia, actividades, resultados = self.resultados_ultimo_analisis
        guardar_reporte(nombre, materia, actividades, resultados)
        messagebox.showinfo("Guardado", "Se han generado y guardado los archivos JSON y TXT en la carpeta 'resultados'.")


if __name__ == "__main__":
    app = AppEvaluacionDocente()
    app.mainloop()