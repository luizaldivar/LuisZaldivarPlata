# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 08:21:04 2026

@author: zaldi
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
data = {
    "Horas_estudio": [1,2,1.5,8,9,8.5,3,3.5,4],
    "Calificaciones": [2,3,2.5,9,10,9.5,5,5.5,6]
}

df = pd.DataFrame(data)
df
#Visualizacion
plt.scatter(df["Horas_estudio"], df["Calificaciones"])
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")
plt.title("Datos de los estudiantes")
plt

#Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(df)
#Mostrar los centroides
centroides = kmeans.cluster_centers_
centroides
df['Cluster'] = kmeans.labels_
df
#Visualizamos los centroides
plt.scatter(df["Horas_estudio"], df["Calificaciones"], c=df['Cluster'])
plt.scatter(centroides[:, 0], centroides[:, 1], marker='X', color='red', s= 200, label='Centroides')
plt.legend()
plt.show()

#=============================metodo codo===========================
def elbow_method(data, max_clusters=10):
    """
    Aplica el método del codo para seleccionar el número óptimo de clusters en k-means.
    Parámetros:
    ----------
    data : matriz o matriz dispersa, forma (n_samples, n_features)
        Los datos de entrada.
    max_clusters : int, opcional (por defecto=10)
        El número máximo de clusters a considerar.
    """
    sum_of_squared_distances = []
    for k in range(1, max_clusters+1):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        sum_of_squared_distances.append(kmeans.inertia_)
    # Graficar la curva del codo
    plt.plot(range(1, max_clusters+1), sum_of_squared_distances, 'bx-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Suma de las Distancias al Cuadrado')
    plt.title('Curva del Codo')
    plt.show()
from sklearn.datasets import make_blobs
# Aplica el método del codo
elbow_method(df.drop(columns=['Cluster']), max_clusters=8)
