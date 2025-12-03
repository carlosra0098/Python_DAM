"""Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, calcule
cuánto pagó la empresa por los N empleados."""
num_trabajadores = int(input("Introduce el número de trabajadores: "))
tarifa_hora = float(input("Introduce la tarifa por hora trabajada (€): "))

sueldo_total_empresa = 0.0
for i in range(1, num_trabajadores + 1):
    horas_trabajadas = float(input(f"Introduce las horas trabajadas por el trabajador {i}: "))
    sueldo_trabajador = horas_trabajadas * tarifa_hora
    sueldo_total_empresa += sueldo_trabajador
    print("Sueldo del trabajador " ,i, ": €", sueldo_trabajador)
    
print("\nTotal pagado por la empresa a los " ,num_trabajadores, " trabajadores: €", sueldo_total_empresa)