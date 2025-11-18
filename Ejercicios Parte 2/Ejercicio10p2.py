# Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.

suma = 0
multiplicacion = 1

for i in range(1, 10 + 1):
    suma = suma + i
    multiplicacion = multiplicacion * i

print("La suma es: ", suma,"y la multiplicación es: ", multiplicacion)