# Árbol de Navidad

altura = int(input("Dime la altura del árbol: "))

#copa del árbol
for i in range(altura): # <- eso es el ancho de la copa
    #espacios
    espacios = " " * (altura - i - 1)
    #asteriscos
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)
    
#tronco del árbol
for _ in range(3): # <- eso es la altura del tronco
    #espacios tronco
    espacio = " " * (altura - 2)
    print(espacio + "***")