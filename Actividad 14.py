# Escribir un programa que sume, reste, multiplique y divida dos números utilizando funciones.
def suma(a, b):
    resultadoS = a + b
    return resultadoS


def division(a, b):
    resultadoD = a/b
    return resultadoD


def resta(a, b):
    resultadoR = a - b
    return resultadoR


def multiplicacion(a, b):
    resultadoM = a * b
    return resultadoM


numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
print("""La multiplicación de {0:} y {1:} da como resultado: {2:}
La división de {0:} y {1:} da como resultado: {3:}
La resta de {0:} y {1:} da como resultado: {4:}
La suma de {0:} y {1:} da como resultado: {5:}""".format(numero1, numero2, multiplicacion(numero1, numero2), division(numero1, numero2), resta(numero1, numero2), suma(numero1, numero2)))

# 2. Utilizando funciones, escribir un programa que calcule la velocidad de un proyectil que recorre 2 Km en 5 minutos. Expresar el resultado en metros/segundo. Modifique el programa para que el usuario pueda dar los dos valores en Km/minutos, y se pueda generar el resultado en metros/segundo.


def convertidor_Distancia(Distancia_K):
    Distancia_M = Distancia_K * 1000
    return Distancia_M


def convertidor_Tiempo(Tiempo_Minutos):
    Tiempo_S = Tiempo_Minutos * 60
    return Tiempo_S


def velocidadtotal(Tiempo_S, Distancia_M):
    velocidad = Distancia_M / Tiempo_S
    return velocidad


# Calculo con los valores dados por el ejercicio
Tiempo_S = convertidor_Tiempo(5)
Distancia_M = convertidor_Distancia(2)
print("La velocidad a la que recorre el proyectil es de {0:.3f} en 2 km y 5 minutos".format(
    velocidadtotal(Tiempo_S, Distancia_M)))

# Resultado con los valores dados por el usuario
print("-------Valores dados por el usuario-------")
x = int(input("Ingrese la distancia que recorre el proyectil: "))
t = int(input("Ingrese el tiempo del proyectil: "))
Tiempo_S = convertidor_Tiempo(t)
Distancia_M = convertidor_Distancia(x)
print("La velocidad a la que recorre el proyectil es de {0:.3f} en {1:} y {2:}".format(
    velocidadtotal(Tiempo_S, Distancia_M), Distancia_M, "metros", Tiempo_S, "segundos"))

# 3. Escribir un programa que utilizando “While” “do While”, “Repeat” y finalmente “For” para que muestre la tablas de multiplicar del 1 al 5 (con While), del 6 al 10 (con do While), del 11 al 15 (con Repeat), y del 16 al 20(con For), de un número ingresado por el usuario. Utilice procedimientos y funciones.


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


num = int(input("Ingres un numero: "))
Multiplicar_5(num)
Multiplicar_10(num)
Multiplicar_15(num)
Multiplicar_20(num)

# Crear un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Programe una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.


def EsMultiplo(a, b):
    if (a % b == 0):
        return a,  "si es multiplo de", b
    elif (b % a == 0):
        return b, "Si es multiplo de", a
    else:
        return "No son multiplos"


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resultado = EsMultiplo(numero1, numero2)
print(resultado)


# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

def TemperaturaMedia(Temperatura_Maxima, Temperatura_Minima):
    resultado = Temperatura_Maxima - Temperatura_Minima / 2
    return resultado


contador = 0
NumeroDias = int(input("Ingrese el numero de días a introducir: "))
while (contador < NumeroDias):
    temperatura_Maxima = float(input("Ingrese la temperatura maxima: "))
    temperatura_Minima = float(input("Ingrese la temperatura minima: "))
    resultado = TemperaturaMedia(temperatura_Maxima, temperatura_Minima)
    print(resultado)
    contador += 1

# El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Se quiere crear un programa principal que al introducir una fecha diga el día juliano que corresponde. Para ello se debe hacer las siguientes subrutinas:
# • LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
# • DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
# • EsBisiesto: Recibe un año y nos dice si es bisiesto.
# • Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.


