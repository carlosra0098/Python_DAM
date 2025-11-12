""" La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch)."""

nombre_postulante = input("Dígame su nombre: ")

while True:
    print("Bienvenido a la página de la Universidad. Dígame en qué Universidad va a estudiar: ")
    print("1. Ing de sistemas")
    print("2. Derecho")
    print("3. Ing naviera")
    print("4. Ing pesquera")
    print("5. Contabilidad")
    print("6. Administración")
    print("7. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            print("Ha elegido Ing de Sistemas", nombre_postulante)
            importe = 350
            mensualidad = 650
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
            
        case 2:
            print("Ha elegido Derecho", nombre_postulante)
            importe = 300
            mensualidad = 550
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
            
        case 3:
            print("Ha elegido Ing naviera", nombre_postulante)
            importe = 300
            mensualidad = 500
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
            
        case 4:
            print("Ha elegido Ing pesquera", nombre_postulante)
            importe = 310
            mensualidad = 460
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
        
        case 5:
            print("Ha elegido Contabilidad", nombre_postulante)
            importe = 280
            mensualidad = 490
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
            
        case 6:
            print("Ha elegido Administración", nombre_postulante)
            importe = 350
            mensualidad = 520
            IGV = importe + mensualidad * 0.18
            monto_final = importe + mensualidad + IGV
            print("El monto final de la matrícula es: ", monto_final)
            print("")
            print("")
            
        case 7:
            print("Has salido correctamente")
            break
                    
        case _:
            print("Error no es ninguna opción válida")
            print("")
            print("")