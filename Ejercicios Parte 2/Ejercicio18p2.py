""" Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla."""

A = int(input("Introduce un número: "))
B = int(input("Introduce el número para elevar: "))
resultado = 1

for i in range(B):
    resultado *= A
    
print("El número ", A,"elevado a ", B,"da como resultado: ", resultado)