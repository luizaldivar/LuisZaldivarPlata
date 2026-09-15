# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:28:31 2026

@author: Mayte
"""

import cv2
import os

ruta_haar = r"C:\Users\Mayte\Downloads\haarcascade_frontalface_default.xml"

print("¿Existe el archivo?", os.path.exists(ruta_haar))

faceClassif = cv2.CascadeClassifier(ruta_haar)

print("¿Clasificador vacío?", faceClassif.empty())

if faceClassif.empty():
    print("ERROR: No se pudo cargar el Haar Cascade")
    exit()

cap = cv2.VideoCapture(0)

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

    print("Rostros detectados:", len(faces))

    for (x, y, w, h) in faces:

        face_region = gray[y:y+h, x:x+w]

        _, face_binary = cv2.threshold(
            face_region,
            128,
            255,
            cv2.THRESH_BINARY
        )

        face_binary_bgr = cv2.cvtColor(
            face_binary,
            cv2.COLOR_GRAY2BGR
        )

        frame[y:y+h, x:x+w] = face_binary_bgr

        # Rectángulo para comprobar la detección
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    cv2.imshow("Deteccion de Rostros", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()