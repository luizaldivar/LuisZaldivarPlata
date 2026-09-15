#==================Captura de video en tiempo real==================
import cv2

# #crear el video de captura de imagenes
# #primero debemos identificar en que puerto se encuentra nuestra camara
# #en este caso seleccionamos donde esta la camara
cap = cv2.VideoCapture(0)

# #crear un ciclo para capturar los frames
while True:
    #leemos los fotogramas
    ret, frame = cap.read()
    
    #en ret se captura si la captura se hace correcta (true), en caso de que n
    print(ret)
    
    #mostrar los frames
    cv2.imshow("VIDEO CAPTURE", frame)
    
    #cerramos con lectura del teclado
    #con tecla esc=27 en codigo ascci
    t = cv2.waitKey(1)
    if t == 27:
        break

# Liberar la cámara y cerrar ventanas al salir del ciclo
cap.release()
cv2.destroyAllWindows()