# Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta, producto y división.

numero1 = input("Dime el primer número")
numero1 = int(numero1)

numero2 = input("Dime el segundo número")
numero2 = int(numero2)

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("La suma es: ", suma, "La resta es: ", resta, "La multiplicación es: ", multiplicacion, "La división es: ", division)