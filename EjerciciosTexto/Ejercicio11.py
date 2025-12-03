# Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.

cadena = input("Dime una cadena: ")
vocales = "aeiouAEIOU"
cadena_nueva = ""

for caracter in cadena:
    if caracter in vocales:
        cadena_nueva += caracter * 2
    else:
        cadena_nueva += caracter
        
print("Cadena resultante:", cadena_nueva)