""" Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo."""

hora = int(input("Dime una hora: "))
minuto = int(input("Dime los minutos: "))
segundo = int(input("Dime los segundos: "))

segundo = segundo + 1
if segundo == 60:
    minuto + 1
    segundo = 0
    if minuto == 60:
        hora + 1
        minuto = 0
        if hora == 23:
            hora = 0

print("Despues de un segundo serán las: ", hora, " con los minutos: ", minuto, "y segundos: ", segundo)