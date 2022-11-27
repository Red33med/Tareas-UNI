# Crea un programa que pida su nombre al usuario y lo escriba al revés (de la última letra a la primera: a partir de "Nacho" escribiría "ohcaN").
nombre = input("Ingrese su nombre: ")
nuevo_nombre = "".join(reversed(nombre))
print(nuevo_nombre)

# • Crea un programa que pida su nombre al usuario y lo escriba alternando letras mayúsculas y minúsculas (por ejemplo, "nAcho" se  mostraría como "NaChO".
usuario = input("Ingrese su nombre: ")
contador = 0

for letra in usuario:
    if (contador % 2 == 0):
        print(letra.upper(), end="")
    else:
        print(letra.lower(), end="")
    contador = contador + 1

# • Crea un programa que pida su nombre al usuario y diga cuántas vocales contiene (por ejemplo, "Aurora" tiene 4 vocales).
nombre = input("Ingrese su nombre: ").lower()
contador = 0

for letra in nombre:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        contador = contador + 1
print("Hay en total de: ", contador, "vocales")

# • Crea un programa que pida su nombre al usuario y diga qué vocales contiene (en orden y sin repetir: por ejemplo, para "Aurora" deberá
# responder "aou").
nombre = input("Ingrese su nombre: ").lower()
lista = []

for letra in nombre:
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        if (letra not in lista):
            lista.append(letra)

print(*lista)

# • Crea un programa que pida una frase al usuario y diga cuántas palabras contiene (pista: puedes contar los espacios, prestando atención en que no estén repetidos).
frase = input("Ingrese la frase: ")
palabras = frase.split()
print("Hay un total de", len(palabras), "palabras")

# • Crea un programa que pida al usuario su nombre y apellidos y los muestre con las mayúsculas y minúsculas correctas (aparecerán en mayúsculas la primera letra y la que haya tras cada espacio; las demás aparecerán en minúsculas. Por ejemplo, si introduce “mArcoS esPInoZa", es escribirá “Marcos Espinoza").
nombre = input("Ingrese su nombre y apellido: ")

x = nombre.title()
print(x)

# • Hacer un código donde se recorre el array mi_tabla usando la variable i como contador, y el resultado de multiplicar a i por 10 se le asigna a mi_tabla[i], después se muestran los datos introducidos en mi_tabla por pantalla, recorriendo el array usando nuevamente la variable i como contador.
mi_tabla = []
tamaño = 10

for i in range(1, tamaño + 1):
    mi_tabla.append(i * 10)

print(mi_tabla)


# • Implementar un programa que evalúe si un número n es divisible entre los numero (2 y 3).
n = int(input("Ingrese un numero: "))

if (n % 2 == 0 and n % 3 == 0):
    print("El numero es divisible para 2 y 3")
else:
    print("El numero no es divisible para 2 y 3")

# • Desarrollar un programa en pseudocódigo que luego de ingresar 2 números naturales por teclado, donde el segundo debe ser mayor que el primero. Luego muestre los números naturales que hay entre ambos empezando de menor a mayor. Debe utilizar los ciclos que sean necesarios para desarrollar el ejercicio.
while (True):
    num1 = int(input("Ingrese el numero menor: "))
    num2 = int(input("Ingrese el numero mayor: "))
    if (num2 > num1):
        for i in range(num1, num2 + 1):
            print(i)
        break
    else:
        print("El segundo valor debe ser mayor que el primero")

# • Calcular según la talla de varias personas introducidas por teclado (n), lo siguiente: • Cuales el promedio de talla • Cual es la talla de la persona mas baja • Cual es la talla de la persona mas alta
tallas = []
tamaño = int(input("Cuantas tallas desea introducir?: "))
contador = 0

while (contador < tamaño):
    usuario = float(input("Ingrese la talla de las personas: "))
    tallas.append(usuario)
    contador += 1

print("El promedio de talla es: ", sum(tallas) / len(tallas))
print("La talla de la persona más baja es:", min(tallas))
print("La talla de la persona más alta es:", max(tallas))
