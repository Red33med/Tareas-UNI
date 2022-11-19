

# Que imprima los números del 100 al 0, en orden decreciente.
Números = 100

while (Números > -1):
    print(Números)
    Números = Números - 1

# Que imprima los números pares entre 0 y 100.
numero_inicial = 0
while numero_inicial <= 100:
    if numero_inicial % 2 == 0:
        print(numero_inicial)
    numero_inicial = numero_inicial + 1


# Que imprima los números impares hasta el 100 y que imprima cuantos impares hay.
numero = 0

while numero <= 100:
    if numero % 2 != 0:
        print(numero)
    numero = numero + 1

# Que imprima todos los números naturales que hay desde la unidad hasta un número que introducimos por teclado.
Numero = int(input("Ingrese un número mayor a 1: "))
Unidad = 1

while (Numero < 1):
    Numero = int(input("El número ingresado debe ser mayor a 1: "))

while (Unidad <= Numero):
    print(Unidad)
    Unidad = Unidad + 1

# RETO: Introducir tantas frases como queramos y contarlas.
x = 1
contador = 0
while (True):
    if (x > 1):
        break
    else:
        input("Ingrese una frase: ")
        contador = contador + 1
        print("Si desea acabar las frases digite 2, si desea continuar digite 1")
        x = int(input("Respuesta: "))

print("El numero de frases es:", contador)

# Introducir un número por teclado. Que nos diga si es positivo o negativo.
valor = int(input("Ingresar un numero negativo o positivo: "))
while (True):
    if (valor >= 0):
        print("Es un valor positivo")
        break
    else:
        print("Es un valor negativo")
        break

# Introducir un número por teclado. Que nos diga si es par o impar.
numero = int(input("Ingresar un numero entero: "))
while (True):
    if (numero % 2 == 0):
        print("Es un valor par")
        break
    else:
        print("Es un valor impar")
        break

# Imprimir y contar los múltiplos de 3 desde la unidad hasta un número que introducimos por teclado.
numero = int(input("Ingrese un número mayor a 0: "))
Unidad = 1
c = 0
while (Unidad <= numero):
    if (Unidad % 3 == 0):
        print(Unidad)
        c = c + 1
    Unidad = Unidad + 1
print("Hay", c, "número múltiplos de 3.")

# Que imprima los números del 1 al 100. Que calcule la suma de todos los números pares, por un lado, y por otro, la de todos los impares.
numero = 1
par = 0
impar = 0

while numero <= 100:
    print(numero)
    if numero % 2 == 0:
        par = par + numero
    if numero % 2 != 0:
        impar = impar + numero
    numero = numero + 1
print("La suma de todos los número pares entre 1 y 100 es igual a:", par)
print("La suma de todos los número impares entre 1 y 100 es igual a:", impar)

# RETO: Imprimir y contar los números que son múltiplos de 2 o de 3 que hay entre 1 y 100.
numero = 1
contador2 = 0
contador3 = 0

while numero <= 100:
    print(numero)
    if numero % 2 == 0:
        contador2 += 1
    if numero % 3 == 0:
        contador3 += 1
    numero = numero + 1
print("Existen", contador3, "multiplos de 3")
print("Existen", contador2, "multiplos de 2")

# Que imprima el mayor y el menor de una serie de cinco números que vamos introduciendo por teclado.
lista = []
Contador = 1
mayor = 0
menor = 0
i = 1
while (Contador <= 5):
    Numero = input("Ingrese el numero #" + str(i) + " ")
    Contador += 1
    lista.append(Numero)
    i += 1
mayor = max(lista)
menor = min(lista)

print(lista)
print("El numero menor es", menor)
print("El numero mayor es", mayor)

# Introducir dos números por teclado. Imprimir los números naturales que hay entre ambos números empezando por el más pequeño, contar cuantos hay y cuantos de ellos son pares. Calcular la suma de los impares.
Inicio = int(input("Ingrese el digito inicial: "))
Fin = int(input("Ingrese el digito final: "))
contador = 0
contadorPar = 1
suma = 0

while (Inicio <= Fin + 1):
    print(Inicio)
    Inicio += 1
    if (Inicio % 2 == 0):
        contadorPar += 1
    else:
        suma = Inicio + suma
    contador = contador + 1

print("Hay", contador, "numeros")
print("Existen", contadorPar, "pares")
print("La suma de los numeros impares es:", suma)
