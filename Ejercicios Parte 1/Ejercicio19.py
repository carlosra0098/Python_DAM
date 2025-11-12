""" Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir"""

saldo = 1000

while True:
    print("Bienvenido a su Cajero Virtual")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero")
    print("3. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            ingreso = int(input("Cuánto dinero quieres ingresar "))
            saldo = saldo + ingreso
            print("Tu saldo actual es: ", saldo)
            print("")
            print("")
            
        case 2:
            retirada = int(input("Cuánto dinero quieres retirar "))
            if retirada <= saldo:
                saldo = saldo - retirada
                print("Tu saldo actual es: ", saldo)
            print("")
            print("")
        
        case 3:
            print("Has salido correctamente")
            print("Saldo final: ", saldo)
            break
                
        case _:
            print("Error no es ninguna opción válida")
            print("")
            print("")
