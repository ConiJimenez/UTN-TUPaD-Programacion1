import os

def mostrar_productos():
    if not os.path.exists("productos.txt"):
        print(f"No existe 'productos.txt'")
        return None
    
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
         nombre, precio, cantidad = linea.strip().split(",")
         print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

def agregar_productos():
    nombre = str(input("Ingrese el nombre del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print("Producto agregado con éxito.\n")

def mostrar_lista(productos):
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

def cargar_productos_en_lista():
    productos = []
    if not os.path.exists("productos.txt"):
        print(f"No existe 'productos.txt'")
        return []

    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre" : nombre,
                "precio" : precio,
                "cantidad" : cantidad
            }

            productos.append(producto)
        
        print("Productos cargados correctamente.")
        mostrar_lista(productos)
        return productos

