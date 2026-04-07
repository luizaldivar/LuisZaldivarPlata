# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:07:07 2026

@author: zaldi
"""

import numpy as np
from scipy import stats

tabla = np.array([
    [40,20],
    [30,30]])

#realiza la pruenba de chi cuadrado de independenciaq stats.chi2_contingency devuelve el estadu¿istico chi-cuadrado, el p-value
#los grados de libertad y las frecuencias esperadas


chi2 , p_value, g1, esperados= stats.chi2_contingency(tabla, correction= False)

#imprime resultados
print(f"Chi cuadrado = {chi2:.4f}")
print(f"p value = {p_value:.4f}")
print(f"Grados de libertad = {g1}")
print("frecuenciqa esperadas:")
print(esperados)

alpha = 0.05

if p_value < alpha:
    print("No hay eviodencia suficiente para que hacer ejercicio dependa del genero")
    
else :
    print("Hacer ejercicio efectivamente depende del genero ")