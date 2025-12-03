""" Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos
variables."""

A = int(input("Dime el primer número: "))
B = int(input("Dime el segundo número: "))

A, B = B, A

print("El valor final de A es: ", A,"y el valor final de B es: ", B)