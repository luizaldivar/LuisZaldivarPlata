# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 07:39:14 2026

@author: zaldi
"""

import pandas as pd
import numpy as np
from numpy import random

#Tipos de arrays
# Tipos de array
array_0 = np.array(5)
print(array_0)

array_1 = np.array([1, 2, 3, 4, 5, 6])
print(array_1)

array_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2)

array_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array_3)

## Index de los arrays
print(array_1[0])
print(array_1[5])

print(array_2[0][1])#fila,columna
print(array_3[1][0][1])#dimension,fila,columna

#shape
print(array_3.shape)
#reshape
print(array_3.reshape)

print(np.concat((array_1,array_1)))  #unir
#split
print(np.split(array_1,3))

#where
print(np.where(array_1 == 3))
#ordenar
arrayN = np.array([10,50,2,0,7,6])
print(np.sort(arrayN))
print(np.sort(arrayN)[::-1])
#random
numero = random.randint(100,200,1)
print(numero)

numero = random.randint(10, size=(5))
