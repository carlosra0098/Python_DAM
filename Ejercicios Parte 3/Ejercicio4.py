# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

num1 = int(input("Dime el primer número: "))
num2 = int(input("Dime el segundo número: "))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2

if num2 == 0:
    print("Suma: ", suma)
    print("Resta: ", resta)
    print("Multipicación: ", mult)
    print("No se puede dividir entre 0")
else:
    div = num1 / num2
    print("Suma: ", suma)
    print("Resta: ", resta)
    print("Multipicación: ", mult)
    print("División: ", div)
