# Ejercicio 1: Pirámide solo mitad y espacios en blancos
altura = int(input("Dime la altura de la pirámide: "))

for i in range(altura):
    espacios_externos = ' ' * (altura - i - 1)
    if i == 0:
        print(espacios_externos + '*')
    else:
        espacios_internos = ' ' * (i - 1)
        print(espacios_externos + '*' + espacios_internos + '*')

for i in range(altura - 2, -1, -1):
    espacios_externos = ' ' * (altura - i - 1)
    if i == 0:
        print(espacios_externos + '*')
    else:
        espacios_internos = ' ' * (i - 1)
        print(espacios_externos + '*' + espacios_internos + '*')


# Ejercicio 2: Triángulo de 4 con espacios en blanco
altura = int(input("Dime la altura de la pirámide: "))

for i in range(altura):
    if i == 0:
        print('4')
    elif i == altura - 1:
        print('4 ' * (altura - 1) + '4')
    else:
        espacios = ' ' * (2 * i - 1)
        print('4' + espacios + '4')