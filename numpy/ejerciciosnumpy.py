
import numpy as np
import pandas as pd


# Crea un array de 10 números aleatorios enteros entre 0 y 100
matriz10 = np.random.randint(0,100,10)
# Crea un array de 5 números aleatorios decimales entre 0 y 1.
matriz5 = np.random.uniform(0,1,5)

# Crea dos arrays de números aleatorios enteros de longitud 5 y concaténalos.
matrizconcat1 = ([1,2,3,4,]) 
matrizconcat2 = ([3,4,5,6,7])
print(np.concat((matrizconcat1,matrizconcat2)))

# Crea un array de 10 números aleatorios enteros y sepáralo en dos arrays de 5 elementos cada uno.
matrizseparados = np.random.randint(10,size=(10))
print(np.split(matrizseparados,2))

# Crea una matriz de 3x3 con números aleatorios decimales entre 0 y 1
matriz = np.random.rand(3, 3)

# Crea un array de 10 números aleatorios enteros y selecciona 3 elementos al azar.
matriz2 = np.random.randint(0,20,10)
seleccion = np.random.choice(matriz2, size=3, replace=False)
print(seleccion)
# Crea un array de 10 números aleatorios enteros entre 0 y 100 y calcula la media.
aleatorio = np.random.randint(0,100,10)
media = np.mean(aleatorio)
print(f"La media de la matriz{aleatorio} es {media}")
