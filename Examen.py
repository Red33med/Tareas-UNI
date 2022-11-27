import random
# # Ejercicio 1
# def numeroCombinatorio(n, k):
#     Combi = Factorial(n) / (Factorial(n - k) * Factorial(k))
#     return int(Combi)


# def Factorial(Num):
#     for i in range(1, Num):
#         Num = Num * i
#     return Num


# print("¿Cuantos Grupos de 2 elementos se pueden formar con un total de 4 elementos?: ",
#       numeroCombinatorio(4, 2))


# # Ejercicio 2
# def ProgresionAritmetica(NumA, razon):
#     for i in range(0, 4):
#         NumA = NumA * razon
#         if (i == 3):
#             lista.append("....")
#         else:
#             lista.append(NumA)
#     return lista


# Numero = int(input("Termino inicial: "))
# Razon = int(input("Razon de la sucesion: "))
# lista = [Numero]

# ProgresionAritmetica(Numero, Razon)

# print("A continuacion la sucesion: ", lista)


lista = [10, 20, 30, 40, 10, 30, 5]
posiciones = []
posicion = -1

elemento = int(input("Ingresar el elemento que desea buscar: "))
try:
    while (True):
        posicion = lista.index(elemento, posicion + 1)
        posiciones.append(posicion)
except:
    pass
print("Ese valor se encuentra en las posiciones:", posiciones)
