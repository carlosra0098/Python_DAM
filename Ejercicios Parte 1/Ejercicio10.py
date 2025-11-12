"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)."""

numero_1 = float(input("Dime el primer número"))
numero_2 = float(input("Dime el segundo número"))

suma = numero_1 + numero_2
resta = numero_1 + numero_2
multiplicacion = numero_1 * numero_2

if numero_2 == 0:
    print("El número no se puede dividir entre 0")
    print("Suma: ", suma, "Resta: ", resta, "Multiplicación: ", multiplicacion)
else:
    division = numero_1 / numero_2
    print("Suma: ", suma, "Resta: ", resta, "Multiplicación: ", multiplicacion, "División: ", division)