""" Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos
son positivos y cuantos negativos."""

contador_negativo = 0
contador_positivo = 0

for i in range (100):
    numero = int(input("Introduce números no nulos (0): "))
    while numero == 0:
        print("No es un número válido ya que es nulo")
    if numero < 0:
        contador_negativo+=1
    if numero > 0:
        contador_positivo+=1
        
print("Hay ", contador_negativo,"números negativos y hay: ", contador_positivo,"número positivos")