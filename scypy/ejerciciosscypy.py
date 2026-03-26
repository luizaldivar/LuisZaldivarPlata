# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:25:22 2026

@author: zaldi
"""

#Un analista quiere comparar el rendimiento (km/litro) de dos tipos de gasolina (A y B).
#Gasolina A: [12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1]
#Gasolina B: [14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1]
#¿Existe una diferencia significativa en el rendimiento entre ambos tipos de gasolina?

import numpy as np
from scipy import stats

# 1) Datos de la muestra
GasolinaA= np.array([12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1])
GasolinaB= np.array([14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1])

# 2) Ejecuta la prueba t de 2 muestras independientes
# equal_var=False para varianzas desiguales
res = stats.ttest_ind(GasolinaA, GasolinaB, equal_var=False)

# 3) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 4) Define el nivel de significancia
alpha = 0.05

# 5) Muestra resultados y decide
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

if p_value < alpha:
    print("Rechazo H0: hay diferencia significativa entre los dos tipos de gasolina.")
else:
    print("No rechazo H0: no hay evidencia suficiente de diferencia entre los grupos.")
    
    
    
#Ejercicio 7: Efecto de un fertilizante
#Un agricultor mide la altura de 10 plantas (en cm) antes de aplicar un fertilizante orgánico y vuelve a medirlas una semana después.
#Antes: [15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7]
#Después: [15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8]
#¿Ha provocado el fertilizante un crecimiento significativo en la altura de las plantas en esa semana?
import numpy as np
from scipy import stats

# 1) Datos de la muestra
Antes= np.array([15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7])
Despues= np.array([15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8])

# 2) Ejecuta la prueba t de 2 muestras independientes
# equal_var=False para varianzas desiguales
res = stats.ttest_ind(Antes, Despues, equal_var=False)

# 3) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 4) Define el nivel de significancia
alpha = 0.05

# 5) Muestra resultados y decide
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

if p_value < alpha:
    print("Rechazo H0: hay diferencia significativa entre aplicar fertilizante y no aplicarlo.")
else:
    print("No rechazo H0: no hay evidencia suficiente de diferencia entre los grupos, se recomienda aplicar fertilizante.")
    


#Ejercicio 1: 
#Una empresa de tecnología afirma que el tiempo promedio que sus empleados tardan en resolver un ticket de soporte es de 45 minutos. Para verificar esta afirmación, se toma una muestra aleatoria de 25 empleados y se mide el tiempo (en minutos) que cada uno tarda en resolver un ticket. ¿El tiempo promedio de resolución de la muestra es significativamente diferente de 45 minutos?
import numpy as np
from scipy import stats
empleados = np.array([
    60,20,30,49,58,57,33,54,40,42,32,35,38,39,61,33,22,49,58,40,42,54,23,45,38
    ])
# 2) Valor hipotético de la media bajo H0
mu0 = 40

# 3) Ejecuta la prueba t de 1 muestra
# sintaxis para ttest_1samp: ttest_1samp(a, popmean) donde a es la muestra y 
# popmean es el valor bajo H0
res = stats.ttest_1samp(empleados, mu0)

# 4) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 5) Define el nivel de significancia (alpha)
alpha = 0.05

# 6) Decide si rechazas H0
print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la media es distinta de 40 minutos.")
else:
    print("No rechazo H0: no hay evidencia suficiente para decir que la media difiere de 40 minutos.")
    
        
