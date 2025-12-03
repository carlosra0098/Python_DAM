""" Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente. Si introducimos otro número nos da un error."""

mes = int(input("Dime el mes(1 al 12): "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("El mes tiene 31 días")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días")
elif mes == 2:
    print("El mes tiene 28 o 29 días")
else:
    print("Error")