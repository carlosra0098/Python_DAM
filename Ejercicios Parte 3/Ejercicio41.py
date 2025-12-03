""" Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
introducir). El programa debe informar de cuantos números introducidos son mayores que 0,
menores que 0 e iguales a 0."""

num = int(input("Dime los números que vas a introducir: "))
contador_mayores = 0
contador_menores = 0  
contador_iguales = 0

for _ in range(num):
    num = float(input("Introduce un número: "))
    if num > 0:
        contador_mayores += 1
    elif num < 0:
        contador_menores += 1
    else:
        contador_iguales += 1
        
print("Números mayores a 0: ", contador_mayores)
print("Números menores a 0: ", contador_menores)
print("Números iguales a 0: ", contador_iguales)