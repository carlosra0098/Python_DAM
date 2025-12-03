""" Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario."""

inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))
print(f"Números pares entre {inicio} y {fin}:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)