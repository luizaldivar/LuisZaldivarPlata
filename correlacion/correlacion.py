# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 07:31:39 2026

@author: zaldi
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('datos_estudiantes_decision.csv')
df.info()
df.head()

#horas de estudio vs calificacion
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="horas_estudio", y="calificacion")
plt.title("Horas de estudio vs calificacion")
plt.xlabel("horas de estudio")
plt.ylabel("calificacion")
plt.show()

#horas_sueno vs nivel_estres
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="horas_sueno", y="nivel_estres")
plt.title("Horas de sueño vs nivel de estres")
plt.xlabel("horas de sueño")
plt.ylabel("nivel de estres")
plt.show()

#uso_redes vs calificacion
plt.Figure(figsize=(6,4))
plt.scatter(data=df, x="uso_redes", y="calificacion")
plt.title("uso de redes sociales vs calificacion")
plt.xlabel("uso de redes sociales")
plt.ylabel("calificacion")
plt.show()

#Pearson para las 3
Pearson_estudio_calf = df['horas_estudio'].corr(df['calificacion'], method='pearson')
Pearson_sueno_estres = df['horas_sueno'].corr(df['nivel_estres'], method='pearson')
Pearson_redes_calf = df['uso_redes'].corr(df['calificacion'], method='pearson')
print("Pearson: \n")
print("Horas de estudio vs calificacion:",Pearson_estudio_calf)
print("Horas de sueño vs nivel de estres:",Pearson_sueno_estres)
print("Horas de uso de redes vs calificacion ",Pearson_redes_calf)   

#para la grafica de Horas de estudio vs calificacion se presento una relacion lineal

#para la grafica de Horas de sueño vs nivel de estres se presento una relacion monotona pero no lineal

#para la grafica de redes vs calificacion se presento una relacion no monotona

#Decision de metodo: para la grafica de Horas de estudio vs calificacion, se prefiere el metodo de Pearson
#por que presenta un patron lineal y son variables cuantittativos

#para el resto de graficas se preferiria spearman por que los datos no son monotonos y 
#tienen alta variacion entre los datos
