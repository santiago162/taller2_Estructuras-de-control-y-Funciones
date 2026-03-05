# Desarrollar una calculadora simple que solicite al usuario dos números y una operación matemática (+, -, *, /). El algoritmo debe realizar la operación correspondiente y mostrar el resultado. Incluir validación para evitar la división por cero.


# Pedir datos
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

# Realizar operación
if operacion == "+":
    print("Resultado:", num1 + num2)

elif operacion == "-":
    print("Resultado:", num1 - num2)

elif operacion == "*":
    print("Resultado:", num1 * num2)

elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir entre cero")

else:
    print("Operación no válida")