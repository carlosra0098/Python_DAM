# Escriba un programa que pida un número entre 0 y 99999, y que diga cuántas cifras tiene.

numero = int(input("Introduce un número: "))
contador = 1

while numero < 0 or numero > 99999:
    print("El número no es válido")
    numero = int(input("Introduce un número"))
    
while numero > 10:
    numero = numero / 10
    contador = contador+1
    
print("El número tiene ", contador,"cifras")
