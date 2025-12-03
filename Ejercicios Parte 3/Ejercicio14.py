""" Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número
invertido."""

num = int(input("Dime un número de dos cifras: "))

if 10 <= num <= 99:
    invertido = (num % 10) * 10 + (num // 10)
    print("El número invertido es: ", invertido)
else:
    print("El número debe de ser de dos cifras.")