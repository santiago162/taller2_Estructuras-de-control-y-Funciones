biblioteca = []


contador_id = 1



def agregar_libro():
    global contador_id

    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")

    while True:
        año = input("Ingrese el año de publicación: ")
        if año.isdigit() and int(año) > 1900:
            año = int(año)
            break
        else:
            print("El año debe ser un número mayor a 1900.")

    libro = {
        "id": contador_id,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "disponible": True
    }

    biblioteca.append(libro)
    contador_id += 1

    print("Libro agregado correctamente.")



def mostrar_libros():

    if len(biblioteca) == 0:
        print("No hay libros registrados.")
        return

    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"

        print(
            f"ID: {libro['id']} - '{libro['titulo']}' "
            f"({libro['autor']}, {libro['año']}) [{estado}]"
        )



def buscar_libro():

    busqueda = input("Ingrese título o autor a buscar: ").lower()

    encontrados = False

    for libro in biblioteca:
        if busqueda in libro["titulo"].lower() or busqueda in libro["autor"].lower():

            estado = "Disponible" if libro["disponible"] else "Prestado"

            print(
                f"ID: {libro['id']} - '{libro['titulo']}' "
                f"({libro['autor']}, {libro['año']}) [{estado}]"
            )
            encontrados = True

    if not encontrados:
        print("No se encontraron coincidencias.")


def prestar_libro():

    id_libro = int(input("Ingrese el ID del libro a prestar: "))

    for libro in biblioteca:
        if libro["id"] == id_libro:

            if libro["disponible"]:
                libro["disponible"] = False
                print("Libro prestado correctamente.")
            else:
                print("El libro ya está prestado.")
            return

    print("Libro no encontrado.")


def devolver_libro():

    id_libro = int(input("Ingrese el ID del libro a devolver: "))

    for libro in biblioteca:
        if libro["id"] == id_libro:

            if not libro["disponible"]:
                libro["disponible"] = True
                print("Libro devuelto correctamente.")
            else:
                print("El libro ya estaba disponible.")
            return

    print("Libro no encontrado.")



def eliminar_libro():

    id_libro = int(input("Ingrese el ID del libro a eliminar: "))

    for libro in biblioteca:
        if libro["id"] == id_libro:

            if libro["disponible"]:
                biblioteca.remove(libro)
                print("Libro eliminado correctamente.")
            else:
                print("No se puede eliminar un libro prestado.")
            return

    print("Libro no encontrado.")



def libros_por_autor():

    autor = input("Ingrese el autor: ").lower()

    for libro in biblioteca:
        if autor in libro["autor"].lower():

            estado = "Disponible" if libro["disponible"] else "Prestado"

            print(
                f"ID: {libro['id']} - '{libro['titulo']}' "
                f"({libro['autor']}, {libro['año']}) [{estado}]"
            )



def estadisticas():

    total = len(biblioteca)
    disponibles = 0
    prestados = 0

    for libro in biblioteca:
        if libro["disponible"]:
            disponibles += 1
        else:
            prestados += 1

    print("Total de libros:", total)
    print("Libros disponibles:", disponibles)
    print("Libros prestados:", prestados)



def exportar_a_txt():

    archivo = open("biblioteca.txt", "w", encoding="utf-8")

    for libro in biblioteca:

        estado = "Disponible" if libro["disponible"] else "Prestado"

        linea = (
            f"ID: {libro['id']} - '{libro['titulo']}' "
            f"({libro['autor']}, {libro['año']}) [{estado}]\n"
        )

        archivo.write(linea)

    archivo.close()

    print("Libros exportados a biblioteca.txt")



def menu_principal():

    while True:

        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro")
        print("7. Libros por autor")
        print("8. Estadísticas")
        print("9. Exportar a TXT")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            mostrar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            prestar_libro()

        elif opcion == "5":
            devolver_libro()

        elif opcion == "6":
            eliminar_libro()

        elif opcion == "7":
            libros_por_autor()

        elif opcion == "8":
            estadisticas()

        elif opcion == "9":
            exportar_a_txt()

        elif opcion == "10":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")



menu_principal()