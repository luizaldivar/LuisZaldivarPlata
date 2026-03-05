# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 07:28:47 2026

@author: zaldi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:31:39 2026

@author: zaldi
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('streaming_platform.csv')
df.info()
df.head()

#horas de estudio vs calificacion
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="hours_watched_per_week", y="age")
plt.title("hours_watched_per_week vs age")
plt.xlabel("hours_watched_per_week")
plt.ylabel("age")
plt.show()

#horas_sueno vs nivel_estres
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="device_type", y="number_of_sessions")
plt.title("device_type vs number_of_sessions")
plt.xlabel("device_type")
plt.ylabel("number_of_sessions")
plt.show()

#uso_redes vs calificacion
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="age", y="favorite_genre")
plt.title("age vs favorite_genre")
plt.xlabel("age")
plt.ylabel("favorite_genre")
plt.show()

#Pearson para las 3
Pearson_estudio_hours = df['hours_watched_per_week'].corr(df['age'], method='pearson')
Pearson_device_type = df['device_type'].corr(df['number_of_sessions'], method='pearson')
Pearson_generoedad = df['age'].corr(df['favorite_genre'], method='pearson')
print("Pearson: \n")
print("Horas miradas vs edad:",Pearson_estudio_hours)
print("Dispositivo vs horas de sesion:",Pearson_device_type)
print("genero vs edad ",Pearson_generoedad)   


