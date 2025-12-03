"""Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para
esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para
determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por
los N empleados."""

num_trabajadores = int(input("Introduce el número de trabajadores: "))
tarifa_hora = float(input("Introduce la tarifa por hora trabajada (€): "))
sueldo_total_empresa = 0.0
for i in range(1, num_trabajadores + 1):
    dias_trabajados = int(input("\nIntroduce el número de días trabajados por el trabajador " + str(i) + ": "))
    horas_totales = 0.0
    
    for j in range(1, dias_trabajados + 1):
        horas_dia = float(input("  Introduce las horas trabajadas el día " + str(j) + ": "))
        horas_totales += horas_dia
    
    sueldo_trabajador = horas_totales * tarifa_hora
    sueldo_total_empresa += sueldo_trabajador
    print("Sueldo del trabajador " ,i, ": €", sueldo_trabajador)
    
print("\nTotal pagado por la empresa a los " ,num_trabajadores, " trabajadores: €", sueldo_total_empresa)