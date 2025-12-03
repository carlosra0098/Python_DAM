# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).

cadena = input("Dime una cadena: ")
cadena_nueva = ""

for caracter in cadena:
    if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u"\
    and caracter != "A" and caracter != "E" and caracter != "I" and caracter != "O" and caracter != "U" and caracter != " ":
        cadena_nueva += caracter
        
print("Cadena resultante:",cadena_nueva)  