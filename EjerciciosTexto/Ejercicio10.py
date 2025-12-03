# Leer una cadena y contar cuántos caracteres son letras mayúsculas.

cadena = input("Dime una cadena: ")
mayuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cont_mayuscula = 0

for caracter in cadena:
    if caracter in mayuscula:
        cont_mayuscula += 1
        
print("Hay", cont_mayuscula,"mayúsculas en la cadena")