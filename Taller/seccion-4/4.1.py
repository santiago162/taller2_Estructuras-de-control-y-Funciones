# Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

lista_compras = []

while True:
    print("\nLISTA DE COMPRAS")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar productos")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ").strip()

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        lista_compras.append(producto)
        print("Producto agregado correctamente.")

    elif opcion == "2":
        producto = input("Ingresa el producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print("Producto eliminado.")
        else:
            print("El producto no está en la lista.")

    elif opcion == "3":
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            print("Productos en la lista:")
            for i, producto in enumerate(lista_compras, start=1):
                print(f"{i}. {producto}")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")