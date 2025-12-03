"""Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que
seleccionamos la opción de 'Salir.'"""
print("=== PROTECTORA DE ANIMALES ===")

while True:
    print("\n1. Registrar animal")
    print("2. Ver animales")
    print("3. Buscar animal")
    print("4. Registrar adopción")
    print("5. Salir")
    
    opcion = input("Opción: ")
    
    match opcion:
        case "1":
            print("--- Registrar Animal ---")
            nombre = input("Nombre: ")
            especie = input("Especie (Perro/Gato): ")
            print(" " + nombre + " (" + especie + ") registrado")
            
        case "2":
            print("--- Animales Disponibles ---")
            print("Luna - Perro - 2 años")
            print("Michi - Gato - 1 año")
            print("Roco - Perro - 4 años")
            
        case "3":
            print("\n--- Buscar Animal ---")
            buscar = input("Buscar por nombre/especie: ")
            print(" Buscando" + buscar + "...")
            
        case "4":
            print("--- Registrar Adopción ---")
            animal = input("Nombre del animal: ")
            adoptante = input("Nombre del adoptante: ")
            print("¡" + animal + " adoptado por " + adoptante + "!")
            
        case "5":
            print("¡Gracias por ayudar a los animales!")
            break
            
        case _:
            print("Opción no válida")