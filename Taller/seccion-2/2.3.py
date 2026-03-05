# Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

while True:
    print("\nCALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "5":
        print("Programa finalizado.")
        break

    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", num1 + num2)

        elif opcion == "2":
            print("Resultado:", num1 - num2)

        elif opcion == "3":
            print("Resultado:", num1 * num2)

        elif opcion == "4":
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("No se puede dividir entre cero")

    else:
        print("Opción no válida.")