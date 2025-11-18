""" Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:
                *
               ***
              *****
             *******
            *********"""

altura = int(input("Dime la altura de la pirámide: "))

for i in range(altura):
    espacios = ' ' * (altura - i - 1)
    asteriscos = '*' * (2 * i + 1)
    print(espacios + asteriscos)
    
for i in range(1, altura + 1):
    for j in range(1, altura):
        print(" ", end = "")
    for k in range(1, (i*2)):
        print("*", end="")
    print()