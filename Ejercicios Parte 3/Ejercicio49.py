"""Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la
semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por
las horas trabajadas."""
horas_totales = 0
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
tarifa_hora = float(input("Introduce la tarifa por hora trabajada (€): "))

for dia in dias_semana:  # Recorre directamente la lista
    horas_dia = float(input("Introduce las horas trabajadas el " + dia + ": "))
    horas_totales += horas_dia
    
sueldo = horas_totales * tarifa_hora
print("Total de horas trabajadas en la semana: " ,horas_totales)
print("Sueldo total a recibir: €" ,sueldo)