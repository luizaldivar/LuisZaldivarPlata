# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 07:50:27 2026

@author: zaldi
"""

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

# ==========================================
# 1. Funciones de Ruido
# ==========================================
def sp_noise(image, prob=0.05):
    """Agrega ruido de sal y pimienta."""
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i, j] = 0
            elif rdn > thres:
                output[i, j] = 255
            else:
                output[i, j] = image[i, j]
    return output

# ==========================================
# 2. Cargar imagen y obtener dimensiones
# ==========================================
# Se lee la imagen en escala de grises
img = cv2.imread('gato.jpg', 0)

if img is None:
    raise FileNotFoundError("No se encontró la imagen 'gato.jpg'. Asegúrate de que la ruta sea correcta.")

alto, ancho = img.shape
mitad_alto = alto // 2
mitad_ancho = ancho // 2

# ==========================================
# 3. Dividir en 4 cuadrantes y aplicar filtros
# ==========================================

# --- Cuadrante 1 (Superior Izquierdo): Ruido Sal/Pimienta + Filtro Gaussiano (Media de Gauss) ---
c1 = img[0:mitad_alto, 0:mitad_ancho]
c1_ruido = sp_noise(c1, prob=0.03)
cuadrante1 = cv2.GaussianBlur(c1_ruido, (5, 5), 0)

# --- Cuadrante 2 (Superior Derecho): Filtro Blur (Promedio/Media) ---
c2 = img[0:mitad_alto, mitad_ancho:ancho]
cuadrante2 = cv2.blur(c2, (5, 5))

# --- Cuadrante 3 (Inferior Izquierdo): Filtro Pasa Altas (Detección de bordes) ---
c3 = img[mitad_alto:alto, 0:mitad_ancho]
kernel_pasa_altas = np.array([[-1, -1, -1],
                              [-1,  8, -1],
                              [-1, -1, -1]])
cuadrante3 = cv2.filter2D(src=c3, ddepth=-1, kernel=kernel_pasa_altas)

# --- Cuadrante 4 (Inferior Derecho): Ruido Sal/Pimienta + Filtro Gaussiano (Media de Gauss) ---
c4 = img[mitad_alto:alto, mitad_ancho:ancho]
c4_ruido = sp_noise(c4, prob=0.03)
cuadrante4 = cv2.GaussianBlur(c4_ruido, (5, 5), 0)

# ==========================================
# 4. Mostrar en un Subplot (2x2)
# ==========================================
plt.figure(figsize=(10, 8))

# Cuadrante 1
ax1 = plt.subplot(2, 2, 1)
ax1.imshow(cuadrante1, cmap="gray")
ax1.set_title("C1: Sal y Pimienta + Gauss")
ax1.axis('off')

# Cuadrante 2
ax2 = plt.subplot(2, 2, 2)
ax2.imshow(cuadrante2, cmap="gray")
ax2.set_title("C2: Filtro Blur")
ax2.axis('off')

# Cuadrante 3
ax3 = plt.subplot(2, 2, 3)
ax3.imshow(cuadrante3, cmap="gray")
ax3.set_title("C3: Filtro Pasa Altas")
ax3.axis('off')

# Cuadrante 4
ax4 = plt.subplot(2, 2, 4)
ax4.imshow(cuadrante4, cmap="gray")
ax4.set_title("C4: Sal y Pimienta + Gauss")
ax4.axis('off')

plt.tight_layout()
plt.show()