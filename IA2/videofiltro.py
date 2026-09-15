import cv2

# #crear el video de captura de imagenes
# #primero debemos identificar en que puerto se encuentra nuestra camara
# #en este caso seleccionamos donde esta la camara
cap = cv2.VideoCapture(0)

# #crear un ciclo para capturar los frames
while True:
    #leemos los fotogramas
    ret, frame = cap.read()
    
    # #convertir la imagen en RGB
    imaGRIS = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #en ret se captura si la captura se hace correcta (true), en caso de que n
    print(ret)
    
    # #mostrar los frames
    cv2.imshow("VIDEO CAPTURA RGB", frame)
    cv2.imshow("VIDEO CAPTURA GRIS", imaGRIS)
    
    # #cerramos con lectura del teclado
    # #con tecla esc=27 en codigo ascci
    t = cv2.waitKey(1)
    if t == 27:
        break

# #Liberar la video captura
# #COMO BORARR LA VIDEO CAPTURA
cap.release()
# #Cerramos la ventana
cv2.destroyAllWindows()