""" Construir manualmente una nueva cadena añadiendo un carácter a la vez 
(ejemplo: filtrar caracteres o construir cadenas invertidas)."""

cadena = input("Añade una cadena: ")
reves = ""

for i in range(len(cadena) -1, -1, -1):
    reves += cadena[i]
    
print(reves)