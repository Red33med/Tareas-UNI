import math

# Un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.

Nombre = str(input("Ingrese su Nombre: "))
print("Ahora estás en la matrix,", Nombre)


# Un programa que solicite al usuario ingresar un número con decimales y almacénelo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.


Numero_Decimal = float(input("Ingrese un número decimal: "))
Numero_Entero = int(input("Ingrese un número entero: "))

Suma_Numeros = (Numero_Decimal + Numero_Entero)

print("El resultado de la suma es", Suma_Numeros)

# Un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, se almacenará el resultado de la suma de esos dos números y luego mostrar ese resultado en pantalla. A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrar en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

Numero_1 = float(input("Primer Número: "))
Numero_2 = float(input("Segundo Número: "))

suma_numeros = Numero_1 + Numero_2
print("La suma de los dos números es: ", suma_numeros)

Numero_3 = float(input("Tercer Número: "))

print("La multiplicación de la suma y el tercer número es: ",
      suma_numeros * Numero_3)


# Un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.

Número = float(input("Ingrese un número: "))
print("El valor menos el 15% queda: ", Número - (Número * 15 / 100))
