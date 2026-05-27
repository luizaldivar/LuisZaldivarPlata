# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:30:01 2026

@author: zaldi
"""

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Variable global para almacenar el modelo una vez entrenado
modelo_clima = None

columnas_entrada = [
    'Temperature (C)', 
    'Apparent Temperature (C)', 
    'Humidity', 
    'Wind Speed (km/h)', 
    'Wind Bearing (degrees)', 
    'Visibility (km)', 
    'Pressure (millibars)'
]

def entrenar_modelo():
    """Lee el CSV y entrena el modelo en tiempo real."""
    global modelo_clima
    
    # Cambiamos el texto del botón para que el usuario sepa que está cargando
    btn_entrenar.config(text="Entrenando... (Por favor espera)", state=tk.DISABLED)
    ventana.update() # Forzamos a la interfaz a actualizar este cambio visual

    try:
        # 1. Carga de datos
        df = pd.read_csv('weatherHistory.csv')

        # 2. Selección y limpieza
        df = df.dropna(subset=columnas_entrada + ['Daily Summary'])
        X = df[columnas_entrada]
        y = df['Daily Summary']

        # 3. Entrenamiento del modelo
        modelo = RandomForestClassifier(
            n_estimators=100,
            max_depth=None, 
            random_state=42,
            class_weight='balanced'
        )
        modelo.fit(X, y)

        # 4. Guardamos el modelo en la variable global
        modelo_clima = modelo
        
        # 5. Actualizamos la interfaz
        messagebox.showinfo("Éxito", "¡El modelo ha leído el CSV y se ha entrenado correctamente!")
        btn_entrenar.config(text="Modelo Entrenado Exitosamente")
        btn_predecir.config(state=tk.NORMAL) # Habilitamos el botón de predecir

    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'weatherHistory.csv'. Asegúrate de que esté en la misma carpeta.")
        btn_entrenar.config(text="Entrenar Modelo", state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al entrenar: {e}")
        btn_entrenar.config(text="Entrenar Modelo", state=tk.NORMAL)


def realizar_prediccion():
    """Recopila los datos de la interfaz y hace la predicción."""
    if modelo_clima is None:
        messagebox.showwarning("Atención", "Primero debes entrenar el modelo.")
        return

    try:
        # Obtener valores y convertirlos a float
        temp = float(entry_temp.get())
        temp_ap = float(entry_temp_ap.get())
        humedad = float(entry_humedad.get())
        viento_vel = float(entry_viento_vel.get())
        viento_dir = float(entry_viento_dir.get())
        visibilidad = float(entry_visibilidad.get())
        presion = float(entry_presion.get())

        # Crear el DataFrame
        datos_usuario = pd.DataFrame(
            [[temp, temp_ap, humedad, viento_vel, viento_dir, visibilidad, presion]], 
            columns=columnas_entrada
        )

        # Predecir
        resultado = modelo_clima.predict(datos_usuario)[0]
        
        # Mostrar el resultado
        label_resultado.config(text=f"Pronóstico: {resultado}", fg="blue")

    except ValueError:
        messagebox.showwarning(
            "Datos inválidos", 
            "Por favor, ingresa únicamente valores numéricos en todos los campos."
        )

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA INTERFAZ GRÁFICA (TKINTER)
# ---------------------------------------------------------

ventana = tk.Tk()
ventana.title("Predictor de Clima con Machine Learning")
ventana.geometry("400x550")
ventana.config(padx=20, pady=20)

tk.Label(ventana, text="1. Entrena la Inteligencia Artificial", font=("Arial", 12, "bold")).pack(pady=(0, 5))

# --- Botón de Entrenamiento ---
btn_entrenar = tk.Button(
    ventana, 
    text="Entrenar Modelo (Leer CSV)", 
    command=entrenar_modelo, 
    font=("Arial", 11), 
    bg="#2196F3", 
    fg="white",
    cursor="hand2"
)
btn_entrenar.pack(pady=(0, 15))

tk.Label(ventana, text="2. Ingresa los parámetros del clima", font=("Arial", 12, "bold")).pack(pady=10)

# --- Campos de entrada ---
frame_entradas = tk.Frame(ventana)
frame_entradas.pack()

def crear_campo(texto_etiqueta, fila):
    tk.Label(frame_entradas, text=texto_etiqueta, font=("Arial", 10)).grid(row=fila, column=0, sticky="e", pady=5, padx=5)
    entry = tk.Entry(frame_entradas, font=("Arial", 10), width=15)
    entry.grid(row=fila, column=1, pady=5)
    return entry

entry_temp = crear_campo("Temperatura (C):", 0)
entry_temp_ap = crear_campo("Temp. Aparente (C):", 1)
entry_humedad = crear_campo("Humedad (ej. 0.89):", 2)
entry_viento_vel = crear_campo("Velocidad viento (km/h):", 3)
entry_viento_dir = crear_campo("Dirección viento (grados):", 4)
entry_visibilidad = crear_campo("Visibilidad (km):", 5)
entry_presion = crear_campo("Presión (milibares):", 6)

# --- Botón de Predicción (Inicia deshabilitado) ---
btn_predecir = tk.Button(
    ventana, 
    text="Predecir Clima", 
    command=realizar_prediccion, 
    font=("Arial", 12, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    cursor="hand2",
    state=tk.DISABLED # Se habilita tras entrenar
)
btn_predecir.pack(pady=20)

# --- Etiqueta de resultado ---
label_resultado = tk.Label(ventana, text="Esperando datos...", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

ventana.mainloop()