def modificar_lista(lista):
    print("Dentro de la función antes de reasignar:", lista)
    lista.append(4)
    print("Dentro de la función después de reasignar:", lista)
mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista)
