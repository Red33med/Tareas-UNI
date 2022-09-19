import math

# Actividad 4
# 1. Un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

Kilometros_Bicicleta = float(
    input("Ingrese la cantidad de kilometros recorridos: "))
Cantidad_Litros = float(
    input("Ingrese la cantidad de litros de combustible: "))
Consumo_Kilómetro = Cantidad_Litros / Kilometros_Bicicleta

print("El consumo de combustible por kilómetro es de: {0:.2f} litros" .format(
    Consumo_Kilómetro))

# 2. Un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32),
Temperatura_Fahrenheit = float(input("Ingresar temperatura en Fahrenheit: "))

print("El equivalente a grados Celsius es de: ",
      (5/9) * (Temperatura_Fahrenheit - 32))

# 3. Un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
Numero_1 = float(input("Ingresar el primer número: "))
Numero_2 = float(input("Ingresar el segundo número: "))
Numero_3 = float(input("Ingresar el tercer número: "))

print("El promedio de los tres números es de: ",
      (Numero_1 + Numero_2 + Numero_3) / 3)

# 4. Un programa que calcule la longitud y el área de una circunferencia.
radio = float(input("Ingrese el radio de la circunferencia: "))

Longitud_circunferencia = 2 * math.pi * radio
área_Circulo = math.pi * radio**2

print("El área de la circunferencia es: {0:.2f} y la longitud es: {1:.2f}".format(
    área_Circulo, Longitud_circunferencia))

# # 5. Un programa que calcule la velocidad de un proyectil que recorre 2 Km en 5 minutos. Expresar el resultado en metros/segundo. Velocidad = espacio/tiempo.
Distancia = 2
Tiempo = 5
Distancia_Nueva = Distancia * 1000
Tiempo_Nuevo = Tiempo * 60

print("La velocidad del proyectil es de:  {0:.2f} ".format(
    Distancia_Nueva/Tiempo_Nuevo))

# 6. Un programa que calcule el número de horas, minutos y segundos que hay en 3700 segundos.
segundos = 3700
horas = int(segundos / 3600)
minutos = int((segundos-(horas*3600))/60)
seg = int(segundos-(horas*3600 + minutos*60))

print("En 3700 segundos hay {0:d} h {1:d} m {2:d} s".format(
    horas, minutos, seg))
