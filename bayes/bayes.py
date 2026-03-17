# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:12:14 2026

@author: zaldi
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

import pandas as pd

data = {
        "correo":[
            "gana dinero rapido",
            "oferta exclusiva gratis",
            "reunion mañana",
            "adjunto el reporte",
            "gana el premio gratis"],
        "clase":[
            "spam","spam","no spam","no spam","spam"]
        }
df = pd.DataFrame(data)
print(df)

#matriz de caracteristicas
vectorizador = CountVectorizer()
x = vectorizador.fit_transform(df['correo'])
print(x.toarray())
#variable objetivo
y = df['clase']

#entrenar el modelo de Naive bAYES
modelo = MultinomialNB()
modelo.fit(x , y)
#predecir la clase de un nuevo correo
nuevo_correo = ["Oferta especial"]
correo_vectorizado = vectorizador.transform(nuevo_correo)
prediccion = modelo.predict(correo_vectorizado)
print(prediccion)