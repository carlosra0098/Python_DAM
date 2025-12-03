""" Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos."""

altura = int(input("Dime la altura de la pirámide: "))

for i in range(altura - 1):
    espacios = ' ' * (altura - i - 1)
    asteriscos = '*' * (2 * i + 1)
    print(espacios + asteriscos)

for j in range(altura):
    espacios = ' ' * j
    asteriscos = '*' * (2 * (altura - j) - 1)
    print(espacios + asteriscos)