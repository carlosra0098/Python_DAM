# Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.

cadena = input("Dime una cadena: ")
caracter_a_reemplazar = input("Dime que caracter quieres reemplazar: ")
caracter_reemplazo = input("Dime por qué caracter quieres reemplazarlo: ")
nueva_cadena = ""

for caracter in cadena:
    if caracter == caracter_a_reemplazar:
        nueva_cadena += caracter_reemplazo
    else:
        nueva_cadena += caracter
        
print("Cadena resultante:", nueva_cadena)