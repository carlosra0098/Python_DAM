# Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.

cadena = input("Dime una cadena: ")
cadena_nueva = ""

for caracter in cadena:
    if caracter != " ":
        cadena_nueva += caracter
        
print("Cadena resultante:", cadena_nueva)