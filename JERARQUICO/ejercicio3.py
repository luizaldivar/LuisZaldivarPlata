# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:41:49 2026

@author: zaldi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:41:32 2026

@author: zaldi
"""

# --- 1. IMPORTACIÓN DE LIBRERÍAS ---
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

# --- 2. DEFINICIÓN DE DATOS ---
X = np.array([
    [95, 98],  # Alumno A
    [92, 94],  # Alumno B
    [88, 90],  # Alumno C
    [65, 70],  # Alumno D
    [60, 68],  # Alumno E
    [58, 62],  # Alumno F
    [30, 40],  # Alumno G
    [35, 38]   # Alumno H
])
# # Etiquetas para identificar puntos en las gráficas
nombres = ["A", "B", "C", "D", "E", "F", "G", "H"]

# --- 3. VISUALIZAR LOS DATOS ORIGINALES ---
# # Antes de aplicar el algoritmo, observamos los puntos.
plt.scatter(
    X[:, 0],  # # todas las filas de columna X
    X[:, 1]   # # todas las filas de columna Y
)

# # Agregamos nombre a cada punto
for nombre, (x, y) in zip(nombres, X):  # #zip() combina dos listas en una sola
    plt.annotate(nombre, (x, y))  # #annotate() agrega texto a un punto específico en la gráfica

plt.title("Datos originales")
plt.xlabel("Promedio")
plt.ylabel("Asistencia")
plt.grid(True)

plt.show()



# # 4. CONSTRUIR LA JERARQUÍA (LINKAGE)

Z = linkage(
    X,
    method='ward',
    metric='euclidean'
)


# # 5. EXPLICAR MATRIZ LINKAGE

# # La matriz Z contiene:
# # [cluster1, cluster2, distancia, cantidad_elementos]
print("Matriz Linkage:\n")
print(Z)
# # 6. DENDROGRAMA

dendrogram(
    Z,
    
    # # Reemplazar índices 0,1,2 por A,B,C
    labels=nombres
)

plt.title("Dendrograma del Clustering Jerárquico")
plt.xlabel("Puntos")
plt.ylabel("Distancia")

plt.grid(True)

plt.show()


# # 7. CREAR EL MODELO AGLOMERATIVO (PRUEBA CON 2 CLUSTERS)

modelo_2 = AgglomerativeClustering(
    n_clusters=2,
    linkage='ward'
)


# # 8. ENTRENAR EL MODELO

etiquetas_2 = modelo_2.fit_predict(X)


# --- 10. GRAFICAR RESULTADO FINAL ---
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=etiquetas_2
)

# # Agregar letras a cada punto
for nombre, (x, y) in zip(nombres, X):
    plt.annotate(nombre, (x, y))

plt.title("Resultado del Clustering Jerárquico Aglomerativo (2 Clusters)")
plt.xlabel("Promedio")
plt.ylabel("Asistencia")
plt.grid(True)

plt.show()


# # 7. CREAR EL MODELO AGLOMERATIVO (PRUEBA CON 3 CLUSTERS)

modelo_3 = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'
)


# # 8. ENTRENAR EL MODELO

etiquetas_3 = modelo_3.fit_predict(X)


# --- 10. GRAFICAR RESULTADO FINAL ---
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=etiquetas_3
)

# # Agregar letras a cada punto
for nombre, (x, y) in zip(nombres, X):
    plt.annotate(nombre, (x, y))

plt.title("Resultado del Clustering Jerárquico Aglomerativo (3 Clusters)")
plt.xlabel("Promedio")
plt.ylabel("Asistencia")
plt.grid(True)

plt.show()

#¿Qué alumnos se parecen más?
#los quwe tienen un promedio y asistencia de 60
#¿Qué perfiles de estudiantes aparecen?
#3 los que asisten poco y tienen mal promedio, los que asisten intermedio y tienen promedio regular y los que siempre asisten y tienen buen promedio
#¿Qué decisión institucional podría tomarse con esta información?
#enfocarse en los que asisten menos
#¿Qué ocurre cuando el número de clusters cambia?
# el programa considera a los que asisten poco y regular como un solo cluster
#¿Qué grupo requeriría más intervención académica?
#los que asisten poco