# Desarrollar un programa que solicite al usuario ingresar una lista de números separados por comas. El algoritmo debe calcular y mostrar: el valor máximo, el valor mínimo, el promedio y la suma total de todos los números.


entrada = input("Ingresa números separados por comas: ")


lista = entrada.split(",")
numeros = []

for num in lista:
    numeros.append(float(num.strip()))


maximo = max(numeros)
minimo = min(numeros)
suma = sum(numeros)
promedio = suma / len(numeros)


print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)
print("Suma total:", suma)
print("Promedio:", promedio)