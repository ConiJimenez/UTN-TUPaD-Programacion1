import utiles

def menu():
    productos = [] 

    while True:
        print("\n========= MENÚ =========")
        print("1. Mostrar productos desde el archivo")
        print("2. Agregar un producto")
        print("3. Cargar productos en una lista")
        print("4. Buscar producto en la lista")
        print("5. Reescribir archivo con la lista actual")
        print("6. Salir")
        print("========================")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            utiles.mostrar_productos()
        
        elif opcion == "2":
            utiles.agregar_productos()

        elif opcion == "3":
            productos = utiles.cargar_productos_en_lista()

        elif opcion == "4":
            utiles.buscar_producto(productos)

        elif opcion == "5":
            utiles.reescribir_archivo(productos)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

menu()