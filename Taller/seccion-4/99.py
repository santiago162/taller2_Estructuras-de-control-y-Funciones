contactos = {}

while True:
    print("\nDIRECTORIO DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el número telefónico: ")
        contactos[nombre] = telefono
        print("Contacto agregado correctamente.")

    elif opcion == "2":
        nombre = input("Ingresa el nombre a buscar: ")
        if nombre in contactos:
            print("Número:", contactos[nombre])
        else:
            print("El contacto no existe.")

    elif opcion == "3":
        nombre = input("Ingresa el nombre a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]
            print("Contacto eliminado.")
        else:
            print("El contacto no existe.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")