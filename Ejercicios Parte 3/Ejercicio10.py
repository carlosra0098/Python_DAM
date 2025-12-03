""" Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha
calificación se compone de los siguientes porcentajes:
• 55% del promedio de sus tres calificaciones parciales.
• 30% de la calificación del examen final.
• 15% de la calificación de un trabajo final."""

nota1 = float(input("Dime la nota del primer parcial: "))
nota2 = float(input("Dime la nota del segundo parcial: "))
nota3 = float(input("Dime la nota del tercer parcial: "))

promedio_notas = (nota1 + nota2 + nota3) / 3
promedio_notas = promedio_notas * 55 / 100

examen_final = float(input("Dime la nota del examen final: "))
nota_final = examen_final * 30 / 100

trabajo_final = float(input("Dime la nota del tranajo final: "))
nota_trabajo = trabajo_final * 15 / 100

calificacion_final = promedio_notas + nota_final + nota_trabajo

print("La califiación final del alumno es: ", calificacion_final)