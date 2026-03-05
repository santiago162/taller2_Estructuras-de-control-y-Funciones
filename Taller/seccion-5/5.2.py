def calcular_promedio(lista):

    if len(lista) == 0:
        return "La lista está vacía"

    suma = sum(lista)
    promedio = suma / len(lista)

    return promedio


numeros = [10, 20, 30, 40]

resultado = calcular_promedio(numeros)

print("Promedio:", resultado)