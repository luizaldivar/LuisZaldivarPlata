# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 07:57:34 2026

@author: zaldi
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def listar_imagenes(directorio):
    """Lista todas las imagenes compatibles dentro del directorio."""
    extensiones_validas = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    return [os.path.join(directorio, f) for f in os.listdir(directorio) 
            if f.lower().endswith(extensiones_validas)]

def separar_canales_rgb(img_bgr):
    """Muestra la imagen original y sus tres canales R, G y B por separado."""
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img_rgb)
    
    # Crear matrices para visualizar cada canal con su respectivo color
    zeros = np.zeros_like(r)
    solo_r = cv2.merge([r, zeros, zeros])
    solo_g = cv2.merge([zeros, g, zeros])
    solo_b = cv2.merge([zeros, zeros, b])

    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    axs[0].imshow(img_rgb)
    axs[0].set_title("Original (RGB)")
    axs[1].imshow(solo_r)
    axs[1].set_title("Canal Rojo (R)")
    axs[2].imshow(solo_g)
    axs[2].set_title("Canal Verde (G)")
    axs[3].imshow(solo_b)
    axs[3].set_title("Canal Azul (B)")
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def rgb_a_escala_de_grises(img_bgr):
    """Convierte la imagen a escala de grises y compara con la original."""
    gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img_rgb)
    axs[0].set_title("Original")
    axs[1].imshow(gris, cmap='gray')
    axs[1].set_title("Escala de Grises")
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def aislar_objeto_por_clic(img_bgr):
    """
    Permite dar clic sobre un objeto para conservar su color y volver gris el fondo.
    Incluye impresion de depuracion y umbrales tolerantes para asegurar la mascara.
    """
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    color_clic = []

    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            color_clic.append(hsv[y, x])
            print(f"\n[INFO] Pixel seleccionado en (X={x}, Y={y}) -> HSV: {hsv[y, x]}")
            cv2.destroyAllWindows()

    nombre_ventana = "Haz CLIC en el objeto de color y presiona ENTER"
    cv2.namedWindow(nombre_ventana, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(nombre_ventana, img_bgr)
    cv2.setMouseCallback(nombre_ventana, on_mouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if not color_clic:
        print("[AVISO] No se detecto seleccion con el raton.")
        return

    h, s, v = int(color_clic[0][0]), int(color_clic[0][1]), int(color_clic[0][2])
    
    # Tolerancias calibradas para capturar tonos completos (como el amarillo del pez)
    tolerancia_h = 18
    umbral_inf = np.array([max(0, h - tolerancia_h), max(30, s - 80), max(30, v - 80)], dtype=np.uint8)
    umbral_sup = np.array([min(179, h + tolerancia_h), 255, 255], dtype=np.uint8)

    # Generacion de la mascara binaria
    mascara = cv2.inRange(hsv, umbral_inf, umbral_sup)
    
    # Limpieza morfologica: rellenar huecos internos y quitar ruido
    kernel = np.ones((5, 5), np.uint8)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

    # Preparar el fondo en gris con 3 canales
    gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    fondo_gris = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)

    # Fusionar: color donde la mascara sea 255, gris donde sea 0
    resultado_bgr = np.where(mascara[:, :, None] == 255, img_bgr, fondo_gris)

    # Conversion a RGB para Matplotlib
    resultado_rgb = cv2.cvtColor(resultado_bgr, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # Mostrar comparativa
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(img_rgb)
    axs[0].set_title("Original")
    axs[1].imshow(mascara, cmap='gray')
    axs[1].set_title("Mascara del Objeto")
    axs[2].imshow(resultado_rgb)
    axs[2].set_title("Objeto a color, resto gris")
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def menu_principal():
    ruta_carpeta = input("Ingresa la ruta de la carpeta con imagenes: ").strip('"').strip("'")
    
    if not os.path.exists(ruta_carpeta):
        print("La ruta especificada no existe.")
        return

    imagenes = listar_imagenes(ruta_carpeta)
    if not imagenes:
        print("No se encontraron imagenes compatibles en la carpeta.")
        return

    print("\n--- IMAGENES ENCONTRADAS ---")
    for idx, path in enumerate(imagenes):
        print(f"[{idx}] {os.path.basename(path)}")

    eleccion = int(input("\nSelecciona el indice de la imagen a procesar: "))
    img_path = imagenes[eleccion]
    img_bgr = cv2.imread(img_path)

    while True:
        print("\n--- MENU DE ACCIONES ---")
        print("1. Descomponer en canales RGB")
        print("2. Convertir imagen a escala de grises")
        print("3. Resaltar objeto por color (resto a escala de grises)")
        print("4. Cambiar de imagen")
        print("5. Salir")
        
        opcion = input("Elige una opcion (1-5): ")

        if opcion == '1':
            separar_canales_rgb(img_bgr)
        elif opcion == '2':
            rgb_a_escala_de_grises(img_bgr)
        elif opcion == '3':
            aislar_objeto_por_clic(img_bgr)
        elif opcion == '4':
            for idx, path in enumerate(imagenes):
                print(f"[{idx}] {os.path.basename(path)}")
            eleccion = int(input("Selecciona nuevo indice: "))
            img_path = imagenes[eleccion]
            img_bgr = cv2.imread(img_path)
        elif opcion == '5':
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu_principal()