# Algoritmo que pida dos números e indique si el primero es mayor que el segundo.

num1 = int(input("Dime el primer número: "))
num2 = int(input("Dime el segundo número: "))

if num1 > num2:
    print("El primer número es mayor")
elif num1 < num2:
    print("El segundo número es mayor, por lo tanto no es mayor que el segundo")
elif num1 == num2:
    print("Los dos números son iguales, por lo tanto no es mayor que el segundo")