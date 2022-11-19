
# Escribir un programa que determine si un número ingresado es primo o no. (Un número es primo si es divisible únicamente por 1 y por sí mismo)

Numero = int(input("Ingresar un numero entero: "))
contador = 0

for i in range(1, Numero+1):
    if (Numero % i == 0):
        contador += 1
if (contador == 2):
    print("Si es un número primo")
else:
    print("No es un número primo")
