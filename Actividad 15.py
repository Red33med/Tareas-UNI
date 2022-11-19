
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


while (True):
    valores1 = input("Ingrese los valores de la lista 1: ")
    lista1.append(valores1)
    valores2 = input("Ingrese los valores de la lista 2: ")
    lista2.append(valores2)
    respuesta = input("Desea continuar (S/N): ")
    if (respuesta == "S"):
        continue
    else:
        break

print("valor pos 0 arreglo 1 + valor pos 0 arreglo 2 = valor pos 0 arreglo 3 valor pos 1 arreglo 1 + valor pos 1 arreglo 2 = valor pos 1 arreglo 3")


def suma(a, b):
    resultado = lista1[a] + lista2[b]
    lista3.append(resultado)
