""" Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún
número negativo o no."""

contador = 0

for i in range (100):
    numero = int(input("Introduce números no nulos (0): "))
    while numero == 0:
        print("Es un número nulo, no es válido")
        
    if numero < 0:
        contador += 1 
        
if contador > 0:
    print("Hay negativos")
else:
    print("Hay positivos")