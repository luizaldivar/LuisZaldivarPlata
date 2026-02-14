#EJERCICIO1
n = int(input("Introduce el valor de N: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")
#EJERCICIO2
num = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}")
#EJERCICIO3
tabla_del = int(input("¿De qué número quieres la tabla?: "))
for i in range(1, 11):
    resultado = tabla_del * i
    print(f"{tabla_del} x {i} = {resultado}")
#EJERCICIO4
suma_notas = 0
cantidad = int(input("¿Cuántas notas vas a ingresar?: "))
for i in range(cantidad):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    suma_notas += nota
if cantidad > 0:
    promedio = suma_notas / cantidad
    print(f"El promedio de las notas es: {promedio:.2f}")
#EJERCICIO5
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1
for _ in range(exponente):
    resultado *= base
print(f"Resultado: {resultado}")
#EJERCICIO6
a = int(input("Inicio (A): "))
b = int(input("Fin (B): "))
suma_pares = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"Suma de pares: {suma_pares}")