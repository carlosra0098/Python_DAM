""" Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales."""

numero1 = int(input("Dime el primer número: "))
numero2 = int(input("Dime el segundo número: "))
numero3 = int(input("Dime el tercer número: "))

if numero1 > numero2 or numero1 > numero3:
    print("El número mayor es: ", numero1)
elif numero2 > numero1 or numero2 > numero3:
    print("El número mayor es: ", numero2)
elif numero3 > numero1 or numero3 > numero2:
    print("El número mayor es: ", numero3)
    
if numero1 == numero2 == numero3:
    print("Los número son iguales")