""" Realiza un programa que pida el dí-a de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error."""

dia_semana = int(input("Dime el día de la semana(1 al 7): "))

if dia_semana == 1:
    print("Es lunes")
elif dia_semana == 2:
    print("Es martes")
elif dia_semana == 3:
    print("Es miércoles")
elif dia_semana == 4:
    print("Es jueves")
elif dia_semana == 5:
    print("Es viernes")
elif dia_semana == 6:
    print("Es sábado")
elif dia_semana == 7:
    print("Es domingo")
else:
    print("Error")