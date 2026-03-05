# Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.


entrada1 = input("Ingresa los elementos de la primera lista separados por comas: ")
entrada2 = input("Ingresa los elementos de la segunda lista separados por comas: ")

lista1 = []
lista2 = []


for elemento in entrada1.split(","):
    lista1.append(elemento.strip())

for elemento in entrada2.split(","):
    lista2.append(elemento.strip())

comunes = []
unicos_lista1 = []
unicos_lista2 = []


for elemento in lista1:
    if elemento in lista2:
        if elemento not in comunes:
            comunes.append(elemento)
    else:
        unicos_lista1.append(elemento)


for elemento in lista2:
    if elemento not in lista1:
        unicos_lista2.append(elemento)


print("\nElementos comunes:", comunes)
print("Elementos únicos de la primera lista:", unicos_lista1)
print("Elementos únicos de la segunda lista:", unicos_lista2)