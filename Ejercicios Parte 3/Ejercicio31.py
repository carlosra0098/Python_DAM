""" Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65
euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de
30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que
debe pagar cada alumno por el viaje."""

alumnos = int(input("Cuántos alumnos van a ir al viaje: "))

if alumnos > 100:
    pago_alumno = 65
    total_pagar = alumnos * pago_alumno
    print("Cada alumno debe pagar: ", pago_alumno,"y el total a pagar es: ", total_pagar)
elif alumnos >= 50 and alumnos <= 99:
    pago_alumno = 70
    total_pagar = alumnos * pago_alumno
    print("Cada alumno debe pagar: ", pago_alumno,"y el total a pagar es: ", total_pagar)
elif alumnos >= 30 and alumnos <= 49:
    pago_alumno = 95
    total_pagar = alumnos * pago_alumno
    print("Cada alumno debe pagar: ", pago_alumno,"y el total a pagar es: ", total_pagar)
elif alumnos < 30:
    total_pago = 4000
    costo_alumnos = total_pago / alumnos
    print("La renta del autobús es de: ", total_pago," y el total a pagar de cada alumnos es: ", costo_alumnos)
