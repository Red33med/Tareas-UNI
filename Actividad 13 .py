# Imprimir las treinta primeras potencias de 4, es decir, 4 elevado a 1, 4 elevado a 2, etc.
num = 4
for n in range(1, 31):
    elevado = num ** n
    print(num, "**", n, "=", elevado)

# Calcular la suma de los n primeros números enteros utilizando la estructura desde. Se ingresa n por teclado.
suma = 0
n = int(input("Ingrese la cantidad de valores: "))
for i in range(1, n + 1):
    suma = suma + i
print("La suma de los", n, "números es:", suma)

# Diseñar el algoritmo para imprimir la suma de los números impares menores o iguales que n.
suma = 0
n = int(input("Ingrese un valor: "))
for i in range(1, n + 1):
    if (i % 2 != 0 and i <= n):
        suma += i
print("La suma de los números impares menores o iguales que", n, "es:", suma)

# Dados dos números enteros, realizar el algoritmo que calcule su cociente y su resto. No se puede utilizar el operador de división ni de resto.
numero1 = int(input("Ingrese el primer numero entero (dividendo):"))
numero2 = int(input("Ingrese el segundo numero entero (divisor):"))

if (numero2 > 0):
    solucion = divmod(numero1, numero2)
    print(solucion)
else:
    print("Error ingrese valores mayores a 0")


# Buscar y escribir la primera vocal leída del teclado. (Se supone que se leen, uno a uno, caracteres desde el teclado; solo cuando se ha leído una vocal se imprime la misma y termina el programa).

x = input("Ingrese los caracteres: ")
vocal = 0
while (vocal == 0):
    if (x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
        #    print("La primer vocal ingresa es:", x)
        vocal += 1

# Escribir un codigo que permita escribir en una pantalla la frase: ¿Desea continuar? S/N, hasta que la respuesta sea S o N.
while (True):
    x = input("¿Desea continuar? S/N: ")
    if (x == "S"):
        continue
    else:
        break

# Leer sucesivamente números del teclado hasta que aparezca un número comprendido entre 1 y 5.
while (True):
    x = int(input("Ingrese un número: "))
    if (x >= 1 and x <= 5):
        break
    else:
        continue

# Determinar el valor máximo de una serie de 20 números ingresados por teclado.
cantidad = 0
lista = []
while (cantidad < 20):
    x = int(input("Ingresar los valores: "))
    cantidad += 1
    lista.append(x)
print("El valor máximo de la serie de números es:", max(lista))

# Determinar simultanemente los valores máximo y minimo de una lista de 10 números.
cantidad = 0
lista2 = []
while (cantidad < 10):
    x = int(input("Ingresar los valores: "))
    cantidad += 1
    lista2.append(x)
print("El valor máximo de la lista de números es:", max(lista2))
print("El valor mínimo de la lista de números es:", min(lista2))
