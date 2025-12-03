# Leer una cadena y construir una nueva cadena con los caracteres en orden inverso.

cadena = input("Dime una cadena: ")
cadena_nueva = ""

for caracter in cadena:
    cadena_nueva = caracter + cadena_nueva
    
print("Cadena resultante:", cadena_nueva)