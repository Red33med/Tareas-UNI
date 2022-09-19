
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
