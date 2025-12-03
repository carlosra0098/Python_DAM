# Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

cadena = input("Dime una cadena: ")
vocales = "aeiouAEIOU"
cadena_nueva = ""

for caracter in cadena:
    if caracter in vocales:
        cadena_nueva += "*"
    else:
        cadena_nueva += caracter
        
print("Cadena resultante:", cadena_nueva)