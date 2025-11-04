# Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.

numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))

if numero1 > numero2:
    print("El número mayor es: ", numero1)
else:
    print("El número mayor es: ", numero2)
    
if numero1 == numero2:
    print("Los número son iguales")