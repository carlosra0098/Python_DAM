# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input("Dime la base: "))
altura = int(input("Dime su altura: "))

area = base * altura

perimetro = 2 * (base + altura)

print("El área del rectángulo es: ", area,"y el perímetro es: ", perimetro)