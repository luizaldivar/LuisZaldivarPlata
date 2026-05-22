# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:03:53 2026

@author: zaldi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# # 1. Datos de ejemplo (coordenadas de ciudades)
data = {
    "Ciudad": ["A", "B", "C", "D", "E", "F"],
    "x": [1.0, 1.5, 10.0, 1.1, 0.8, 1.4],
    "y": [1.0, 1.2, 10.0, 0.9, 1.3, 0.8],
    "poblacion": [500, 50, 10, 400, 300, 200]  # Para contexto
}
df = pd.DataFrame(data)# 2. Preprocesamiento: Normalizar datos (opcional pero recomendado)
coords = df[["x", "y"]].values
coords_normalized = StandardScaler().fit_transform(coords) # Normaliza para evitar sesgos en escala

# 3. Aplicar DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=3) # Parámetros clave
clusters = dbscan.fit_predict(coords_normalized)

# 4. Asignar clusters al DataFrame
df["cluster"] = clusters
print(df.head()) # Mostrar los primeros registros para verificar
# Crear una figura con tamaño personalizado
plt.figure(figsize=(10, 6))

# Definir colores para cada cluster (azul para cluster 0, rojo para ruido)
colors = {0: "blue", -1: "red"}

# Iterar sobre cada grupo de puntos según su cluster
for cluster, group in df.groupby("cluster"):
    # Graficar los puntos:
    # - x: coordenada x original (sin normalizar)
    # - y: coordenada y original
    # - color: según el cluster
    # - tamaño (s): proporcional a la población (dividido entre 10 para ajustar)
    # - alpha: transparencia (0.7 = 70% opaco)
    plt.scatter(
        group["x"], group["y"],
        color=colors[cluster],
        label=f"Cluster {cluster}" if cluster != -1 else "Ruido",
        s=group["poblacion"] / 10,
        alpha=0.7
    )

# Personalizar el gráfico:
plt.title("Agrupamiento de Ciudades con DBSCAN (eps=0.5, min_samples=3)", fontsize=14)
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)
plt.legend() # Mostrar leyenda (cluster y ruido)
plt.grid(True) # Añadir cuadrícula
plt.show() # Mostrar el gráfico

# ==========================================
# # 4. RESULTADOS EN TABLA
# ==========================================
print("\nResultados de Clustering:")
print(df[["Ciudad", "x", "y", "cluster"]])