""" Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora
de llegada a la ciudad B."""

HH = int(input("Introduce las horas: "))
MM = int(input("Introduce los minutos: "))
SS = int(input("Introduce los segundos: "))
T = int(input("Introduce el tiempo de viaje en segundos: "))

total_segundos = HH * 3600 + MM * 60 + SS + T
hora_llegada = (total_segundos // 3600) % 24
minuto_llegada = (total_segundos % 3600) // 60
segundo_llegada = total_segundos % 60

print("La hora de llegada del ciclista a la ciudad es las: ",hora_llegada,":",minuto_llegada,":",segundo_llegada)