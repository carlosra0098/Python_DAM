# Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).

cadena1 = input("Dime una cadena: ")
cadena2 = input("Dime una cadena: ")
cadena_nueva = ""

for caracter in cadena1:
    cadena_nueva = "".join([cadena_nueva, caracter])
    
for caracter in cadena2:
    cadena_nueva = "".join([cadena_nueva, caracter])
    
print("Cadena resultante:", cadena_nueva)