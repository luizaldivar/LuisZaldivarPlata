# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 07:50:53 2026

@author: zaldi
"""
#umbralizacion
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen
img = cv2.imread("jack.jpg")

# Convertir a gris
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

matriz = np.ones(gris.shape, dtype='uint8') * 50

# ======== IMAGEN BRILLANTE ========
# Aumentar el brillo
brillanteGray = cv2.add(gris, matriz)

# Usando threshold
# Valor de umbralizacion 160, valor maximo 255, tipo de umbralizacion
# treshol_binary

_, imgthres1 = cv2.threshold(brillanteGray, 160, 255, cv2.THRESH_BINARY)
_, imgthres2 = cv2.threshold(brillanteGray, 160, 255, cv2.THRESH_BINARY_INV)

# USANDO EL ADAPTATIVO
imaadaptative = cv2.adaptiveThreshold(brillanteGray, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# ======== IMAGEN OSCURA ========
oscuraGray = cv2.subtract(gris, matriz)

_, imgthres3 = cv2.threshold(oscuraGray, 50, 255, cv2.THRESH_BINARY)
_, imgthres4 = cv2.threshold(oscuraGray, 50, 255, cv2.THRESH_BINARY_INV)

# USANDO EL ADAPTATIVO
imaadaptative2 = cv2.adaptiveThreshold(oscuraGray, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Mostrar las imagenes
fig = plt.figure()
ax1 = fig.add_subplot(2, 4, 1)
ax1.imshow(brillanteGray, cmap="gray")
ax1.set_title("Brillante")

ax2 = fig.add_subplot(2, 4, 2)
ax2.imshow(imgthres1, cmap="gray")
ax2.set_title("Brillante THRESH 1")

ax3 = fig.add_subplot(2, 4, 3)
ax3.imshow(imgthres2, cmap="gray")
ax3.set_title("Brillante THRESH 2")

ax4 = fig.add_subplot(2, 4, 4)
ax4.imshow(imaadaptative, cmap="gray")
ax4.set_title("Brillante ADAPTATIVA")

ax5 = fig.add_subplot(2, 4, 5)
ax5.imshow(oscuraGray, cmap="gray")
ax5.set_title("Oscura")

ax6 = fig.add_subplot(2, 4, 6)
ax6.imshow(imgthres3, cmap="gray")
ax6.set_title("Oscura Thresh 1")

ax7 = fig.add_subplot(2, 4, 7)
ax7.imshow(imgthres4, cmap="gray")
ax7.set_title("Oscura Thresh 2")

ax8 = fig.add_subplot(2, 4, 8)
ax8.imshow(imaadaptative2, cmap="gray")
ax8.set_title("Oscura Thresh Adapattiva")

plt.show()