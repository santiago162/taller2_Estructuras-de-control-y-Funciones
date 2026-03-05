# Desarrollar una calculadora simple que solicite al usuario dos números y una operación matemática (+, -, *, /). El algoritmo debe realizar la operación correspondiente y mostrar el resultado. Incluir validación para evitar la división por cero.


nombre = input("Ingresa tu nombre: ")


while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            break
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


ciudad = input("Ingresa tu ciudad de residencia: ")


print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")