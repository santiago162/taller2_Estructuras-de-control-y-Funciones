# Crear un algoritmo que permita al usuario ingresar 10 números (que pueden repetirse) y luego muestre una lista sin elementos duplicados. Implementar la lógica de eliminación de duplicados usando ciclos y una lista auxiliar, sin utilizar funciones de conjuntos.

numeros = []
sin_duplicados = []


for i in range(10):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)


for num in numeros:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)