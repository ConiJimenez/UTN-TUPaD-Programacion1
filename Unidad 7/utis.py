import os


def mostrar_productos():
    if not os.path.exists("productos.txt"):
        print(f"No existe 'productos.txt'")
        return None
    
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
