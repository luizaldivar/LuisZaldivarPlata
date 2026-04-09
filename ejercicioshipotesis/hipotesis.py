# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 08:11:03 2026

@author: zaldi
"""
#Ejercicio 1: x
#Una empresa de tecnología afirma que el tiempo promedio que sus empleados tardan en resolver un ticket
 #de soporte es de 45 minutos. Para verificar esta afirmación, se toma una muestra aleatoria de 25 empleados y 
#se mide el tiempo (en minutos) que cada uno tarda en resolver un ticket. ¿El tiempo promedio de resolución de la 
#muestra es significativamente diferente de 45 minutos?
import numpy as np
from scipy import stats

# 1) Datos: calificaciones registradas de los estudiantes
ml = np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])
# 2) Valor hipotético de la media bajo H0
mu0 = 500

# 3) Ejecuta la prueba t de 1 muestra
# sintaxis para ttest_1samp: ttest_1samp(a, popmean) donde a es la muestra y 
# popmean es el valor bajo H0
res = stats.ttest_1samp(ml, mu0)

# 4) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 5) Define el nivel de significancia (alpha)
alpha = 0.05

# 6) Decide si rechazas H0
print("t =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Rechazo H0: hay evidencia de que la media es distinta de 500ML.")
else:
    print("No rechazo H0: no hay evidencia suficiente para decir que la media difiere de 500ML.")
    


#EJERCICIO 2
#Un investigador educativo quiere saber si existe diferencia en las calificaciones finales 
#entre estudiantes que estudian con música y estudiantes que estudian en silencio.

#Selecciona dos grupos completamente distintos y registra sus calificaciones:
import numpy as np
from scipy import stats
GrupoMusica = np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
GrupoSilenci= np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])

 
# 2) Ejecuta la prueba t de 2 muestras independientes
# equal_var=False para varianzas desiguales
res = stats.ttest_ind(GrupoMusica, GrupoSilenci, equal_var=False)

# 3) Extrae el estadístico t y el p-value
t_stat = res.statistic
p_value = res.pvalue

# 4) Define el nivel de significancia
alpha = 0.01

# 5) Muestra resultados y decide
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

if p_value < alpha:
    print("Rechazo H0: hay evidencia suficiente de que los estudiantes que estudian con musica tienen mejor calificacion.")
else:
    print("No rechazo H0: no hay evidencia suficiente para afirmar que los chicos que estudian con musica tienen mejores calificaciones.")
    
#EJERCICIO 3
#Una universidad registra históricamente que sus estudiantes se distribuyen por carrera de la siguiente manera:

#Ingeniería: 40%
#Administración: 35%
#Psicología: 25%
#Este año se inscribieron 400 estudiantes nuevos y se observó la siguiente distribución: [200, 120, 80] (Ingeniería, Administración, Psicología)
    
import numpy as np
from scipy import stats

# 1) Frecuencias observadas (encuesta nueva)
observadas = np.array([200, 120, 80])

# 2) Proporciones históricas esperadas
p = np.array([0.40, 0.35, 0.25])

# 3) Total de personas encuestadas
n = 400

# 4) Frecuencias esperadas
esperadas = n * p

# 5) Cálculo del estadístico chi-cuadrado
res = stats.chisquare(f_obs=observadas, f_exp=esperadas)

# 6) Extraer resultados
chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1

# 7) Mostrar resultados
print(f"Frecuencias Observadas: {observadas}")
print(f"Frecuencias Esperadas: {esperadas}")
print(f"Chi-cuadrado: {chi2:.4f}")
print(f"Grados de libertad: {gl}")
print(f"Valor p: {p_value:.4f}")

# 8) Interpretación
alpha = 0.05
if p_value < alpha:
    print("Se rechaza la hipótesis nula, la distribucion actual es diferente")
else:
    print("No se rechaza la hipótesis nula,no hay evidencia de que la distribucion haya cambiado")   