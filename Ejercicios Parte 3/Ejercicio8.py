""" Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y
comisiones."""

sueldo_base = float(input("Dime tu sueldo base: "))

venta1 = float(input("Dime el monto de la primera venta: "))
venta2 = float(input("Dime el monto de la segunda venta: "))
venta3 = float(input("Dime el monto de la tercera venta: "))

venta1 = venta1 * 10 / 100
print("El total de la primera venta es: ", venta1, "euros.")
venta2 = venta2 * 10 / 100
print("El total de la primera venta es: ", venta2, "euros.")
venta3 = venta3 * 10 / 100
print("El total de la primera venta es: ", venta3, "euros.")

sueldo_total = sueldo_base + venta1 + venta2 + venta3
print("El sueldo total es: ", sueldo_total)