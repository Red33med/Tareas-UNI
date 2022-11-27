import random
# Crea un array o arreglo unidimensional con un tamaño de 10, inserta los valores numéricos que desees de la manera que quieras y muestra por pantalla la media de valores del array.

tamaño = 0
lista = []
while (tamaño < 10):
    usuario = int(input("Ingrese los valores numericos: "))
    tamaño += 1
    lista.append(usuario)
print(lista)
print("La media de los valores de mi lista son:", sum(lista) / len(lista))


# Crea un array o arreglo unidimensional donde tu le indiques el tamaño por teclado, y crear una función que rellene el array o arreglo con los múltiplos de un numero pedido por teclado. Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la función, el array contendrá 3, 6, 9, 12, 15. Muéstralos por pantalla usando otra función distinta.
tamaño = int(input(u"Ingrese el tamaño del arreglo: "))
numero = int(input(u"Ingrese un numero: "))
lista = []


def multiplos(num, tamaño):
    for i in range(1, tamaño + 1):
        lista.append(i * num)


def lectura():
    print(lista)


multiplos(numero, tamaño)
lectura()

# Crea dos arrays o arreglos unidimensionales que tengan el mismo tamaño (lo pedirá por teclado), en uno de ellos almacenaras nombres de personas como cadenas, en el otro array o arreglo ira almacenando la longitud de los nombres, para ello puedes usar la función longitu(cadena) que viene en PSeInt. Muestra por pantalla el nombre y la longitud que tiene. Puedes usar funciones si lo deseas.
nom = []
longitud = []
contador = 0
tamaño = int(input("Ingrese el tamaño de la lista: "))


def longitudNombres(usuario):
    longitud.append(len(usuario))


while (contador < tamaño):
    usuario = input("Ingrese los nombres: ")
    nom.append(usuario)
    longitudNombres(usuario)
    contador += 1


print("Los nombres de la lista son: ", nom)
print("Su respectiva longitud: ", longitud)

# Pedir valores numericos en dos arrays distintos y almacenar el resultado de los valores de cada posición (posición 0 del arreglo 1 + posición 0 del arreglo 2) y mostrar el contenido de los 3 arreglos de esta forma:
# valor pos 0 arreglo 1 + valor pos 0 arreglo 2 = valor pos 0 arreglo 3
# valor pos 1 arreglo 1 + valor pos 1 arreglo 2 = valor pos 1 arreglo 3
lista1 = []
lista2 = []
lista3 = []
contador = 0
indice = -1


def suma(a, b):
    resultado = lista1[a] + lista2[b]
    lista3.append(resultado)


while (contador < 3):
    valores1 = int(input("Ingrese los valores de la lista 1: "))
    lista1.append(valores1)
    valores2 = int(input("Ingrese los valores de la lista 2: "))
    lista2.append(valores2)
    indice += 1
    suma(indice, indice)
    contador += 1


print("La suma de la posición 0 de la lista 1 y 2 es: ",
      lista1[0], "+", lista2[0], "=", lista3[0])
print("La suma de la posición 1 de la lista 1 y 2 es: ",
      lista1[1], "+", lista2[1], "=", lista3[1])
print("La suma de la posición 2 de la lista 1 y 2 es: ",
      lista1[2], "+", lista2[2], "=", lista3[2])


# Buscar un elemento dentro de un arreglo numérico bidimensional que nosotros le pedimos por teclado ingresar por teclado. Indicar las posición donde se encuentra. Si hay más de uno, indicar igualmente la posición.

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


# • Pediremos los IDs (números) de alumnos de dos clases, álgebra y análisis ingresados en dos arreglos unidimensionales de tamaño 10. Queremos mostrar todos los alumnos comunes en las dos asignaturas.
lista_Algebra = []
lista_anilsis = []
Lista_IDs_Similares = []
tamaño = 0

