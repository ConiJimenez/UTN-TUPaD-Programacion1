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
            archivo.close()         
    return catalogo

def guardar_catalogo(catalogo):
    archivo = open(ARCHIVO, "w")
    archivo.write("TITULO,CANTIDAD\n")
    for libro in catalogo:
        archivo.write(libro["TITULO"] + "," + str(libro["CANTIDAD"]) + "\n")
        archivo.close()

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
        cant = int(cant)
        catalogo.append({"TITULO": titulo, "CANTIDAD": cant})
        guardar_catalogo(catalogo)
        print("Libro cargado correctamente.")


    