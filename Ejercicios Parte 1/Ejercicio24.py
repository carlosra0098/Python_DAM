""" Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra."""

monto_compra = float(input("Diga su monto de compra: "))
dia_semana = input("Diga el día de la semana que es (Si es martes o jueves se le aplicará un 15 por ciento de descuento) (PD: Tiene que escribir el día en minúsculas): ")

if dia_semana.lower() == "martes" or dia_semana.lower() == "jueves":
    monto_descuento = monto_compra * 15 / 100
    total_pagar = monto_compra - monto_descuento
    print(f"El descuento realizado por ser {dia_semana} es: €{monto_descuento:.2f}")
    print(f"El total a pagar es: €{total_pagar:.2f}")
else:
    print(f"El total a pagar es: €{monto_compra:.2f}")
