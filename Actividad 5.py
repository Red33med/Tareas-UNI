
# Por teclado se ingresa el valor hora de un empleado. Posteriormente se ingresa el nombre del empleado, la antigüedad y la cantidad de horas
# trabajadas en el mes. Se pide calcular el importe a cobrar teniendo en cuenta que al total que resuelta de multiplicar el valor hora por la
# cantidad de horas trabajadas, hay que sumarle la cantidad de años trabajados multiplicados por $30, y al total de todas esas operaciones
# restarle el 13% en concepto de descuentos. Imprimir el recibo correspondiente con el nombre, la antigüedad, el valor hora, el total a
# cobrar en bruto, el total de descuentos y el valor neto a cobrar

Valor_Hora_Empleado = float(input("Ingrese el valor hora del empleado: "))
Nombre_Empleado = str(input("Ingrese el nombre del Empleado: "))
Antiguedad_Empleado = int(
    input("Ingrese la antiguedad del empleado en años: "))
Horas_al_mes = float(input("Ingrese las horas trabajadas al mes: "))

Cobro1 = Valor_Hora_Empleado * Horas_al_mes + Antiguedad_Empleado * 30
Descuento = Cobro1 * 0.13
Cobro2 = Cobro1 - Descuento

print("""Nombre del empleado: {0:}
Antiguedad: {1:} años
Valor por hora: {2:} $
Total a cobrar en bruto: {3:} $
Todal de descuento: {4:} $
Valor neto a cobrar: {5:} $""" .format(Nombre_Empleado, Antiguedad_Empleado, Valor_Hora_Empleado, Cobro1, Descuento, Cobro2))

# Dados 3 números donde el primero y el último son límites de un intervalo, indicar si el segundo pertenece a dicho intervalo.

Numero_1 = int(input("Ingresar el numero de limite máximo: "))
Numero_2 = int(input("Ingresar el segundo numero: "))
Numero_3 = int(input("Ingresar el numero de limite mínimo: "))

if Numero_1 > Numero_2 > Numero_3:
    print("Si pertenece a dicho intervalo")
else:
    print("No pertenece a dicho intervalo")


# Una empresa que trabaja con vehículos desea calcular las necesidades de combustible (cantidad de combustible necesario para llenar los depósitos de todos sus vehículos) para lo cual nos han facilitado este esquema de cálculo. Se desea crear un programa para que puedan realizar el cálculo de forma automatizada.

Turismo = 32
Todoterreno = 11
Capturismo = 40
Captodot = 65
Necesidad_Combustible = Turismo * Capturismo + Todoterreno * Captodot
print(Necesidad_Combustible)

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal (redondeado) y lo almacene en una variable, y muestre por pantalla la frase:

Peso_Kilogramos = float(input("Ingrese el peso en kilogramos: "))
Estatura_Usuario = float(input("Ingrese su estatura en metros: "))

Indice_Masa_Corporal = round(Peso_Kilogramos/Estatura_Usuario**2)

print("Tu índice de masa corporal es {0:.2f} " .format(Indice_Masa_Corporal))

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

Inversión = float(input("Ingrese la cantidad a invertir: "))
Interes_Anual = float(input("Ingrese el interes anual: "))
Número_Años = int(input("Ingrese el número de años: "))
Capital_Obtenido = Inversión * 1 + Interes_Anual / 100
print("El capital obtenido en la inversión es de: ", Capital_Obtenido)

# Realice una redacción de máximo 300 palabras en las cuales comente el nivel de dificultad de los ejercicios realizados hasta el momento, y qué habilidades y destrezas pudo desarrollar.

# A lo largo de la actividad pude aprender muchas nuevas funciones que acortan operaciones y líneas de código. Se siente muy bien saber que cada día estoy adquiriendo nuevos conocimientos en Python. Cabe recalcar que es un lenguaje muy moldeable que te permite simplificar muchas líneas de código en simples funciones, eso es lo que más me ha sorprendido de este lenguaje. Por último, solo decir que los ejercicios planteados te ayudan a ganar lógica de programación y solo debemos entender cual es la necesidad de cada ejercicio y empaparnos del tema.
