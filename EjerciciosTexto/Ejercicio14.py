# Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.

cadena = input("Dime una cadena que contenga números(0 a 9 solamente): ")
numeros = "0123456789"
cont_num = 0

for caracter in cadena:
    if caracter in numeros:
        cont_num += 1
        
print("Hay", cont_num,"números en la cadena")