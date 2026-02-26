# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 07:35:49 2026

@author: zaldi
"""

import pandas as pd
df = pd.read_csv('part1_employees.csv')
#Obtén todas las filas del depto "Eng" que además tengan perf_score >= 0.85, pero muestra solo las columnas:
  #emp_id, name, city, perf_score, salary_mxn.
resultado = df.loc[ (df["dept"] == "Eng") & (df["perf_score"] >= 0.85),  ["emp_id", "name", "city", "salary_mxn"]]

print(resultado)

#Del DataFrame completo, obtén las filas 3 a 8 (incluyendo 3 y excluyendo 8), y solo las columnas 0, 1, 5 y 6
# (por posición).
resp2 = df.iloc[3:8,[0,1,5,6]]
print("las filas son ")
print(resp2)
#Calcula:Filtra empleados que estén en city CDMX o GDL, con warnings == 0 y absences <= 1. 
#Muestra emp_id, name, city, warnings, absences.

resultado2 = df.loc[ (df["city"] == "CDMX") | (df["city"] == "GDL") & (df["warnings"] == 0) & (df["absences"] <=1),  ["emp_id", "name", "city", "warnings", "absences"]]


#Calcula:
#salario promedio (salary_mxn)
#perf promedio (perf_score)
#total de warnings (warnings)

promediosalario = df["salary_mxn"].mean()
print(promediosalario)

perfpromedio = df["perf_score"].mean()
print("El promedio de la puntuacion es ",perfpromedio )
sumarwarnings = df["warnings"].sum()
print("El total de warnings es...", sumarwarnings)
#por cada departamento
#suma número de empleados
#salario promedio
#perf promedio
#total de warnings (warnings)
medidasdetendencia = df.agg({
    "salary_mxn" : "mean",
    "perf_score" : "mean",
    "warnings" : "sum"})

#por cada departamento
#suma número de empleados
#salario promedio
#perf promedio
analisisdept = (
    df.groupby("dept")
    .agg(
        empleados = ("dept","count"),
        salario_promedio = ("salary_mxn", "mean"),
    perf_promedio = ("perf_score", "mean")
    )
    .sort_values("salario_promedio", ascending=False)
    )
analisisdept


