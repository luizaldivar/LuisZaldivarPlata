# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:01:38 2026

@author: zaldi
"""

# -*- coding: utf-8 -*-
"""
Práctica 3: Lectura, recorte y combinación de imágenes
"""

import cv2
import matplotlib.pyplot as plt

# ==========================================
# 1. LEER 2 IMÁGENES A COLOR
# ==========================================
# Reemplaza con las rutas de tus dos imágenes
ruta_img1 = 'gato.jpg'
ruta_img2 = 'nina.jpg'

# Lectura en BGR (estándar OpenCV)
img1_bgr = cv2.imread(ruta_img1)
img2_bgr = cv2.imread(ruta_img2)

# Validar que ambas imágenes existan
if img1_bgr is None or img2_bgr is None:
    raise FileNotFoundError("Verifica que las rutas de 'imagen1.jpg' e 'imagen2.jpg' sean correctas.")

# Conversión a RGB para visualización en Matplotlib
img1_rgb = cv2.cvtColor(img1_bgr, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2_bgr, cv2.COLOR_BGR2RGB)

# ==========================================
# 2. SELECCIÓN DE RECORTES Y COMBINACIÓN
# ==========================================
# Definir dimensiones comunes para los recortes (alto, ancho)
alto_recorte = 250
ancho_recorte = 250

# Validar que las imágenes originales tengan tamaño suficiente
h1, w1 = img1_rgb.shape[:2]
h2, w2 = img2_rgb.shape[:2]

if h1 < alto_recorte or w1 < ancho_recorte or h2 < alto_recorte or w2 < ancho_recorte:
    # Ajuste automático al tamaño mínimo disponible si las imágenes son pequeñas
    alto_recorte = min(h1, h2, alto_recorte)
    ancho_recorte = min(w1, w2, ancho_recorte)

# Coordenadas de inicio para cada recorte (y1:y2, x1:x2)
# Recorte 1: Tomado desde el origen (0, 0)
recorte1 = img1_rgb[0:alto_recorte, 0:ancho_recorte]

# Recorte 2: Tomado desde el centro de la imagen 2
y_ini2 = (h2 - alto_recorte) // 2
x_ini2 = (w2 - ancho_recorte) // 2
recorte2 = img2_rgb[y_ini2:y_ini2 + alto_recorte, x_ini2:x_ini2 + ancho_recorte]

# Combinación / Mezcla lineal ponderada (50% de cada recorte)
# Fórmula: resultado = recorte1 * 0.5 + recorte2 * 0.5 + 0
combinacion = cv2.addWeighted(recorte1, 0.5, recorte2, 0.5, 0)

# ==========================================
# 3. MOSTRAR EN SUBPLOT (1x3)
# ==========================================
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Posición 1: Imagen 1 original
axs[0].imshow(img1_rgb)
axs[0].set_title("1. Imagen Original 1")
axs[0].axis('off')

# Posición 2: Combinación de los recortes
axs[1].imshow(combinacion)
axs[1].set_title(f"2. Combinación ({ancho_recorte}x{alto_recorte})")
axs[1].axis('off')

# Posición 3: Imagen 2 original
axs[2].imshow(img2_rgb)
axs[2].set_title("3. Imagen Original 2")
axs[2].axis('off')

plt.tight_layout()
plt.show()