
# Resolución ecuación de primer grado
# ax + b = 0
a = int(input("Ingresar primer numero: "))
b = int(input("Ingresar segundo numero: "))
if (a != 0):
    x = -b / a
    print(x)
elif (b != 0):
    print("Solución imposible")
else:
    print("Error matemático")

# Media aritmetica

contador = 1
Suma = 0
Numero = 0

while (Numero >= 0):
    Numero = float(input("Ingresar la cantidad de valores: "))
    try:
        Numero = int(Numero)
        if (Numero >= 0):
            contador += 1
            Suma = Suma + Numero
    except ValueError:
        print("Ingrese un número entero por favor")

MediaAritmetica = Suma / contador
print("La media aritmetica de {0:} numeros es de: {1:}" .format(
    contador, MediaAritmetica))
print(Suma)

# Nomina semanal empleados de una empresa:

nombre = input("Ingrese su nombre: ")
Horas_Trabajadas = float(input("Ingrese las horas trabajadas: "))
Tarifa_Horaria = float(input("Ingrese la tarifa horaria: "))

if (Horas_Trabajadas <= 35):
    Salario_Bruto = Horas_Trabajadas * Tarifa_Horaria
else:
    Salario_Bruto = 35 * Tarifa_Horaria + \
        (Horas_Trabajadas - 35) * 1.5 * Tarifa_Horaria
# Calculo de Impuestos
if (Salario_Bruto <= 2000):
    Impuestos = 0
elif (Salario_Bruto <= 2220):
    Impuestos = (Salario_Bruto - 2000) * 0.20
elif (Salario_Bruto > 2220):
    Impuestos = (Salario_Bruto - 2220) * 0.30 + (220 * 0.20)
# Calculo salario Neto
Salario_neto = Salario_Bruto - Impuestos

print("""Nombre: {0:}
Salario Bruto: {1:}
Impuestos: {2:}
Salario Neto: {3:}""" .format(nombre, Salario_Bruto, Impuestos, Salario_neto))


# Se desea diseñar un algoritmo que escriba los nombres de los dias de la semana en funcion del valor de una variable llamada Dia.

Dias = ["", "Lunes", "Martes", "Miércoles",
        "Jueves", "Viernes", "Sabado", "Domingo"]

while (True):
    NumeroDia = int(input("Ingrese el número de dia: "))
    try:
        Resultado = Dias[NumeroDia]
        if (NumeroDia == 0):
            print("Ese dia no existe")
        else:
            print(Resultado)
    except:
        print("Ese dia no existe")
