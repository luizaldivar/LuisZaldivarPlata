# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 07:52:37 2026

@author: zaldi
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 08:05:45 2023

@author: mayte
"""
#==============tomar una unica foto con camara==============
import cv2
#import os

#crear video
cap=cv2.VideoCapture(0)

#tomar una sola foto
ret, frame=cap.read()

if ret:
    cv2.imwrite("foto.png", frame)
    print("foto tomada correctamente")
else:
    print("Error al acceder a la cámara")

#liberar la camara
cap.release()

fotoTomada=cv2.imread("foto.png")
cv2.imshow("foto tomada", fotoTomada)
