# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:32:00 2026

@author: zaldi
"""


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
#===================reseñas=================
data = {
        "Reseña":[
            "el producto funciona perfectamente",
            "muy buena calidad",
            "el producto llego dañado",
            "muy mala calidad",
            "excelente producto de calidad",
            "mala calidad"],
        "clasificacion":[
            "satisfecho","satisfecho","insatisfeco","insatisfecho","satisfecho","insatisfecho"]
        }
df = pd.DataFrame(data)
print(df)

#matriz de caracteristicas
vectorizador = CountVectorizer()
x = vectorizador.fit_transform(df['Reseña'])
print(x.toarray())
#variable objetivo
y = df['clasificacion']

#entrenar el modelo de Naive bAYES
modelo = MultinomialNB()
modelo.fit(x , y)
#predecir la clase de un nuevo correo
nuevo_correo = ["producto mala calidad"]
correo_vectorizado = vectorizador.transform(nuevo_correo)
prediccion = modelo.predict(correo_vectorizado)
print(prediccion)




#=====noticias====
datanoticias = {
        "Noticias":[
            "equipo gana campeonato",
            "nuevo telefono inteligente",
            "jugador anota gol",
            "empresa lanza nueva computadora",
            "equipo gana torneo"],
        "categoria":[
            "deportes","tecnologia","deportes","tecnologia","deportes"]
        }
df2 = pd.DataFrame(datanoticias)
print(df2)

#matriz de caracteristicas
vectorizador2 = CountVectorizer()
x2 = vectorizador2.fit_transform(df2['Noticias']) # Corregido: vectorizador2 y df2
print(x2.toarray()) # Corregido: x2

#variable objetivo
y2 = df2['categoria'] # Corregido: df2

#entrenar el modelo de Naive Bayes
modelo2 = MultinomialNB()
modelo2.fit(x2 , y2) # Corregido: modelo2 y x2

#predecir la clase de una nueva noticia
nuevo_correo2 = ["nuevo equipo gana"]
correo_vectorizado2 = vectorizador2.transform(nuevo_correo2) # Corregido: vectorizador2 y nuevo_correo2
prediccion2 = modelo2.predict(correo_vectorizado2) # Corregido: modelo2 y correo_vectorizado2
print(prediccion2) # Corregido: prediccion2