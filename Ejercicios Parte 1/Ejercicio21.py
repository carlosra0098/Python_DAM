""" Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto."""

nombre = input("Dime tu nombre: ")
horas_trabajadas = int(input("Dime cuántas horas has trabajado: "))
tarifa_trabajador = int(input("Dime tu tarifa: "))
dinero_bruto = 0

if horas_trabajadas > 35:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    dinero_bruto = (horas_normales * tarifa_trabajador) + (horas_extra * tarifa_trabajador * 1.5)
else:
    dinero_bruto = horas_trabajadas * tarifa_trabajador

if dinero_bruto <= 500:
    dinero_neto = dinero_bruto
else:
    base_imponible = dinero_bruto - 500
    
    if base_imponible <= 400:
        impuesto = base_imponible * 0.25
        dinero_neto = 500 + (base_imponible - impuesto)
    else:
        impuesto_400 = 400 * 0.25
        resto = base_imponible - 400
        impuesto_resto = resto * 0.45
        impuesto_total = impuesto_400 + impuesto_resto
        dinero_neto = dinero_bruto - impuesto_total

print("El nombre del trabajador es:", nombre)
print("El salario bruto es:", dinero_bruto)
print("La tarifa por hora es:", tarifa_trabajador)
print("El salario neto es:", dinero_neto)