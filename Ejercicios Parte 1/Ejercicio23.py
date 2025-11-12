""" Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra."""

while True:
    print("Bienvenido a la farmacia")
    print("1. Pagar con tarjeta")
    print("2. Pagar al contado")
    print("3. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            pago_tarjeta = float(input("Se aplica un recargo al pagar con tarjeta "))
            recargo = pago_tarjeta * 1.03
            print("El recargo es de:  ", recargo)
            print("")
            print("")
            
        case 2:
            pago_contado = float(input("Se aplica un descuento al pagar al contado "))
            descuento = pago_contado * 5 / 100
            pago_contado = pago_contado - descuento
            print("El descuento es de: ", descuento, "y el total a pagar es: ", pago_contado)
            print("")
            print("")
            
        case 3:
            print("Has salido correctamente")
            break
                
        case _:
            print("Error no es ninguna opción válida")
            print("")
            print("")
 