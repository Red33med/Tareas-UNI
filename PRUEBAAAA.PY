# Objetivo: dividir las diferentes operaciones en funciones.
# Además, añadir:
# Una comprobación que nos diga si el número es par o impar
# Una comprobación que nos diga si el número es primo o no.

# def Multiplos(num):
#     listaM = []
#     for mul in range(1, 6):
#         mimultiplo = num * mul
#         listaM.append(mimultiplo)
#     return listaM


# def Cuadrados(num):
#     micuadrado = num ** 2
#     return micuadrado


# def Cubo(num):
#     return (num ** 3)


# def Valor100(num):
#     return (num * 100)


# def CheckPar(num):
#     return (num % 2 == 0)


# def CheckPrimo(num):
#     for divisor in range(2, num):
#         if (num % divisor == 0):
#             return False
#         else:
#             return True


# miNumero = int(input('Hey! Introduce tu número para que calcule cosas: '))
# # miNumero = int(miNumero)

# print('Sus 5 primeros múltiplos:', Multiplos(miNumero))
# print('Su cuadrado y su cubo:', Cuadrados(miNumero), Cubo(miNumero))
# print('Su valor por 100:', Valor100(miNumero))
# print('¿Es el número Par?:', CheckPar(miNumero))
# print('¿Es el número Primo?', CheckPrimo(miNumero))


# def convertidor_Distancia(Distancia_K):
#     Distancia_M = Distancia_K * 1000
#     return Distancia_M


# def convertidor_Tiempo(Tiempo_Minutos):
#     Tiempo_S = Tiempo_Minutos * 60
#     return Tiempo_S


# def velocidadtotal(Tiempo_S, Distancia_M):
#     velocidad = Distancia_M / Tiempo_S
#     return velocidad


# # Calculo con los valores dados por el ejercicio
# Tiempo_S = convertidor_Tiempo(5)
# Distancia_M = convertidor_Distancia(2)
# print("La velocidad a la que recorre el proyectil es de {0:.3f} en 2 km y 5 minutos".format(
#     velocidadtotal(Tiempo_S, Distancia_M)))

# # Resultado con los valores dados por el usuario
# print("-------Valores dados por el usuario-------")
# x = int(input("Ingrese la distancia que recorre el proyectil: "))
# t = int(input("Ingrese el tiempo del proyectil: "))
# Tiempo_S = convertidor_Tiempo(t)
# Distancia_M = convertidor_Distancia(x)
# print("La velocidad a la que recorre el proyectil es de {0:.3f} en {1:} y {2:}".format(
#     velocidadtotal(Tiempo_S, Distancia_M), Distancia_M, Tiempo_S))

def Multiplicar_5(numero):
    LIMITE = 5
    contador = 1
    while (contador <= LIMITE):
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1


def Multiplicar_10(numero):
    LIMITE = 10
    contador = 6
    while (contador <= LIMITE):
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1


def Multiplicar_15(numero):
    LIMITE = 15
    contador = 11
    while (contador <= LIMITE):
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1


def Multiplicar_20(numero):
    LIMITE = 20
    contador = 16
    while (contador <= LIMITE):
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1


Multiplicar_5(1)
Multiplicar_10(1)
Multiplicar_15(1)
Multiplicar_20(1)
