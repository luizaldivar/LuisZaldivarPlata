# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 08:51:12 2026

@author: zaldi
"""

#Problema 1: Control de Calidad en una Fábrica de Tornillos
#Una fábrica de tornillos afirma que el diámetro promedio de sus tornillos es de 10 mm. 
#Se toma una muestra aleatoria de 49 tornillos, obteniéndose un diámetro promedio de 9.7 mm con una desviación estándar de 0.5 mm.  

#¿Se puede concluir, con un nivel de significancia del 1%, que el diámetro medio es menor al teórico de 10 mm?  


import numpy as np
from scipy import stats
import pandas as pd

# Datos extraídos de la terminal
alpha = 0.01           # Nivel de significancia
mu_0 = 10              # Media teórica
x_bar = 9.7             # Media muestral
s = 0.5                  # Desviación estándar
n = 49                  # Tamaño de muestra

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para la prueba (una cola)
z_critical = stats.norm.ppf(1 - alpha)

# Comparacion de los valores usando valor absoluto
if abs(z) > z_critical:
    conclusion = "Rechazar la hipotesis nula"
else:
    conclusion = "No rechazar la hipotesis nula"

print(conclusion)
# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Parametros': [
        'Media teorica', 
        'Media muestral', 
        'Desviacion estandar', 
        'Tamaño de muestra', 
        'Z-calculado', 
        'Z-critico', 
        'Conclusion'
    ],
    'Valores': [
        mu_0, 
        x_bar, 
        s, 
        n, 
        z, 
        z_critical, 
        conclusion
    ]
})

print(df)


#el diametro medido es mucho menor al teorico de 10 mm

#Problema 2: Duración de Baterías de Celulares
#Un fabricante de celulares asegura que la duración promedio de sus baterías es de 20 horas. Se toma una muestra de 30 baterías y se encuentra que su duración promedio es de 18.5 horas, con una desviación estándar de 2.5 horas.  

#Con un nivel de significancia del 5%, ¿se puede concluir que la duración de las baterías es menor a la especificada por el fabricante?  
import numpy as np
from scipy import stats
import pandas as pd

# Datos extraídos de la terminal
alpha = 0.05          # Nivel de significancia
mu_0 = 20             # Media teórica
x_bar = 18.5             # Media muestral
s = 2.5                  # Desviación estándar
n = 30                  # Tamaño de muestra

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para la prueba (una cola)
z_critical = stats.norm.ppf(1 - alpha)

# Comparacion de los valores
# Comparacion de los valores usando valor absoluto
if abs(z) > z_critical:
    conclusion = "Rechazar la hipotesis nula"
else:
    conclusion = "No rechazar la hipotesis nula"

print(conclusion)

# Crear un DataFrame con los datos
df2 = pd.DataFrame({
    'Parametros': [
        'Media teorica', 
        'Media muestral', 
        'Desviacion estandar', 
        'Tamaño de muestra', 
        'Z-calculado', 
        'Z-critico', 
        'Conclusion'
    ],
    'Valores': [
        mu_0, 
        x_bar, 
        s, 
        n, 
        z, 
        z_critical, 
        conclusion
    ]
})

print(df2)  



#Problema 3: Control de Peso en una Planta de Alimentos
#Un productor de harina en bolsa indica que el peso promedio de sus bolsas es de 1 kg (1000 gramos). Para verificarlo, se toman 40 bolsas y se obtiene un peso promedio de 990 gramos, con una desviación estándar de 12 gramos.  

#Si se usa un nivel de significancia del 2%, ¿se puede concluir que las bolsas tienen un peso menor al anunciado?
# Datos extraídos de la terminal
alpha = 0.02          # Nivel de significancia
mu_0 = 1000             # Media teórica
x_bar = 990             # Media muestral
s = 12                  # Desviación estándar
n = 40                  # Tamaño de muestra

# Calculo del estadistico de prueba Z
z = (x_bar - mu_0) / (s / np.sqrt(n))

# Valor critico para la prueba (una cola)
z_critical = stats.norm.ppf(1 - alpha)

# Comparacion de los valores
# Comparacion de los valores usando valor absoluto
if abs(z) > z_critical:
    conclusion = "Rechazar la hipotesis nula"
else:
    conclusion = "No rechazar la hipotesis nula"

print(conclusion)

# Crear un DataFrame con los datos
df3 = pd.DataFrame({
    'Parametros': [
        'Media teorica', 
        'Media muestral', 
        'Desviacion estandar', 
        'Tamaño de muestra', 
        'Z-calculado', 
        'Z-critico', 
        'Conclusion'
    ],
    'Valores': [
        mu_0, 
        x_bar, 
        s, 
        n, 
        z, 
        z_critical, 
        conclusion
    ]
})

print(df3)  

