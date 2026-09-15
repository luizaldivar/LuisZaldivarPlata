# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Tomar captura con la cámara
# ==========================================
cap = cv2.VideoCapture(0)

# Tomar la primera foto para RGB
ret1, frame1 = cap.read()

# Tomar la segunda foto para escala de grises
ret2, frame2 = cap.read()

# Liberar la cámara
cap.release()

if not ret1 or not ret2:
    print("Error al acceder a la cámara")
else:
    # Guardar y cargar primera foto
    cv2.imwrite("captura1.png", frame1)
    ima = cv2.imread("captura1.png")
    img_rgb = cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)

    # ==========================================
    # 2. Sacar canales RGB y mostrarlos en subplot
    # ==========================================
    solo_rojo = np.zeros_like(img_rgb)
    solo_verde = np.zeros_like(img_rgb)
    solo_azul = np.zeros_like(img_rgb)

    solo_rojo[:, :, 0] = img_rgb[:, :, 0]
    solo_verde[:, :, 1] = img_rgb[:, :, 1]
    solo_azul[:, :, 2] = img_rgb[:, :, 2]

    fig = plt.figure(figsize=(10, 8))

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img_rgb)
    ax1.set_title("Original (RGB)")
    ax1.axis("off")

    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(solo_rojo)
    ax2.set_title("Canal Rojo")
    ax2.axis("off")

    ax3 = fig.add_subplot(2, 2, 3)
    ax3.imshow(solo_verde)
    ax3.set_title("Canal Verde")
    ax3.axis("off")

    ax4 = fig.add_subplot(2, 2, 4)
    ax4.imshow(solo_azul)
    ax4.set_title("Canal Azul")
    ax4.axis("off")

    plt.tight_layout()
    plt.show()

    # ==========================================
    # 3. Sumas a canales: Rojo (+35), Azul (+40), Verde (+10)
    # ==========================================
    r, g, b = cv2.split(img_rgb)

    r = cv2.add(r, 35)
    g = cv2.add(g, 10)
    b = cv2.add(b, 40)

    # Reconstruir imagen
    img_modificada_rgb = cv2.merge([r, g, b])

    # Guardar y mostrar en subplot
    img_modificada_bgr = cv2.cvtColor(img_modificada_rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite("captura_modificada.png", img_modificada_bgr)

    fig2 = plt.figure(figsize=(10, 5))

    ax_orig = fig2.add_subplot(1, 2, 1)
    ax_orig.imshow(img_rgb)
    ax_orig.set_title("Original")
    ax_orig.axis("off")

    ax_mod = fig2.add_subplot(1, 2, 2)
    ax_mod.imshow(img_modificada_rgb)
    ax_mod.set_title("Modificada (+R, +G, +B)")
    ax_mod.axis("off")

    plt.tight_layout()
    plt.show()

    # ==========================================
    # 4. Segunda foto: Escala de grises, Ruido Gaussiano y Filtro Gaussiano
    # ==========================================
    # Convertir a escala de grises
    img_gris = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Generar y aplicar ruido gaussiano
    ruido_gauss = np.random.normal(0, 25, img_gris.shape)
    img_con_ruido = cv2.add(img_gris, ruido_gauss.astype(np.uint8))

    # Aplicar filtro gaussiano
    img_filtrada = cv2.GaussianBlur(img_con_ruido, (5, 5), 0)

    # Mostrar comparación en subplot
    fig3 = plt.figure(figsize=(12, 4))

    ax_g1 = fig3.add_subplot(1, 3, 1)
    ax_g1.imshow(img_gris, cmap="gray")
    ax_g1.set_title("Gris Original")
    ax_g1.axis("off")

    ax_g2 = fig3.add_subplot(1, 3, 2)
    ax_g2.imshow(img_con_ruido, cmap="gray")
    ax_g2.set_title("Con Ruido Gaussiano")
    ax_g2.axis("off")

    ax_g3 = fig3.add_subplot(1, 3, 3)
    ax_g3.imshow(img_filtrada, cmap="gray")
    ax_g3.set_title("Filtro Gaussiano Aplicado")
    ax_g3.axis("off")

    plt.tight_layout()
    plt.show()