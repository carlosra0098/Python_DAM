""" Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso
contrario, el programa termina cuando se introduce un espacio."""

letra = input("Introduce un carácter (espacio para terminar): ")
vocales = 'aeiouAEIOU'
while letra != ' ':
    if letra in vocales:
        print("VOCAL")
    else:
        print("NO VOCAL")
    letra = input("Introduce un carácter (espacio para terminar): ")
    
print("Programa terminado.")