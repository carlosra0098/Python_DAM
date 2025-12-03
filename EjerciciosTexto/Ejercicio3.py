""" Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador."""

cadena = input("Introduce una cadena: ")
longitud = len(cadena)
buscar = input("Qué caracter quieres buscar: ")
contador = 0

for i in range(longitud):
    if cadena[i] == buscar:
        contador += 1
        
print("El caracter aparece", contador, "veces.")