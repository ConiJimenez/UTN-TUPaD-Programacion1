titulos = []
ejemplares = []
menu_abierto = 1

while (menu_abierto == 1):
    print("\n--- Menú Biblioteca ---")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Ingresar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo o devolución)")
    print("8. Salir")
    break

opcion = input("Seleccione una opción (1-8): ").strip()

if opcion == "1":
    cantidad_str = input("Cuántos títulos desea ingresar? ").strip()
    if cantidad_str.isdigit():
        cantidad = int(cantidad_str)
        contador = 0
        while contador < cantidad:
            titulo = input(f"Ingrese título {contador + 1}: ").strip()
            if titulo == "":
                print("El título no debe estar vacío.")
            elif titulo in titulos:
                print("Este título ya ha sido ingresado.")
            else:
                titulos.append(titulo)
                ejemplares.append(0)
                contador += 1

    else:
        print("Debe ingresar un número válido.")

elif opcion == "2":
    if len(titulos) == 0:
        print("No figuran títulos ingresados para asignarles ejemplares.")
    else: 
        for i in range(len(titulos)):
            cantidad_str = input(f"Ingrese la cantidad de ejemplares para '{titulos[i]}'").strip()
            if cantidad_str.isdigit():
                cantidad = int(cantidad_str)
                if cantidad >= 0:
                    ejemplares[i] = cantidad
                else:
                    print("La cantidad debe ser cero o mayor a cero.")
            else: 
                print("Debe ingresar un número válido.")

elif opcion == "3":
    if len(titulos) == 0:
        print("El catálogo está vacío.")
    else:
        print("\nCatálogo de libros:")
        for i in range(len(titulos)):
            print(f"{i + 1}). '{titulos[i]}' - Ejemplares: {ejemplares[i]}")

elif opcion == "4":
    if len(titulos) == 0:
        print("No hay títulos ingresados.")
    else:
        buscar = input("Ingrese el título que desea buscar: ").strip()
        if buscar in titulos:
            index = titulos.index(buscar)
            print(f"'{buscar}' tiene {ejemplares[index]} ejemplares.")
        else:
            print("El título no se encontró en el catálogo.")

elif opcion == "5":
    agotados = False
    for i in range(len(titulos)):
        if ejemplares[i] == 0:
            if not agotados:
                print("Libros agotados:")
                agotados = True
            print(f"- {titulos[i]}")
    if not agotados:
        print("No hay libros agotados.")

elif opcion == "6":
    nuevo_titulo = input("Ingrese el nuevo título: ").strip()
    if nuevo_titulo == "":
        print("El título no puede estar vacío.")
    elif nuevo_titulo in titulos:
        print("Este título ya se encuentra en el catálogo.")
    else:
        cantidad_str = input("Ingrese la cantidad de ejemplares: ").strip()
        if cantidad_str.isdigit():
            cantidad = int(cantidad_str)
            if cantidad >= 0:
                titulos.append(nuevo_titulo)
                ejemplares.append(cantidad)
                print(f"'{nuevo_titulo}' agregado con {cantidad} ejemplare.")
            else:
                print("La cantidad deber ser de cero o mayor a cero.")
        else:
            print("Debe ingresar un número válido.")

elif opcion == "7":
    if len(titulos) == 0:
        print("No hay títulos en el catálogo.")
    else:
        buscar = input("Ingrese el título para actualizar los ejemplares: ").strip()
        if buscar in titulos:
            index = titulos.index(buscar)
            print(f"Ejemplares actuales de '{buscar}': {ejemplares[index]}")
            accion = input("Desea hacer un préstamo (P) o una devolución (D)? " ).strip().upper()
            if accion == "P":
                if ejemplares[index] > 0:
                    ejemplares[index] -= 1
                    print(f"Préstamo realizado. Ejemplares que restan: {ejemplares[index]}") 
                else:
                    print("No hay ejemplares disponibles")
            elif accion == "D":
                ejemplares[index] += 1
                print(f"Devolución realizada. Ejemplares actuales: {ejemplares[index]}")     
            else: 
                print("Opción no válida. Debe ingresar 'P' o 'D'")
        else:
            print("El título no se halló en el catálogo")

elif opcion == "8":
    print("Saliendo del programa. Adiós.")
    menu_abierto = 0

else:
    print("Opción inválida. Seleccione una opción del 1 al 8.")