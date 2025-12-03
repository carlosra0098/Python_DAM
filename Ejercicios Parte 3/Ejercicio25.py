# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("Introduce una letra: ")

if cadena.isupper():
    print("Es mayúscula")
else:
    print("Es minúscula")