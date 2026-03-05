# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.


nombres = ["Ana", "Luis", "Carlos", "Marta", "Sofia"]

buscar = input("Ingresa el nombre que deseas buscar: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i].lower() == buscar.lower():
        print("Nombre encontrado en la posición:", i)
        encontrado = True
        break

if not encontrado:
    print("El nombre no se encuentra en la lista.")