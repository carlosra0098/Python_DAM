""" Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por
cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime
el resultado obtenido por el estudiante."""

preguntas_examen = int(input("Dime cuántas preguntas tiene el examen: "))

respuestas_correctas = int(input("Dime cuántas respuestas correctas tienes: "))
respuestas_incorrectas = int(input("Dime cuántas preguntas incorrectas tienes: "))
respuestas_blanco = int(input("Dime cuántas preguntas tienes en blanco: "))

if (respuestas_correctas + respuestas_incorrectas + respuestas_blanco) != preguntas_examen:
    print("Compi imposible de hacer porque no coinciden las preguntas")
else:
    notas_final = (respuestas_correctas * 5) + (respuestas_incorrectas * - 1) + (respuestas_blanco * 0)
print("La nota final es: ", notas_final)