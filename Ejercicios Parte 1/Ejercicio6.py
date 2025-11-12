# Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de descuento realizado.

print("Introduce el precio del artículo")
precio = input()
precio = float(precio)

print("Introduce el precio de venta real")
real = input()
real = float(real)

descuento = ((real - precio) / real) * 100

print("El descuento del producto ha sido de: ", descuento, "%")

