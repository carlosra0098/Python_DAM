# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Primero verificamos las condiciones más obvias
if año <= 0:
    print("El año debe ser un número positivo.")
elif mes < 1 or mes > 12:
    print("El mes debe estar entre 1 y 12.")
elif dia < 1:
    print("El día debe ser un número positivo.")
else:
    # Lista con los días de cada mes (para año no bisiesto)
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print("La fecha es correcta.")