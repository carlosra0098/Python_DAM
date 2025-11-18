""" Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. Este es un ejemplo:"""

altura = int(input("Dime la altura de la pirámide: "))

for i in range(altura):
    espacios = ' ' * i
    asteriscos = '*' * (2 * (altura - i) - 1)
    print(espacios + asteriscos)