
# Diseñar el código correspondiente a un programa que escribe el porcentaje descontado en una compra, introduciendo por teclado el precio de la tarifa (valor total de la compra) y el precio pagado.

Tarifa = float(input("Ingrese el precio de la Tarifa: "))
Precio_Pagado = float(input("Ingrese el precio pagado: "))
Descuento = Tarifa - Precio_Pagado
Porcentaje_Descontado = Descuento * 100 / Tarifa
print("El porcentaje de descuento es de:", Porcentaje_Descontado)

# Diseñar el código correspondiente a un programa que pida por teclado dos números enteros y muestre su suma, resta, multiplicación, división y el resto (módulo) de la división Si la operación no es conmutativa, también se mostrará el resultado invirtiendo los operadores.

Numero_1 = int(input("Ingrese el primer numero entero: "))
Numero_2 = int(input("Ingrese el segundo numero entero: "))
Suma = Numero_1 + Numero_2
Resta = Numero_1 - Numero_2
Resta_2 = Numero_2 - Numero_1
Multiplicacion = Numero_1 * Numero_2
División = Numero_1 / Numero_2
División2 = Numero_2 / Numero_1
Modulo = Numero_1 % Numero_2
Modulo2 = Numero_2 % Numero_1

print("""Suma: {0:}
Resta: {1:}
Resta Invertida: {2:}
Multiplicación: {3:}
Division: {4:0.2f}
Division invertida: {5:0.2f}
Modulo: {6:}
Modulo invertido: {7:}""" .format(Suma, Resta, Resta_2, Multiplicacion, División, División2, Modulo, Modulo2))

# Diseñar el código correspondiente a un programa que obtiene la última cifra de un número introducido

Numero = int(input("Ingresar un numero: "))
print(Numero % 10)

# Diseñar el código correspondiente a un programa que pida el total de kilómetros recorridos, el precio de la gasolina (por galón), el dinero de gasolina gastado en el viaje y el tiempo que se ha tardado (en horas y minutos) y que calcule:
# • Consumo de gasolina (en galón y dólares) por cada 100 km.
# • Consumo de gasolina (en galón y dólares) por cada km.
# • Velocidad media (en km/h y m/s).


Kilometros_Recorridos = float(
    input("Ingrese total de kilometros recorridos: "))
Precio_Gasolina = float(input("Ingrese precio de la gasolina por galón: "))
Dinero_Gastado = float(
    input("Ingrese dinero gastado de gasolina en el viaje: "))
Tiempo_de_Viaje = float(input("Ingrese el tiempo que se tomó en horas: "))
Tiempo_de_Viaje2 = float(input("Ingrese el tiempo que se tomó en minutos: "))

Consumo_Gasolina_por_KilometroenDolares = Dinero_Gastado / Kilometros_Recorridos
Consumo_Gasolina_por_Kilometroen_Galon = Consumo_Gasolina_por_KilometroenDolares * Precio_Gasolina
Consumo_Gasolina_100Dolares = Consumo_Gasolina_por_KilometroenDolares * 100
Consumo_Gasolina_100Galones = Consumo_Gasolina_por_Kilometroen_Galon * 100

Minutos_a_Horas = float(Tiempo_de_Viaje2 / 60)
TiempoTotalenhoras = Tiempo_de_Viaje + Minutos_a_Horas

Velocidad_Media_Kilometros = Kilometros_Recorridos / (TiempoTotalenhoras)

TiempoTotalSegundos = TiempoTotalenhoras * 3600

Velocidad_Media_Metros = Kilometros_Recorridos * 1000 / TiempoTotalSegundos

print("""El consumo de gasolina en galones por cada 100 km es: {0:.2f}
El consumo de gasolina en dolares por cada 100 km es: {1:.2f} 
El consumo de gasolina en galones por cada kilometro es: {2:.2f}
El consumo de gasolina en dolares por cada kilometro es: {3:.2f}
La Velocidad media en Km/h es: {4:.2f}
La velocidad media en M/s es: {5:.2f}""" .format(Consumo_Gasolina_100Galones, Consumo_Gasolina_100Dolares, Consumo_Gasolina_por_Kilometroen_Galon, Consumo_Gasolina_por_KilometroenDolares, Velocidad_Media_Kilometros, Velocidad_Media_Metros))
