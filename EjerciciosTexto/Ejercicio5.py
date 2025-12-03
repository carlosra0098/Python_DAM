""" Verificar si un carácter específico está en la cadena con un ciclo y comparaciones."""

cadena1 = input("Introduce la cadena: ")
caracter_buscar = input("Qué caracter quieres encontrar: ")

encontrado = False

for caracter in cadena1:
    if caracter == caracter_buscar:
        encontrado = True
        break
    
if encontrado:
    print("El caracter encontrado:", caracter_buscar,"está en la cadena: ", cadena1)
else:
    print("No se ha encontrado el caracter", caracter_buscar)