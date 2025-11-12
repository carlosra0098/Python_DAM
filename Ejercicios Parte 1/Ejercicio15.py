""" Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
son iguales."""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")
elif num1 > num2 == num3:
    print(num1, ">" ,num2, "=", num3)
elif num1 == num2 < num3:
    print(num1, "=", num2, "<", num3)
elif num1 < num2 == num3:
    print(num1, "<", num2, "=", num3)
elif num1 == num2 > num3:
    print(num1, "=", num2, ">", num3)
elif num1 == num3 > num2:
    print(num1, "=", num3, ">", num2)
elif num1 == num3 < num2:
    print(num1, "=", num3, "<", num2)
elif num1 > num2 > num3:
    print(num1, ">", num2, ">", num3)
elif num1 > num3 > num2:
    print(num1, ">", num3, ">", num2)
elif num2 > num1 > num3:
    print(num2, ">", num1, ">", num3)
elif num2 > num3 > num1:
    print(num2, ">", num3, ">", num1)
elif num3 > num1 > num2:
    print(num3, ">", num1, ">", num2)
elif num3 > num2 > num1:
    print(num3, ">", num2, ">", num1)
else:
    print("Error en la comparación de números.")