""" Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos."""

suma = 0
contador = 0        
numero = None

while numero != 0:
    numero = int(input("Introduce un número (0 para terminar): "))
    suma += numero
    if numero != 0:
        contador += 1
if contador > 0:
    media = suma / contador
    print("La suma de los números introducidos es:", suma)
    print("La media de los números introducidos es:", media)
else:
    print("No se han introducido números distintos de cero.")