def LeerFecha():  # parametros
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    return dia, mes, año


def EsBisiesto(año):
    return (año % 4 == 0 and not (año % 100 == 0)) or año % 400 == 0


def DiasDelMes(mes, año):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        if EsBisiesto(año):
            return 29
        else:
            return 28


def Calcular_Dia_Juliano(dia, mes, año):
    diaj = 0
    for mes in range(1, mes):
        diaj = diaj + DiasDelMes(mes, año)
    diaj = diaj + dia
    return diaj


dia, mes, año = LeerFecha()
print("El dia Juliano es:", Calcular_Dia_Juliano(dia, mes, año))


# Se quiere crear un programa que trabaje con fracciones a/b. Para representar una fracción se a utilizar dos enteros: numerador y denominador, dependiendo de lo que quiera hacer el usuario se necesita crear funciones para:
# • Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando lea una fracción debes simplificarla.
# • Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
# • Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
# • Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
# • Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# • Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# • Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# • Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.

def Leer_fraccion():
    a = int(input("Ingrese el primer numero (Numerador): "))
    b = int(input("Ingrese el segundo numero (denominador): "))
    a, b = Simplificar_Fraccion(a, b)
    return a, b


def EscribirFraccion(a, b):
    if (b != 1):
        print(a)
        print("---")
        print(b)
    else:
        print(a)


def MCD(x, y):
    x = abs(x)
    y = abs(y)
    mayor = max(x, y)
    menor = min(x, y)
    resto = (mayor % menor)
    if resto == 0:
        return menor
    else:
        return MCD(menor, resto)


def Simplificar_Fraccion(a, b):
    m = MCD(a, b)
    return a, b


def Sumar_Fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 + n2 * d1
    denominador = d1 * d2
    numerador = Simplificar_Fraccion(numerador, denominador)
    denominador = Simplificar_Fraccion(numerador, denominador)
    return numerador, denominador


def Restar_Fracciones(n1, d1, n2, d2):
    numerador = n1 * d2 - n2 * d1
    denominador = d1 * d2
    numerador = Simplificar_Fraccion(numerador, denominador)
    denominador = Simplificar_Fraccion(numerador, denominador)
    return numerador, denominador


def Multiplicacion_Fracciones(n1, d1, n2, d2):
    numerador = n1 * n2
    denominador = d1 * d2
    numerador = Simplificar_Fraccion(numerador, denominador)
    denominador = Simplificar_Fraccion(numerador, denominador)
    return numerador, denominador


def Dividir_Fracciones(n1, d1, n2, d2):
    numerador = n1 * d2
    denominador = d1 * n2
    numerador = Simplificar_Fraccion(numerador, denominador)
    denominador = Simplificar_Fraccion(numerador, denominador)
    return numerador, denominador


while True:
    print("1.- Sumar dos fracciones")
    print("2.- Restar dos fracciones")
    print("3.- Multiplicar dos fracciones")
    print("4.- Dividir dos fracciones")
    print("5.- Salir")
    opcion = int(input("Elige una opción: "))
    if opcion >= 1 and opcion <= 4:
        print("Fracción 1:")
        n1, d1 = Leer_fraccion()
        print("Fracción 2:")
        n2, d2 = Leer_fraccion()
    if opcion == 1:
        print("Sumar fracciones")
        numerador, denominador = Sumar_Fracciones(n1, d1, n2, d2)
        EscribirFraccion(numerador, denominador)
    if opcion == 2:
        print("Restar fracciones")
        numerador, denominador = Restar_Fracciones(n1, d1, n2, d2)
        EscribirFraccion(numerador, denominador)
    if opcion == 3:
        print("Multiplicar fracciones")
        numerador, denominador = Multiplicacion_Fracciones(n1, d1, n2, d2)
        EscribirFraccion(numerador, denominador)
    if opcion == 4:
        print("Dividir fracciones")
        numerador, denominador = Dividir_Fracciones(n1, d1, n2, d2)
        EscribirFraccion(numerador, denominador)
    if opcion == 5:
        break
    else:
        print("Opción incorrecta")
