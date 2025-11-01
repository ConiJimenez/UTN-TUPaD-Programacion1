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
                