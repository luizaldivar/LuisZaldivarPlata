# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:29:56 2026

@author: zaldi
"""

# --- 1. IMPORTACIÓN DE LIBRERÍAS ---
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

# --- 2. DEFINICIÓN DE DATOS ---
X = np.array([
    [20, 100],
    [22, 120],
    [23, 140],
    [45, 700],
    [46, 750],
    [48, 720],
    [60, 1500],
    [62, 1600]
])
# # Etiquetas para identificar puntos en las gráficas
nombres = ["A", "B", "C", "D", "E", "F","G","H"]

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
plt.xlabel("Edad")
plt.ylabel("Gasto mensual")
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
plt.xlabel("Edad")
plt.ylabel("Gasto Mensual")
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
plt.xlabel("Edad")
plt.ylabel("Gasto mensual")
plt.grid(True)

plt.show()

#¿Qué clientes parecen más similares?
#Los clientes  de entre 40 y 50 años de edad

#Que  grupos naturales identifica el algoritmo?
#Identifica 3 ggrupos, de los cuales los de 20 y 40-50 estan mas unidos

#¿Qué representa cada cluster desde el punto de vista comercial?
#Cada segmento en donde la gente con mayor edad gasta mucho mas

#¿Cuál sería una estrategia de marketing para cada grupo?
#enfocarse mas en adultos de mediana y avanzada edad

#¿Por qué el algoritmo agrupa ciertos clientes?
#por que son la edad o etapa de la vida que lo conforman, agrupa a chicos a inicios de sus 20 por que a esa edad uno gasta menos al tener menos ingresos.
