
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import timedelta


Fecha_Hoy = datetime.strptime(
    input("Ingresar la fecha de hoy (d/m/y): "), "%d/%m/%Y")
fecha_nacimiento = datetime.strptime(
    input("Ingrese su fecha de nacimiento (d/m/y): "), "%d/%m/%Y")
edad = relativedelta(Fecha_Hoy, fecha_nacimiento)
Ingresos_Mensuales = float(input("Ingresar sus ingresos mensuales: "))

Ingresos_Anuales = Ingresos_Mensuales * 12

if edad.years < 21 and Ingresos_Anuales < 5000:
    print("""No debe pagar impuestos
    Sus ingresos anuales son: {0:}
    Usted tiene: {1:} años""" .format(Ingresos_Anuales, edad.years))
else:
    print("""Debe pagar impuestos
    Sus ingresos anuales son: {0:}
    Usted tiene: {1:} años""" .format(Ingresos_Anuales, edad.years))


# Objetivo: generar la serie de Fibonacci, imprimiendo el número de elementos
# que el usuario quiera.
# Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... El siguiente número es
# la suma de los dos anteriores
# Cosas a cumplir:
# - Pedir al usuario que introduzca un número de elementos
# - Si el usuario introduce cualquier cosa que no es convertible a int, volver a
# pedirle que introduzca un número.
# - Imprimir los X primeros términos de la serie, siendo X el número introducido por el usuario.
# - El número de elementos tiene que ser mayor que 1.

# Pedir al usuario el número de elementos hasta que sea correcto

# Bucle condicionado
while (True):
    Introducir = input("Ingrese cuantos elementos desea: ")
    try:
        Introducir = int(Introducir)
        if (Introducir >= 2):
            break
        else:
            print("El numero de elementos tiene que ser mayor o igual que 2")
            continue
    except ValueError:
        print("Ingrese un número entero por favor!")

# Fibonacci
nume1 = 0
nume2 = 1
contador = 0

while (contador < Introducir):
    print(nume1)
    # Calcular el siguiente numero:
    numerosiguiente = nume1 + nume2
    # Actualizar los valores para la otra vuelta
    nume1 = nume2
    nume2 = numerosiguiente
    contador += 1