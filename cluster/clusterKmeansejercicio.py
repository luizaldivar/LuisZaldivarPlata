# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:08:55 2026

@author: zaldi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#======================ejercicio 1==========
data = {
        'Compras_Mes':[1, 2, 1.5, 10, 12, 11, 4, 5, 6],
        'Gasto_mensual':[ 2, 3, 2.5, 9, 11, 10, 5, 6, 7]
        }

df = pd.DataFrame(data)
df

#2 graficar los puntos
plt.scatter(df['Compras_Mes'],df['Gasto_mensual'])
plt.xlabel('Compras del mes')
plt.ylabel('Gasto mensual')
plt.title('Datos sin clasificar')
plt.show

#metodo del codo para encontrar K
X = df[['Compras_Mes','Gasto_mensual']].values
inercias = []

for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)


#Graficar el metodo
plt.plot(range(1, 8), inercias, marker='o')
plt.xlabel('Numero de clusters (K)')
plt.ylabel('Inercia')
plt.title('Metodo del codo')
plt.show()

#aplicamos K means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
df

#Mostrar los Clusters
centroides = kmeans.cluster_centers_
centroides
#graficar los clusters con los centroides
colores = ['red', 'green', 'blue']
for i in range(3):
    puntos = df[df['Cluster'] == i]
    plt.scatter(puntos['Compras_Mes'], puntos['Gasto_mensual'], c=colores[i], label=f'Cluster {i}')
    # Esta línea necesita estar indentada para usar la 'i' del ciclo for
    plt.scatter(centroides[i, 0], centroides[i, 1], c=colores[i], marker='X', s=100, label=f'Centroides {i}')

plt.xlabel('Compras Mes')
plt.ylabel('Gasto Mensual')
plt.title('Clusters y Centroides')
plt.legend()
plt.show()

 #¿Qué tipo de clientes representa cada grupo?
#existen clientes ocasionales(aquellos que compran poco y gastan poco), 
#clientes regulares(representan una compra o gasto moderados) clientes frecuentes(compran mucho y gastan mucho)           


#======================ejercicio 2  Agrupamiento de personas según salud física==========
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data2 = {
        'Ejercicio':[0.5, 1, 1.5, 6, 7, 8, 2, 3, 4],
        'Condicion':[2, 3, 2.5, 8, 9, 10, 4, 5, 6]
        }

df2 = pd.DataFrame(data2)
df2

plt.scatter(df2['Ejercicio'],df2['Condicion'])
plt.xlabel('Horas de ejercicio por semana')
plt.ylabel('Nivel de condición física')
plt.title('Datos sin clasificar')
plt.show

X2 = df2[['Ejercicio','Condicion']].values
inercias2 = []

for k2 in range(1, 8):
    kmeans2 = KMeans(n_clusters=k2, random_state=42)
    kmeans2.fit(X2)
    inercias2.append(kmeans2.inertia_)


plt.plot(range(1, 8), inercias2, marker='o')
plt.xlabel('Numero de clusters (K)')
plt.ylabel('Inercia')
plt.title('Metodo del codo')
plt.show()

kmeans_final = KMeans(n_clusters=3, random_state=42)
df2['Cluster'] = kmeans_final.fit_predict(X2)
df2

centroides2 = kmeans_final.cluster_centers_
centroides2

colores2 = ['red', 'green', 'blue']
for i2 in range(3):
    puntos2 = df2[df2['Cluster'] == i2]
    plt.scatter(puntos2['Ejercicio'], puntos2['Condicion'], c=colores2[i2], label=f'Cluster {i2}')
    plt.scatter(centroides2[i2, 0], centroides2[i2, 1], c=colores2[i2], marker='X', s=100, label=f'Centroides {i2}')

plt.xlabel('Horas de ejercicio')
plt.ylabel('Condición física')
plt.title('Clusters y Centroides')
plt.legend()
plt.show() 
# Se observan 3 grupos de personas, con baja condicion y poco ejercicio, condicion y ejercicio intermedio y las que tienen alta condicion y hacen mucho ejercicio

#=============0000ejercicio3=================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data3 = {
        'Ventas':[2, 3, 2.5, 15, 18, 20, 5, 6, 7],
        'Ingresos':[3, 4, 3.5, 9, 10, 10, 5, 6, 7]
        }

df3 = pd.DataFrame(data3)
df3

plt.scatter(df3['Ventas'],df3['Ingresos'])
plt.xlabel('Número de ventas mensuales')
plt.ylabel('Nivel de ingresos generados')
plt.title('Datos sin clasificar')
plt.show

X3 = df3[['Ventas','Ingresos']].values
inercias3 = []

for k3 in range(1, 8):
    kmeans3 = KMeans(n_clusters=k3, random_state=42)
    kmeans3.fit(X3)
    inercias3.append(kmeans3.inertia_)


plt.plot(range(1, 8), inercias3, marker='o')
plt.xlabel('Numero de clusters (K)')
plt.ylabel('Inercia')
plt.title('Metodo del codo')
plt.show()

kmeans_productos = KMeans(n_clusters=3, random_state=42)
df3['Cluster'] = kmeans_productos.fit_predict(X3)
df3

centroides3 = kmeans_productos.cluster_centers_
centroides3

colores3 = ['red', 'green', 'blue']
for i3 in range(3):
    puntos3 = df3[df3['Cluster'] == i3]
    plt.scatter(puntos3['Ventas'], puntos3['Ingresos'], c=colores3[i3], label=f'Cluster {i3}')
    plt.scatter(centroides3[i3, 0], centroides3[i3, 1], c=colores3[i3], marker='X', s=100, label=f'Centroides {i3}')

plt.xlabel('Ventas mensuales')
plt.ylabel('Ingresos generados')
plt.title('Clusters y Centroides')
plt.legend()
plt.show()          

#Se observan 3 grupos de productos: aquellos de bajo rendimiento con pocas ventas y bajos ingresos, 
#los de rotación media que mantienen ventas e ingresos intermedios, 
#y los productos estrella que registran un alto volumen de ventas junto con una gran generación de ingresos.