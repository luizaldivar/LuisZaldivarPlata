# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:34:26 2026

@author: zaldi
"""

# -*- coding: utf-8 -*-
import cv2
import sys

# Carga del clasificador Haar Cascade integrado
ruta_haar = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceClassif = cv2.CascadeClassifier(ruta_haar)

if faceClassif.empty():
    print("ERROR: No se pudo cargar el Haar Cascade")
    sys.exit()

cap = cv2.VideoCapture(0)

# Modo inicial: 1=Normal, 2=Gris, 3=B/N, 4=Desenfoque
modo = 1

print("--- MENÚ DE EFECTOS PARA EL ROSTRO ---")
print("1: Color original (Normal)")
print("2: Escala de Grises")
print("3: Blanco y Negro (Binario)")
print("4: Desenfoque Gaussiano")
print("Q: Salir del programa")
print("--------------------------------------")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer la cámara")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        # Extraer región del rostro
        face_roi = frame[y:y+h, x:x+w]

        if modo == 1:
            # 1: Normal (mantiene los colores del rostro)
            pass

        elif modo == 2:
            # 2: Escala de grises
            face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
            frame[y:y+h, x:x+w] = cv2.cvtColor(face_gray, cv2.COLOR_GRAY2BGR)

        elif modo == 3:
            # 3: Blanco y negro (binario umbralizado)
            face_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
            _, face_bin = cv2.threshold(face_gray, 128, 255, cv2.THRESH_BINARY)
            frame[y:y+h, x:x+w] = cv2.cvtColor(face_bin, cv2.COLOR_GRAY2BGR)

        elif modo == 4:
            # 4: Desenfoque gaussiano
            face_blur = cv2.GaussianBlur(face_roi, (51, 51), 0)
            frame[y:y+h, x:x+w] = face_blur

        # Cuadro verde delimitador
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Indicador de modo en la esquina superior de la ventana
    nombres_modos = {1: "Normal", 2: "Gris", 3: "Blanco y Negro", 4: "Desenfoque"}
    cv2.putText(
        frame,
        f"Modo actual: {nombres_modos[modo]}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.imshow("Deteccion de Rostros - Menu", frame)

    # Captura de teclas para el menú
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        modo = 1
    elif key == ord('2'):
        modo = 2
    elif key == ord('3'):
        modo = 3
    elif key == ord('4'):
        modo = 4
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()