# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import time

horas = 0
minutos = 0
segundos = 0

print("CRONÓMETRO EN EJECUCIÓN")
print("=" * 40)

while True:
    print(f"Tiempo: {horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
    
    time.sleep(1)
    
    segundos = segundos + 1
    
    if segundos == 60:
        segundos = 0
        minutos = minutos + 1
    
    if minutos == 60:
        minutos = 0
        horas = horas + 1