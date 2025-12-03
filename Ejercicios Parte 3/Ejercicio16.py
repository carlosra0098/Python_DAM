""" Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto
determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro."""

distancia = float(input("Dime la distancia entre los dos coches: "))
v1 = float(input("Dime la velocidad a la que va el coche más lento: "))
v2 = float(input("Dime la velocidad a la que va el coche más rapido: "))

if v2 <= v1:
    print("El vehículo más rápido es el segundo, inténtalo de nuevo")
elif distancia <= 0:
    print("Imposible compi")
else:
    velocidad_relativa = v2 - v1
    
    tiempo_horas = distancia / velocidad_relativa
    
    tiempo_minutos = tiempo_horas * 60
    
    print("El coche más rapido alcanzará al más lento en: ", tiempo_minutos,"minutos e irá con una velocidad relativa al otro coche de: ", velocidad_relativa,"km/h")
