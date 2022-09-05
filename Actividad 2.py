import math
from locale import locale_encoding_alias
import msvcrt

print("LAS PREGUNTAS DE RESPUESTA A MANO LAS COMENTE EN EL CODIGO COMO COMENTARIOS, POR SI EJECUTA EL ARCHIVO PYTHON (SI DESEA SE LO PUEDO ENVIAR EN WORD")
# A:    Crear en Python lo siguiente:
# 1. Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos. ???
print("Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos")
cateto1 = float(input("Primer cateto: "))
cateto2 = float(input("Segundo cateto: "))
hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
print("La hipotenusa del triángulo rectángulo es: ", hipotenusa)

# 2. Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y altura (H). ???
print("Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y altura (H).")
radio = float(input("Radio: "))
altura = float(input("Altura: "))
área = (2*math.pi*radio*altura + 2*math.pi*radio**2)
volumen = (math.pi*radio**2*altura)
print("El área del cilindro es: ", área)
print("El volumen del cilindro es: ", volumen)

# 3. Desarrollar un algoritmo que calcule el área de un cuadrado.???
print("Desarrollar un algoritmo que calcule el área de un cuadrado.")
longitud_cuadrado = float(input("Longitud: "))
área_cuadrado = (longitud_cuadrado**2)
print("El área del cuadrado es: ", área_cuadrado)

# 4. Realiza un algoritmo que le permita determinar el área de un rectángulo. ??
print("Realiza un algoritmo que le permita determinar el área de un rectángulo.")
base_rectángulo = float(input("Base: "))
altura_rectángulo = float(input("Altura: "))
área_rectángulo = (base_rectángulo * altura_rectángulo)
print("El área de un rectángulo es: ", área_rectángulo)


# B.	Desarrolle en Python lo siguiente:
# 1. Dados el radio y altura de un cilindro calcule el área total y el volumen.??????????
print("Dados el radio y altura de un cilindro calcule el área total y el volumen.")
radio = float(input("Radio: "))
altura = float(input("Altura: "))
área = (2*math.pi*radio*altura + 2*math.pi*radio**2)
volumen = (math.pi*radio**2*altura)
print("El área del cilindro es: ", área)
print("El volumen del cilindro es: ", volumen)

# 2. Se tiene un recipiente cilíndrico con capacidad en litros (volumen). Su altura es un dato en metros. Determine el diámetro de la base.??????????????????
print("Se tiene un recipiente cilíndrico con capacidad en litros (volumen). Su altura es un dato en metros. Determine el diámetro de la base.")
cilindro_Capacidad_Litros = float(input("La capacidad en litros es de: "))
altura_Cilindro_Metros = float(input("La altura del cilindro en metros: "))
# Convertir la capacidad en litros a metros cúbicos.
un_litro = 0.001  # metros cúbicos
capacidad_Metros_Cúbicos = cilindro_Capacidad_Litros * un_litro
print("La capacidad en metros cúbicos es de: ", capacidad_Metros_Cúbicos)
# Formula del Volumen
# volumen_Cilindro = (math.pi*radio**2*altura_Cilindro_Metros) solo para entendimiento///
# Despejaremos el radio de la ecuación del volumen_cilindro
radio_Cilindro = math.sqrt(
    capacidad_Metros_Cúbicos / (math.pi*altura_Cilindro_Metros))
print("El radio de un cilindro es: ", radio_Cilindro)
# Ahora con el valor del radio_Cilindro podemos encontrar el diámetro.
radio_Cilindro = float(
    input("Ingrese el valor del radio del cilindro (use dos decimales): "))
diámetro_Cilindro = (2*radio_Cilindro)
print("El diámetro de la base del cilindro es: ", diámetro_Cilindro)


# 3. Dadas las tres dimensiones de un bloque rectangular calcule y muestre su área total y su volumen.?????????????
print("Dadas las tres dimensiones de un bloque rectangular calcule y muestre su área total y su volumen.")
# Definimos Variables
altura_Prisma = float(input("Ingrese la altura del prisma: "))
lado_A = float(input("Ingrese el lado A del prisma: "))
lado_B = float(input("Ingrese el lado B del prisma: "))
# Fórmula del área total de un prisma
área_Total_Prisma = 2*((lado_A * lado_B) + (lado_A *
                       altura_Prisma) + (lado_B * altura_Prisma))
print("El área total del prisma es de: ", área_Total_Prisma)

# 4. Explique en máximo 200 palabras qué realiza la siguiente codificación?????????????????????
print("Explique en máximo 200 palabras qué realiza la siguiente codificación")
print("x = Mate")
print("y = mática ")
print("Z = x + y")
print("Z")
print("Matemática")

print("Z = La  + Z")
print("Z")
print("La Matemática")

print("r = e in Z")
print("r")
print("True")

print("En este algoritmo se realiza una suma de la variable X y Y, lo que ocasiona que se sumen sus valores, en este caso las palabras. Por ende, se unen formando la palabra Matemática. En el caso 2 sucede lo mismo, pero usamos un string que sería la palabra La + la variable Z que sería la palabra Matemática. Y nos muestra la suma que sería La Matemática. Por último, en el algoritmo 3, podemos ver un operador de pertenencia el cual pregunta si la letra e se encuentra en la variable Z. Y nos arroja un True porque si se encuentra la letra e en la variable. En caso contrario arrojaría un False.")

msvcrt.getch()
