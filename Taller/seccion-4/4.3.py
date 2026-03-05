# Dada una lista de diccionarios donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock", crear un programa que permita actualizar el precio de un producto específico buscándolo por su nombre.


productos = [
    {"nombre": "Laptop", "precio": 2500, "stock": 5},
    {"nombre": "Mouse", "precio": 50, "stock": 20},
    {"nombre": "Teclado", "precio": 120, "stock": 10}
]

nombre_buscar = input("Ingresa el nombre del producto a actualizar: ")

encontrado = False

for producto in productos:
    if producto["nombre"].lower() == nombre_buscar.lower():
        nuevo_precio = float(input("Ingresa el nuevo precio: "))
        producto["precio"] = nuevo_precio
        print("Precio actualizado correctamente.")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

print("\nLista actualizada:")
for producto in productos:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")