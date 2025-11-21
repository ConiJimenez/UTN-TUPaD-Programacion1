import utiles

#utiles.agregar_productos()
#utiles.mostrar_productos()
productos = utiles.cargar_productos_en_lista()
print()
utiles.agregar_productos()
utiles.buscar_producto(productos)
utiles.reescribir_archivo(productos)
