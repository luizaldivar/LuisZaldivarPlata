# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:03:22 2026

@author: zaldi
"""

import numpy as np
from scipy import stats

# 1) Datos: calificaciones registradas de los estudiantes
scores = np.array([
    72, 68, 75, 70, 66, 74, 71, 69, 73, 67,
    70, 72, 65, 76, 68, 71, 69, 74, 70, 66,
    73, 67, 72, 68, 75, 69, 71, 70, 74, 66
])

# 2) Valor hipotético de la media bajo H0
mu0 = 70

# 3) Ejecuta la prueba t de 1 muestra
# sintaxis para ttest_1samp: ttest_1samp(a, popmean) donde a es la muestra y 
# popmean es el valor bajo H0
res = stats.ttest_1samp(scores, mu0)

# 4) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 5) Define el nivel de significancia (alpha)
alpha = 0.05

# 6) Decide si rechazas H0
print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la media es distinta de 70.")
else:
    print("No rechazo H0: no hay evidencia suficiente para decir que la media difiere de 70.")
    
    
import numpy as np
from scipy import stats

# 1) Datos de la muestra
hombres = np.array([78, 85, 90, 72, 88, 76, 95, 83, 79, 87, 91, 74, 86, 80, 93])
mujeres = np.array([62, 70, 65, 68, 74, 60, 72, 66, 71, 63, 69, 75, 64, 67, 73])

# 2) Ejecuta la prueba t de 2 muestras independientes
# equal_var=False para varianzas desiguales
res = stats.ttest_ind(hombres, mujeres, equal_var=False)

# 3) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 4) Define el nivel de significancia
alpha = 0.05

# 5) Muestra resultados y decide
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

if p_value < alpha:
    print("Rechazo H0: hay diferencia significativa entre los pesos de hombres y mujeres.")
else:
    print("No rechazo H0: no hay evidencia suficiente de diferencia entre los grupos.")
    
    
    
    
