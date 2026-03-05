# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

N = int(input("Ingresa un número entero positivo: "))

if N > 0:
    print("Números pares desde 1 hasta", N, ":")

    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i)
else:
    print("El número debe ser positivo.")