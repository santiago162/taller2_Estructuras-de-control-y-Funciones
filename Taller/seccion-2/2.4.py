# Desarrollar un sistema que convierta una calificación numérica (0-100) a su equivalente en letras según la siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Validar que la nota ingresada esté dentro del rango permitido.

nota = float(input("Ingresa la calificación (0-100): "))

if nota < 0 or nota > 100:
    print("Nota no válida. Debe estar entre 0 y 100.")

elif nota >= 90:
    print("Calificación: A")

elif nota >= 80:
    print("Calificación: B")

elif nota >= 70:
    print("Calificación: C")

elif nota >= 60:
    print("Calificación: D")

else:
    print("Calificación: F")