# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:35:45 2026

@author: zaldi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler




# 1. Cargar el archivo CSV hecho con tus datos
df = pd.read_csv('ejercicio_1_zonas_entrega.csv')

# 2. Preprocesamiento: Normalizar datos
coords = df[["X", "Y"]].values
coords_normalized = StandardScaler().fit_transform(coords) 

# 3. Aplicar DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=3) 
clusters = dbscan.fit_predict(coords_normalized)

# 4. Asignar clusters al DataFrame
df["cluster"] = clusters
print(df.head()) # Mostrar los primeros registros para verificar

# ==========================================
# GRAFICACIÓN
# ==========================================
plt.figure(figsize=(10, 6))

# CORRECCIÓN 1: Se definen colores para los clusters (0 y 1) y para el ruido (-1)
colors = {0: "blue", 1: "green", -1: "red"}

# Iterar sobre cada grupo de puntos según su cluster
for cluster, group in df.groupby("cluster"):
    # Graficar los puntos
    plt.scatter(
        group["X"], group["Y"],
        color=colors[cluster],
        # CORRECCIÓN 2: El ruido en DBSCAN siempre se identifica con el valor -1
        label=f"Cluster {cluster}" if cluster != -1 else "Ruido",
        # CORRECCIÓN 3: Tamaño fijo (50) ya que la tabla original no tiene columna de población
        s=50,
        alpha=0.7
    )

# Personalizar el gráfico:
plt.title("Agrupamiento de zonas de entregas con DBSCAN (eps=0.5, min_samples=3)", fontsize=14)
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)
plt.legend() 
plt.grid(True) 
plt.show() 

# ==========================================
# # 4. RESULTADOS EN TABLA
# ==========================================
print("\nResultados de Clustering:")
# CORRECCIÓN 4: Nombres de columnas idénticos a los de tu imagen (Punto, X, Y)
print(df[["Punto", "X", "Y", "cluster"]])

#Se identificaron 2 zonas de entrega 

#=========EJERCICIO 2============
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 2026
Ejercicio 2 — Segmentación de sensores ambientales
@author: zaldi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# 1. Cargar datos en un DataFrame
df = pd.read_csv('ejercicio_2_sensores_ambientales.csv')
features = ["Temperatura_C", "Humedad_pct"]
coords = df[features].values

# 2. Preprocesamiento: Escalar datos con StandardScaler
scaler = StandardScaler()
coords_normalized = scaler.fit_transform(coords) 

# 3. Grafico k-distancia para elegir eps adecuado
min_samples = 3
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(coords_normalized)
distances, indices = neighbors_fit.kneighbors(coords_normalized)

distances_sorted = np.sort(distances[:, min_samples-1], axis=0)

plt.figure(figsize=(8, 4))
plt.plot(distances_sorted, color="blue", lw=2, label="K-distancia")
plt.axhline(y=0.4, color="red", linestyle="--", label="eps sugerido = 0.4")
plt.title("Paso 3: Gráfico de K-distancia (Método del Codo)", fontsize=12, fontweight='bold')
plt.xlabel("Puntos ordenados por distancia", fontsize=10)
plt.ylabel(f"Distancia al {min_samples}º vecino más cercano", fontsize=10)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.7)
plt.show()

# 4. Aplicar DBSCAN y agregar columna Cluster
eps_elegido = 0.4
dbscan = DBSCAN(eps=eps_elegido, min_samples=min_samples) 
clusters = dbscan.fit_predict(coords_normalized)
df["cluster"] = clusters

print("\nResultados de Clustering de Sensores:")
print(df[["Sensor", "Temperatura_C", "Humedad_pct", "cluster"]])

# 5. Graficar los clusters + anomalías detectadas
plt.figure(figsize=(10, 6))
colors = {0: "blue", 1: "green", 2: "purple", -1: "red"}
labels = {
    0: "Cluster 0: Frío / Seco", 
    1: "Cluster 1: Cálido / Húmedo", 
    2: "Cluster 2: Templado", 
    -1: "Anomalía (Ruido)"
}

for cluster, group in df.groupby("cluster"):
    plt.scatter(
        group["Temperatura_C"], group["Humedad_pct"],
        color=colors[cluster],
        label=labels[cluster],
        s=60,
        alpha=0.8,
        edgecolors='black',
        linewidths=0.6
    )

