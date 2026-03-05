# Desarrollar un programa que solicite al usuario un número y genere su tabla de multiplicar del 1 al 10. Luego, debe preguntar si desea generar otra tabla, continuando este proceso hasta que el usuario decida salir.

while True:
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

    print(f"\nTabla del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    continuar = input("\n¿Deseas generar otra tabla? (s/n): ").lower()

    if continuar != "s":
        print("Programa finalizado.")
        break