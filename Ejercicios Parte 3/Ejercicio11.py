""" Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""

num1 = int(input("Dime el primer número: "))
num2 = int(input("Dime el segundo número: "))

if num1 < 0:
    num1 = num1 * -1
if num2 < 0:
    num2 = num2 * -1
distancia = num1 - num2

if distancia < 0:
    distancia = distancia * -1
print("La distancia entre los dos números es: ", distancia)