numeropar = 4
numeropositivo = 20
edadpersona = 17
calificacion = 60

if numeropar % 2 == 0:
	print ("El numero es Par")
else:
	print ("Impar")

if numeropositivo > 0:
    print("es positivo")
elif numeropositivo < 0:
    print("es negativo")
else:
    print("es cero")

if edadpersona > 17:
    print("es mayor de edad")

else :
    print("es menor de edad")

if calificacion >59 :
    print("la persona aprobo la materia")
else:
    print("la persona a reprobado :( ")

clasificacion = ["A", "B", "C", "D", "E", "F"]



if calificacion >= 90:
    print(clasificacion[0]) 
elif calificacion >= 80:
    print(clasificacion[1])
elif calificacion >= 70:
    print(clasificacion[2])
elif calificacion >= 60:
    print(clasificacion[3]) 
elif calificacion >= 50:
    print(clasificacion[4]) 
else:
    print(clasificacion[5]) 
temperatura = 52

if temperatura < 0 :
     print("se trata de un elemto solido")

elif temperatura < 101:
     print("se trata de un elemento liquido")
else:
     print("se trata de un elemento gaseoso")
