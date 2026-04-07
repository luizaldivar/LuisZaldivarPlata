# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 08:23:21 2026

@author: zaldi
"""

#Ejercicio 1:
#En una encuesta realizada en dos ciudades (Ciudad A y Ciudad B), se preguntó a los habitantes cuál era su medio de transporte preferido: automóvil o transporte público.
import numpy as np
from scipy import stats

ciudades = np.array([
    [85,65],
    [50,100]])

#realiza la pruenba de chi cuadrado de independenciaq stats.chi2_contingency devuelve el estadu¿istico chi-cuadrado, el p-value
#los grados de libertad y las frecuencias esperadas


chi2 , p_value, g1, esperados1= stats.chi2_contingency(ciudades, correction= False)

#imprime resultados
print(f"Chi cuadrado = {chi2:.4f}")
print(f"p value = {p_value:.4f}")
print(f"Grados de libertad = {g1}")
print("frecuenciqa esperadas:")
print(esperados1)

alpha = 0.05

if p_value < alpha:
    print("No hay evidencia suficiente de que la ciudad de residencia influya en el medio de transporte")
    
else :
    print("Hay evidencia suficiente que demuestra que la ciudad de residencia influye en el medio de transporte ")



#Ejercicio 2: 
#Un investigador de salud pública quiere saber si el nivel educativo influye en el consumo de tabaco. Encuesta a 200 personas y obtiene:
import numpy as np
from scipy import stats

datos_colesterol = np.array([
    [10, 50],  #dieta vegana
    [30, 40],  # dieta mixta
    [45, 5]   # dieta carnivora
])
 #realiza la pruenba de chi cuadrado de independenciaq stats.chi2_contingency devuelve el estadu¿istico chi-cuadrado, el p-value
 #los grados de libertad y las frecuencias esperadas

chi2, p_value, dof, esperados3 = stats.chi2_contingency(datos_colesterol, correction=False)
 #imprime resultados
print(f"Estadístico Chi-cuadrado: {chi2:.4f}")
print(f"p value = {p_value:.4f}")
print(f"Grados de libertad = {g1}")
print("frecuenciqa esperadas:")
print(esperados3)

alpha = 0.05
if p_value < alpha:
    print("Resultado: Se rechaza la hipótesis nula (H0).")
    print("Conclusión: Existe evidencia suficiente entre el tipo de dieta y el nivel de colesterol.")
else:
    print("Resultado: No se rechaza la hipótesis nula (H0).")
    print("Conclusión: No hay evidencia suficiente de que el tipo de dieta influya en el nivel de colesterol.")
    
#Ejercicio 3:
#Un nutriólogo quiere saber si el tipo de dieta que sigue una persona está relacionado con su nivel de colesterol. Evalúa a 180 pacientes y registra:
import numpy as np
from scipy import stats

datos_salud = np.array([
    [40, 20],  # Sin estudios
    [35, 45],  # Bachillerato
    [15, 45]   # Universidad
])
 #realiza la pruenba de chi cuadrado de independenciaq stats.chi2_contingency devuelve el estadu¿istico chi-cuadrado, el p-value
 #los grados de libertad y las frecuencias esperadas

chi2, p_value, dof, esperados = stats.chi2_contingency(datos_salud, correction=False)
 #imprime resultados
print(f"Estadístico Chi-cuadrado: {chi2:.4f}")
print(f"p value = {p_value:.4f}")
print(f"Grados de libertad = {g1}")
print("frecuenciqa esperadas:")
print(esperados)

alpha = 0.05
if p_value < alpha:
    print("Resultado: Se rechaza la hipótesis nula (H0).")
    print("Conclusión: Existe evidencia suficiente para afirmar que el nivel educativo influye en el hábito de fumar.")
else:
    print("Resultado: No se rechaza la hipótesis nula (H0).")
    print("Conclusión: No hay evidencia suficiente; el nivel educativo y el hábito de fumar parecen ser independientes.")
    
