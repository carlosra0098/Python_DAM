""" Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas."""

contador_pares = 0
contador_impares = 0

for i in range(100, 200 + 1):
    if i % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
        
print("Suma pares: ", contador_pares, "Suma impares: ", contador_impares)