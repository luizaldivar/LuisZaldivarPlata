# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:22:25 2026

@author: zaldi
"""




# --- 1. IMPORTACIÓN DE LIBRERÍAS ---
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import AgglomerativeClustering

# --- 2. DEFINICIÓN DE DATOS ---
X = np.array([
    [1, 1],   # A
    [2, 1],   # B
    [5, 5],   # C
    [6, 5],   # D
    [10,10],  # E
    [11,10]   # F
])
# # Etiquetas para identificar puntos en las gráficas
nombres = ["A", "B", "C", "D", "E", "F"]

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
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
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


# # 7. CREAR EL MODELO AGLOMERATIVO

modelo = AgglomerativeClustering(
    n_clusters=3,
    linkage='ward'
)


# # 8. ENTRENAR EL MODELO

etiquetas = modelo.fit_predict(X)


# --- 10. GRAFICAR RESULTADO FINAL ---
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=etiquetas
)

# # Agregar letras a cada punto
for nombre, (x, y) in zip(nombres, X):
    plt.annotate(nombre, (x, y))

plt.title("Resultado del Clustering Jerárquico Aglomerativo")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()



#¿Qué puntos se unen primero y por qué?
#se unen primero los pares (A, B), (C, D) y (E, F) porque son los puntos más cercanos entre sí, con una distancia de solo 1 unidad.




#¿Qué sucede al cortar el dendrograma en una altura pequeña?
# Se obtienen muchos clusters con pocos elementos, manteniendo un alto nivel de detalle y 
#separación entre los datos.


#¿Qué significa la altura donde se unen dos ramas? Representa el nivel 
#de distancia o disimilitud (en este caso, el incremento de varianza interna 
#por el método Ward) en el que se fusionan esos grupos.



#¿Cuántos clusters aparecen al cortar aproximadamente en distancia 8? Aparecen 2 clusters,
# ya que a esa altura los grupos más cercanos ya se habrán fusionado, dejando solo dos grandes bloques separados.