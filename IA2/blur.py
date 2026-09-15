# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:47:42 2026

@author: zaldi
"""

# ====================Filtros en imagenes====================
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
img = cv2.imread('gato.jpg', 0)
print("Tamaño:", img.shape)
print("Tipo:", img.dtype)
# lectura de la imageen en escala de gris& "C:\Users\zaldi\AppData\Local\Microsoft\WindowsApps\python3.13.exe" -m pip install matplotlib
img = cv2.imread('nina.jpg', 0)
print("Tamaño:", img.shape)
print("Tipo:", img.dtype)
# filtro media
# copia de imagen entre 0 y 1
A = img.copy() / 255

# guardar el tamano de la imagen
m, n = A.shape
# crear imagen nueva
B = np.zeros((m, n))
i = 2
j = 2

for i in range(m - 1):
    for j in range(n - 1):
        B[i, j] = (A[i - 1, j - 1] + A[i - 1, j] + A[i - 1, j + 1]
                  + A[i, j - 1] + A[i, j] + A[i, j + 1]
                  + A[i + 1, j - 1] + A[i + 1, j] + A[i + 1, j + 1])
        B[i, j] = B[i, j] / 9

cv2.imshow('img', img)
cv2.imshow('filtro media', B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtro pasa altas
# mascara de convolucion para deteccion de bordes
h = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
for i in range(m - 1):
    for j in range(n - 1):
        B[i, j] = (h[0, 0] * A[i - 1, j - 1] + h[0, 1] * A[i - 1, j] + h[0, 2] * A[i - 1, j + 1]
                  + h[1, 0] * A[i, j - 1] + h[1, 1] * A[i, j] + h[1, 2] * A[i, j + 1]
                  + h[2, 0] * A[i + 1, j - 1] + h[2, 1] * A[i + 1, j] + h[2, 2] * A[i + 1, j + 1])
        B[i, j] = abs(B[i, j])

cv2.imshow('img', img)
cv2.imshow('filtro pasa altas', B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtro media con funcion
# lectura de la imageen en escala de gris
img = cv2.imread('nina.jpg')
filtrada = cv2.blur(img, (5, 5))
# mostrar
cv2.imshow("Imagen original", img)
cv2.imshow("Filtro medi", filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==========================tipos de ruido==========================
def sp_noise(image, prob):
    '''
    Agregue ruido de sal y pimienta
    problema: relación de ruido
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

out1 = sp_noise(img, prob=0.02)
cv2.imshow("ruido sal pimienta", out1)
cv2.waitKey(0)
cv2.destroyAllWindows()

def gasuss_noise(image, mean=0, var=0.001):
    '''
    Agregue ruido gaussiano
    significar: significar
    var: varianza
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    return out

out2 = gasuss_noise(img, mean=0, var=0.01)

# Mostrar imagen
titles = ['Original Image', 'Add Salt and Pepper noise', 'Add Gaussian noise']
images = [img, out1, out2]

plt.figure(figsize=(20, 15))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# ====================Filtros de suavizado con comando de cv2====================
# lectura de la imageen en escala de gris
img = cv2.imread('foto.png')

# filtro convolucion
kernel = np.ones((3, 3), np.float32) / 9
# filter2D recibe laimage a filtrar, la profundidad, -1 le da la misma profundidad que la imagen de entard
# matriz de 2d a utilizar
# en este caos se lee la imagen con ruidp
convolucion = cv2.filter2D(out1, -1, kernel)
cv2.imshow('img', out1)
cv2.imshow('convolucion', convolucion)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtro promedio
promedio = cv2.blur(out1, (3, 3))
cv2.imshow('img', out1)
cv2.imshow('promedio', promedio)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtro gaussiano
# Parametros que recibe imagen, tamano del kernel y desviacion estandar
gaussiano = cv2.GaussianBlur(out1, (3, 3), 0)
cv2.imshow('img', out1)
cv2.imshow('gaussiano', gaussiano)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filtro mediana
mediana = cv2.medianBlur(out1, 3)
cv2.imshow('img', out1)
cv2.imshow('mediana', mediana)
cv2.waitKey(0)
cv2.destroyAllWindows()

# deteccion de bordes
# Filtro promedio suaviza la imagen
img = cv2.imread('animales.jpg', 0)

kernel2 = np.array([[-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1]])
# filter2D recibe laimage a filtrar, la profundidad, -1 le da la misma profundidad que la imagen de entard
# matriz de 2d a utilizar
bordes = cv2.filter2D(src=img, ddepth=-1, kernel=kernel2)
cv2.imshow('img', img)
cv2.imshow('bordes', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()