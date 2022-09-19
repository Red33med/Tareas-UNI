
# Crear un programa que a partir de un número ingresado diga si el mismo es par o impar.

Numero = int(input("Ingresar un numero entero: "))
if Numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

# Escribir un programa que sume todos los números pares entre 2 y 100.

valorInicial = 2
valorFinal = 100
suma = sum([i for i in range(valorInicial, valorFinal+1) if i % 2 == 0])
print("La suma de los numeros pares es: {}".format(suma))

# Crear un programa que permita ingresar un nombre y una cantidad numérica para que así después el programa escriba este nombre tantas veces como su cantidad ingresada.

Nombre = input("Ingresar nombre: ")
Numero = int(input("Ingresar un valor numerico: "))

print(Nombre*Numero)
