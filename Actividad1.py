from ast import If
import msvcrt

print("Del ejercicio 2: ¿Es este algoritmo la solución perfecta al ejercicio anterior? Razone su respuesta.??????????????")
print("Si y no, porque no está escrito en el algoritmo la posibilidad de que los valores ingresados en las variables sean iguales.")

print("Del ejercicio 2: De ser necesario ¿qué cambios deberá realizar? Indíquelos.??????????????")
print("Solo implementaría un cambio, la condición de que si los tres valores son iguales aparezca un mensaje de error o que diga que debemos introducir otros valores.")

# Realizar un algoritmo que permita leer dos valores, determinar cuál de los dos valores es el menor y escríbalo. ??????????????
print("Realizar un algoritmo que permita leer dos valores, determinar cuál de los dos valores es el menor y escríbalo.")
A = float(input("Número A: "))
B = float(input("Número B: "))
if A == B:
    print("Introdusca dos valores distintos")
elif A < B:
    print("A es menor que B")
else:
    print("B es menor que A")

# Realizar un algoritmo que sume dos números.????????????????
print("Realizar un algoritmo que sume dos números.")
x = int(input("Número uno: "))
y = int(input("Número dos: "))
print("La suma es: ", x + y)

# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B, y C respectivamente. El algoritmo debe indicar cual es el menor. Asumiendo que los tres valores introducidos por el teclado son valores distintos. ??????????????????
print("Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B, y C respectivamente. El algoritmo debe indicar cual es el menor. Asumiendo que los tres valores introducidos por el teclado son valores distintos.")
a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Valor C: "))

if a == b == c:
    print("Valores no correctos, debe introducir valores distintos")
if a < b and a < c:
    print("A es el menor")
elif b < a and b < c:
    print("B es el menor")
elif c < a and c < b:
    print("C es el menor")


# Desarrolle un algoritmo que lea cuatro números diferentes y a continuación imprima el mayor de los cuatro números introducidos y también el menor de ellos. ??????????
print("Desarrolle un algoritmo que lea cuatro números diferentes y a continuación imprima el mayor de los cuatro números introducidos y también el menor de ellos.")
a = int(input("Número A: "))
b = int(input("Número B: "))
c = int(input("Número C: "))
d = int(input("Número D: "))

if a == b == c == d:
    print("Valores no correctos, debe introducir valores distintos")
if d > a and d > b and d > c:
    print("D es el mayor")
elif d < a and d < b and d < c:
    print("D es el menor")
if a > b and a > c and a > d:
    print("A es el mayor")
elif a < b and a < c and a < d:
    print("A es el menor")
if c > a and c > b and c > d:
    print("C es el mayor")
elif c < b and c < a and c < d:
    print("C es el menor")
if b > a and b > c and b > d:
    print("B es el mayor")
elif b < a and b < c and b < d:
    print("B es el menor")


msvcrt.getch()
