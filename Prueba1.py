from ast import If
from socket import if_indextoname

# Desarrolle un algoritmo que permita leer dos valores distintos, determinar cual de los dos valores es el mayor y escribirlo.
# Introducir Dos valores distintos
A = 1
B = 3

if A == B:
    print("Introdusca dos valores distintos")
if A < B:
    print("A es menor que B")
if B < A:
    print("B es menor que A")


# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales. ??????????
a = 40
b = 6
c = 300

if a == b == c:
    print("Valores no correctos, debe introducir valores distintos")
if (a > b and a > c):
    print("A es el mayor")
elif (a < b and a < c):
    print("A es el menor")
if (c < b and c < a):
    print("C es el menor")
if (b < a and b < c):
    print("B es el menor")
if (b > a and b > c):
    print("B es el mayor")
else:
    print("C es el mayor")
