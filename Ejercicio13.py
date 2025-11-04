# Escriba un programa que lea dos números y lo visualiza en orden ascendente.

numero1 = float(input("Dime el primer número: "))
numero2 = float(input("Dime el segundo número: "))

if numero1 > numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)