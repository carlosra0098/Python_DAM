""" Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos."""

contador_positivo = 0
contador_negativo = 0

hay_negativo = False
numero = None

while numero != 0:
    numero = int(input("Ingresa un número no nulo: "))
    if numero > 0:
        contador_positivo += 1
    elif numero < 0:
        hay_negativo = True
        contador_negativo += 1
        
if hay_negativo:
    print("Se ha leido al menos un número negativo.")
    
print("Números negativos leídos: ", contador_negativo)
print("Números positivos leídos: ", contador_positivo)