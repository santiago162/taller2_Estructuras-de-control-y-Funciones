def factorial(n):

    if n < 0:
        return "No existe factorial para números negativos"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


numero = int(input("Ingresa un número: "))

print("Factorial:", factorial(numero))