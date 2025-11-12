""" En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch)."""

while True:
    print("\n=== CASINO DE DADOS ===")
    print("1. Lanzar dados y evaluar")
    print("2. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    match opcion:
        case 1:
            dado1 = int(input("Dime el número del primer dado (1-6): "))
            dado2 = int(input("Dime el número del segundo dado (1-6): "))
            dado3 = int(input("Dime el número del tercer dado (1-6): "))
            
            cantidad_seis = 0
            if dado1 == 6:
                cantidad_seis += 1
            if dado2 == 6:
                cantidad_seis += 1
            if dado3 == 6:
                cantidad_seis += 1
                
            print(f"\nResultados: Dado1={dado1}, Dado2={dado2}, Dado3={dado3}")
            
            match cantidad_seis:
                case 3:
                    print(" Excelente - Los tres dados son seis")
                case 2:
                    print(" Muy bien - Dos dados son seis")
                case 1:
                    print(" Regular - Un dado es seis")
                case 0:
                    print(" Pésimo - Ningún dado es seis")
                    
        case 2:
            print("¡Ha salido correctamente del casino!")
            break
            
        case _:
            print("Opción no válida. Por favor seleccione 1 o 2.")