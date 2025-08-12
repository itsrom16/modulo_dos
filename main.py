from db_manager import crear_tabla, agregar_libro, actualizar_libro, eliminar_libro, ver_libros, buscar_libros

def mostrar_menu():
    print("\n📚 Biblioteca Personal")
    print("1. Agregar nuevo libro")
    print("2. Actualizar información de un libro")
    print("3. Eliminar libro existente")
    print("4. Ver listado de libros")
    print("5. Buscar libros")
    print("6. Salir")

def main():
    crear_tabla()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            estado = input("Estado (Leído / No leído): ")
            agregar_libro(titulo, autor, genero, estado)
            print("✅ Libro agregado con éxito.")

        elif opcion == "2":
            id_libro = int(input("ID del libro a actualizar: "))
            print("Campos: titulo, autor, genero, estado")
            campo = input("Campo a actualizar: ")
            nuevo_valor = input("Nuevo valor: ")
            actualizar_libro(id_libro, campo, nuevo_valor)
            print("✅ Libro actualizado.")

        elif opcion == "3":
            id_libro = int(input("ID del libro a eliminar: "))
            eliminar_libro(id_libro)
            print("🗑️ Libro eliminado.")

        elif opcion == "4":
            libros = ver_libros()
            print("\n📋 Lista de libros:")
            for libro in libros:
                print(libro)

        elif opcion == "5":
            campo = input("Buscar por (titulo / autor / genero): ")
            valor = input("Valor a buscar: ")
            resultados = buscar_libros(campo, valor)
            for libro in resultados:
                print(libro)

        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break

        else:
            print("⚠️ Opción inválida.")

if __name__ == "__main__":
    main()