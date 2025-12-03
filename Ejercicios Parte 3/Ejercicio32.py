""" La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los
siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo
minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
en turno de mañana, 15 %, y en turno de tarde, 10 %.
Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona
que realiza una llamada."""

tiempo_llamada = int(input("Cuánto tiempo duró la llamada: "))
dia_semana = input("Dime el día de la semana que es: ").strip().lower()
turno = input("Dime el turno en el que trabajas(mañana o tarde): ").strip().lower()

if tiempo_llamada <= 5:
    coste = tiempo_llamada * 1
elif tiempo_llamada <= 8:
    coste = (5 * 1) + ((tiempo_llamada - 5) * 0.8)   
elif tiempo_llamada <= 10:
    coste = (5 * 1) + (3 * 0.8) + ((tiempo_llamada - 8) * 0.7)
else:
    coste = (5 * 1) + (3 * 0.8) + (2 * 0.7) + ((tiempo_llamada - 10) * 0.5)

if dia_semana == "domingo":
    coste_total = coste + (coste * 3 /100)
    print("El coste total de la llamada es: ", coste_total)
else:
    if turno == "mañana":
        coste_total = coste + (coste * 15 / 100)
        print("El coste total de la llamada es: ", coste_total)
    elif turno == "tarde":
        coste_total = coste + (coste * 10 / 100)
        print("El coste total de la llamada es: ", coste_total)
        