while (tamaño < 10):
    clase_Algebra = int(input("Ingrese los IDs de la clase de algebra: "))
    lista_Algebra.append(clase_Algebra)
    clase_analisis = int(input("Ingrese los IDs de la clase de analisis: "))
    lista_anilsis.append(clase_analisis)
    tamaño += 1
    if (clase_Algebra == clase_analisis):
        Lista_IDs_Similares.append(clase_analisis)

print("Clase de algebra:", lista_Algebra)
print("Clase analisis", lista_anilsis)
print("IDs similares:", Lista_IDs_Similares)

# • El tamaño de un arreglo de números es de 10 y se pedirá los valores numéricos con los que se rellena. Los valores no se pueden repetir. Mostrar el arreglo con los valores al final.
lista = []
contador = 0
while (contador < 10):
    usuario = input("Ingrese los valores de la lista: ")
    checkeo = usuario in lista
    if (checkeo == True):
        print("Error! No puedes ingresar valores repetidos")
        continue
    else:
        lista.append(usuario)
        contador += 1
        continue
print(lista)

# • Suponga un array con 25 números enteros generados aleatoriamente (utilizar función azar()) y mostrados en pantalla, mostrar en pantalla el valor que ocupa el centro del array.

lista = []
contador = 0

while (contador < 25):
    lista.append(random.randrange(0, 26))
    contador += 1

print(lista)
Valor_Medio = len(lista) // 2
print("El valor del centro de la lista es:", lista[Valor_Medio])

# • Suponga un array con 30 notas de 0 a 20, calcule el promedio de las notas de los aprobados (mayores o iguales a 11) y el promedio de las notas de los desaprobados e indique la cantidad de aprobados y desaprobados.
lista = []
lista_Aprobados = []
lista_Desaprobados = []
contador = 0
sumaAA = 0
sumaDD = 0

while (contador < 30):
    nota = random.randrange(0, 21)
    lista.append(nota)
    contador += 1
    if (nota >= 11):
        lista_Aprobados.append(nota)
        sumaAA = sumaAA + nota
    else:
        lista_Desaprobados.append(nota)
        sumaDD = sumaDD + nota


def promedio(a, b):
    resultado = a / len(b)
    return resultado


print("Notas completas de todos los estudiantes:")
print(lista)
print("----Notas de los aprobados, cantidad y su promedio:----")
print("Aprobados:", lista_Aprobados)
print("Promedio:", promedio(sumaAA, lista_Aprobados))
print("Cantidad de aprobados", len(lista_Aprobados))
print("----Notas de los desaprobados, cantidad y su promedio:----")
print("Desaprobados:", lista_Desaprobados)
print("Promedio:", promedio(sumaDD, lista_Desaprobados))
print("Cantidad de desaprobados", len(lista_Desaprobados))

# • Suponga un array que contiene 40 notas de 0 a 20 generados aleatoriamente y mostradas en pantalla, de acuerdo a la nota contenida, indique cuántos estudiantes son:
# • Deficientes 0-5
# • Regulares 6-10
# • Buenos 11-15
# • Excelentes 16-20

lista = []
lista_Regulares = []
lista_Deficientes = []
lista_Buenos = []
lista_Excelentes = []
contador = 0
sumaAA = 0
sumaDD = 0

while (contador < 40):
    nota = random.randrange(0, 21)
    lista.append(nota)
    contador += 1
    if (nota <= 5):
        lista_Deficientes.append(nota)
    elif (nota <= 10):
        lista_Regulares.append(nota)
    elif (nota <= 15):
        lista_Buenos.append(nota)
    elif (nota <= 20):
        lista_Excelentes.append(nota)

print("Notas completas de todos los estudiantes:")
print(lista)
print("Cantidad de Estudiantes defidicientes:")
print(len(lista_Deficientes))
print("Cantidad de Estudiantes Regulares:")
print(len(lista_Regulares))
print("Cantidad de Estudiantes Buenos:")
print(len(lista_Buenos))
print("Cantidad de Estudiantes Excelentes:")
print(len(lista_Excelentes))