plt.title(f"Segmentación Ambiental con DBSCAN (eps={eps_elegido}, min_samples={min_samples})", fontsize=14, fontweight='bold')
plt.xlabel("Temperatura (°C)", fontsize=12)
plt.ylabel("Humedad (%)", fontsize=12)
plt.legend(loc="best") 
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu May 21 2026
Ejercicio 3 — Análisis de patrones de fraude bancario
@author: zaldi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# 1. Crear DataFrame con columnas Monto y Hora
df = pd.read_csv('fraude_bancario.csv')
features = ["Monto_USD", "Hora_Dia"]
coords = df[features].values

# 2. Escalar los datos con StandardScaler
scaler = StandardScaler()
coords_normalized = scaler.fit_transform(coords) 

# 3. Aplicar el gráfico k-distancia para determinar eps
min_samples = 3
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(coords_normalized)
distances, indices = neighbors_fit.kneighbors(coords_normalized)

distances_sorted = np.sort(distances[:, min_samples-1], axis=0)

plt.figure(figsize=(8, 4))
plt.plot(distances_sorted, color="blue", lw=2, marker='s', markersize=4, label="K-distancia transacciones")
plt.axhline(y=0.5, color="red", linestyle="--", label="eps determinado = 0.5")
plt.title("Paso 3: Gráfico de K-distancia (Análisis de Fraude)", fontsize=12, fontweight='bold')
plt.xlabel("Puntos ordenados por distancia", fontsize=10)
plt.ylabel(f"Distancia al {min_samples}º vecino más cercano", fontsize=10)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.7)
plt.show()

# 4. Aplicar DBSCAN y etiquetar transacciones
eps_determinado = 0.5
dbscan = DBSCAN(eps=eps_determinado, min_samples=min_samples) 
clusters = dbscan.fit_predict(coords_normalized)
df["cluster"] = clusters

# Etiquetamos según el comportamiento de la densidad encontrado
def asignar_etiqueta(cluster_id):
    if cluster_id == 0:
        return "Normal"
    elif cluster_id == 1:
        return "Sospechosa (Patrón Grupal)"
    else:
        return "Fraude Detectado (Aislado)"

df["Estado_DBSCAN"] = df["cluster"].apply(asignar_etiqueta)

# 5. Graficar las transacciones diferenciando perfiles
plt.figure(figsize=(10, 6))
colors = {0: "#3182ce", 1: "#dd6b20", -1: "#e53e3e"}
labels = {
    0: "Transacciones Normales (Cluster 0)", 
    1: "Patrón Sospechoso Nocturno/Alto (Cluster 1)", 
    -1: "Fraudes Críticos Detectados (Ruido)"
}

for cluster, group in df.groupby("cluster"):
    plt.scatter(
        group["Hora_Dia"], group["Monto_USD"],
        color=colors[cluster],
        label=labels[cluster],
        s=80,
        alpha=0.9,
        edgecolors='black',
        linewidths=0.7
    )

plt.title("Paso 5: Detección de Patrones de Fraude Bancario mediante DBSCAN", fontsize=14, fontweight='bold')
plt.xlabel("Hora del Día (Formato 24h)", fontsize=12)
plt.ylabel("Monto de la Transacción (USD)", fontsize=12)
plt.legend(loc="upper right", frameon=True, shadow=True)
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# 6. Calcular el porcentaje de transacciones sospechosas y anómalas
total_transacciones = len(df)
alertas_sospechosas = (df["cluster"] == 1).sum()
alertas_fraude = (df["cluster"] == -1).sum()

pct_sospechosas = (alertas_sospechosas / total_transacciones) * 100
pct_fraudes = (alertas_fraude / total_transacciones) * 100
pct_total_alertas = ((alertas_sospechosas + alertas_fraude) / total_transacciones) * 100

print(f"\n--- Métricas del Sistema de Monitoreo ---")
print(f"Porcentaje de Transacciones Sospechosas (Cluster 1): {pct_sospechosas:.1f}%")
print(f"Porcentaje de Fraudes Críticos (Ruido -1): {pct_fraudes:.1f}%")
print(f"Porcentaje Total de Transacciones Alertadas: {pct_total_alertas:.1f}%")