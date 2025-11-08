import csv
import os

ARCHIVO = "caalogo.csv"


def cargar_catalogo():
    catalogo = []

    if os.path.exists(ARCHIVO):
        archivo = open(ARCHIVO, "r")
        archivo.readline()
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                titulo = partes[0]
                cantidad = int(partes[1])
                catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})        
    return catalogo

def guardar_catalogo(catalogo):
    with open(ARCHIVO, "w") as archivo:
        archivo.write("TITULO,CANTIDAD\n")
        for libro in catalogo:
            archivo.write(libro["TITULO"] + "," + str(libro["CANTIDAD"]) + "\n")

def buscar_libro(catalogo, titulo):
    for libro in catalogo:
        if libro["TITULO"] == titulo:
            return libro
        return None

def mostrar_catalogo(catalogo):
    if len(catalogo) == 0:
        print("No hay libros cargados.")
    else:
        print("CATALOGO:")
        for libro in catalogo:
            print(libro["TITULO"], "-", libro["CANTIDAD"], "ejemplares")

def listar_agotados(catalogo):
    hay_agotados = False
    for libro in catalogo:
        if libro["CANTIDAD"] == 0:
            print("-", libro["TITULO"])
            hay_agotados= True
        if not hay_agotados:
            print("No hay libros agotados.") 

def consultar_disponibilidad(catalogo):
    titulo = input("Titulo: ")
    libro = buscar_libro(catalogo, titulo)
    if libro:
        print(f"{libro['CANTIDAD']} ejemplares disponibles.")
    else:
        print("Ese libro no está cargado.")

def ingresar_titulos(catalogo):
    cantidad = input("¿Cuantos libros querés cargar?")
    if not cantidad.isdigit():
        print("Debe ser un número.")  
        return
    cantidad = int(cantidad)

    for _ in range(cantidad):
        titulo = ""
        while titulo == "":
            titulo = input("Título del libro: ").strip()
            if titulo == "":
                print("No puede estar vacío")
            elif buscar_libro(catalogo, titulo):
                print("Ese libro ya existe")
                titulo = ""

        cant = input("Cantidad de ejemplares: ")
        if not cant.isdigit():
            print("Debe ser un número")
            continue

        catalogo.append({"TITULO": titulo, "CANTIDAD": cant})
        guardar_catalogo(catalogo)
        print("Libro cargado correctamente.")

def ingresar_ejemplares(catalogo):
    titulo = input("Titulo existente: ")
    libro = buscar_libro(catalogo, titulo)
    if libro is None:
        print("No existe ese libro")
        return
    
    cant = input("Cuántos ejemplares agregas? ")
    if not cant.isdigit():
        print("Debe ser un número")
        return
    
    libro["CANTIDAD"] += int(cant)
    guardar_catalogo(catalogo)
    print("Ejemplares actualizados.")

def agregar_titulo(catalogo):
    titulo = input("Nuevo título: ").strip()
    if titulo == "" or buscar_libro(catalogo, titulo):
        print("Título vacío o ya existe")
        return
    
    cant = input("Cantidad inicial: ")
    if not cant.isdigit():
        print("Debe ser un número")
        return
    
    catalogo.append({"TITULO": titulo, "CANTIDAD": int(cant)})
    guardar_catalogo(catalogo)
    print("Libro agregado")

def actualizar_prestamo_devolucion(catalogo):
    titulo = input("Título: ")
    libro = buscar_libro(catalogo, titulo)

    if libro is None:
        print("No existe ese libro")
        return
    
    print("1. Préstamo (restar 1)")
    print("2. Devolución (sumar 1)")
    opcion = input("Opción: ")

    if opcion == "1":
        if libro["CANTIDAD"] > 0:
            libro["CANTIDAD"] -= 1
            guardar_catalogo(catalogo)
            print("Préstamo realizado")
        else:
            print("No quedan ejemplares")
    elif opcion == "2":
        libro["CANTIDAD"] += 1
        guardar_catalogo(catalogo)
        print("Devolución realizada")
    else:
        print("Opción inválida")

def menu():
    catalogo = cargar_catalogo()
    opcion = ""

    while opcion != "8":
        print("\n-- MENU BIBLIOTECA --")
        print("1. Ingresar títulos")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar los agotados")
        print("6. Agregar título")
        print("7. Préstamo/Devolución")
        print("8. Salir")

        opcion = input("Elegí una opción: ")
        if opcion == "1":
            ingresar_titulos(catalogo)
        elif opcion == "2":
            ingresar_ejemplares(catalogo)
        elif opcion == "3":
            mostrar_catalogo(catalogo)
        elif opcion == "4":
            consultar_disponibilidad(catalogo)
        elif opcion == "5":
            listar_agotados(catalogo)
        elif opcion == "6":
            agregar_titulo(catalogo)
        elif opcion == "7":
            actualizar_prestamo_devolucion(catalogo)
        elif opcion == "8":
            print("Adios")
        else:
            print("Opción inválida")  

menu()  
        
