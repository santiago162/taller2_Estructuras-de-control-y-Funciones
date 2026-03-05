# Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.

print("CONVERTIDOR DE UNIDADES")
print("1. Celsius a Fahrenheit")
print("2. Kilómetros a Millas")
print("3. Kilogramos a Libras")

opcion = input("Selecciona una opción (1-3): ")

if opcion == "1":
    celsius = float(input("Ingresa los grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Resultado: {fahrenheit:.2f} °F")

elif opcion == "2":
    km = float(input("Ingresa los kilómetros: "))
    millas = km * 0.621371
    print(f"Resultado: {millas:.2f} millas")

elif opcion == "3":
    kg = float(input("Ingresa los kilogramos: "))
    libras = kg * 2.20462
    print(f"Resultado: {libras:.2f} libras")

else:
    print("Opción no válida")