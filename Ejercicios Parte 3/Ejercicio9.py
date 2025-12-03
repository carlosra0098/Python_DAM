""" Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea
saber cuánto deberá pagar finalmente por su compra."""

total_compra = float(input("Introduce el total de la compra: "))

descuento = total_compra * 15 / 100

pago_final = total_compra - descuento

print("El total a pagar después del descuento es: ", pago_final)