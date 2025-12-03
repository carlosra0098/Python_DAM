# Leer una cadena y contar cuántas vocales contiene.

cadena = input("Dime una cadena: ")
vocales ="aeiouAEIOU"
cont_vocal = 0

for caracter in cadena:
    if caracter in vocales:
        cont_vocal += 1
    
print("Hay",cont_vocal,"vocales en la cadena")