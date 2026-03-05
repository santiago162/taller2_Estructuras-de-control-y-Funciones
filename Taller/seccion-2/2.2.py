# Implementar un menú interactivo con tres opciones: 1. Saludar, 2. Despedirse, 3. Salir. El programa debe mostrar el menú, leer la opción seleccionada y ejecutar la acción correspondiente utilizando estructuras condicionales if-elif-else.

while True:
    print("\nMENÚ")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        print("Hola, ¡qué gusto saludarte!")

    elif opcion == "2":
        print("Hasta luego, ¡que tengas un buen día!")

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")