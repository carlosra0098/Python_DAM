""" Realizar un algoritmo que muestre la tabla de multiplicar de un número introducido por
teclado."""

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
print("Tabla de multiplicar del" ,numero, ":")
for i in range (1,11):
    resultado = numero * i 
    print (numero, "x", i, "=", resultado)