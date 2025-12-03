""" Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar qué tipo de triángulo es, teniendo en
cuenta:
• Si se cumple Pitágoras entonces es triángulo rectángulo
• Si sólo dos lados del triángulo son iguales entonces es isósceles.
• Si los 3 lados son iguales entonces es equilátero.
• Si no se cumple ninguna de las condiciones anteriores, es escaleno."""

A = int(input("Ingrese la longitud del lado A: "))
B = int(input("Ingrese la longitud del lado B: "))
C = int(input("Ingrese la longitud del lado C: "))

if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("El triángulo es rectángulo.")
elif A == B and B == C:
    print("El triángulo es equilátero.")
elif A == B or B == C or A == C:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")