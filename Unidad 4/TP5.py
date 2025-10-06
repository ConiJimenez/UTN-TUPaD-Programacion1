#Ejercicio 1:
notas = [10, 5.50, 4.50, 9, 7, 6, 10, 3, 8, 9]

print("Lista de notas de los 10 estudiantes: ")
print(notas)

promedio = sum(notas) / len(notas)
print(f"\nPromedio de las notas: {promedio: .2f}") 

nota_mas_alta = max(notas)

print(f"La nota más alta es: {nota_mas_alta}")

nota_mas_baja = min(notas)

print(f"La nota más baja es: {nota_mas_baja}")

#Ejercicio 2:
productos = []

print("Ingrese 5 productos: ")
for i in range(5):
    producto = input(f"Producto {i + 1}: ")
    productos.append(producto)

productosOrdenados = sorted(productos)
print("\nLista de productos ordenados: ")
print(productosOrdenados)

#Ejercicio 3:
numeros = [5, 8, 4, 10, 7, 3, 2, 20, 45, 65, 14, 4, 1, 89,99]

num_pares = []
num_impares = []

for numero in numeros:
    if numero % 2 == 0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)

print("Lista original de 15 números: ")
print(numeros)

print(f"Lista de números pares: ")
print(num_pares)
print(f"Cantidad de números pares: {len(num_pares)}")

print(f"Lista de números impares: ")
print(num_impares)
print(f"Cantidad de números impares: {len(num_impares)}")

#Ejercicio 4:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

for valor in [1, 3, 5]:
    while valor in datos:
        datos.remove(valor)

print("Lista sin 1, 3 y 5:")
print(datos)

#Ejercicio 5: 
estudiantes = ["Lorena", "Pablo", "Jorge", "Pedro", "Ismael", "Hernan", "Ines", "Alicia"]

accion = input("\n¿Quiere agregar un nuevo estudiante o eliminar uno existente? (escribí 'agregar' o 'eliminar'): ").lower()

if accion == "agregar":
    nuevo = input("Ingresa el nombre del nuevo/a estudiante: ")
    estudiantes.append(nuevo)
    print(f"{nuevo} ha sido ingresado/a a la lista.")

elif accion == "eliminar":
    eliminar_estudiante = input("¿A qué estudiante de la lista desea eliminar?: ")
    estudiantes.remove(eliminar_estudiante)
    print(f"{eliminar_estudiante} ha sido eliminado/a de la lista.")
else:
    print("Opción no válida. No se realizaron cambios.")

print("\nLista final de estudiantes: ")
print(estudiantes)

#Ejercicio 6:
lista = [7, 5, 4, 9, 3, 2, 1]

print("\nLista original: ")
print(lista)

cantidad_elementos = len(lista)

for indice_pasada in range(cantidad_elementos - 1):

    for indice_actual in range(cantidad_elementos - 1 - indice_pasada):
        if lista[indice_actual] > lista[indice_actual + 1]:
            lista[indice_actual], lista[indice_actual + 1] = lista[indice_actual + 1], lista[indice_actual]

print("Lista ordenada (de menor a mayor): ")
print(lista)

#Ejercicio 7:
temperaturas = [ 
    [15, 25],
    [18, 24],
    [11, 18],
    [18, 22],
    [14, 25],
    [19, 27],
    [17, 22],
]

suma_min = 0
suma_max = 0

for t in temperaturas:
    suma_min += t[0]
    suma_max += t[1]

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"El promedio de las temperaturas mínimas es: {promedio_min:.2f} °C")
print(f"El promedio de las temperaturas máximas es: {promedio_max:.2f} °C")

mayor_amplitud = 0
dia_may_amplitud = 0

for i in range(len(temperaturas)):
    min_temp = temperaturas[i][0]
    max_temp = temperaturas[i][1]
    amplitud = max_temp - min_temp

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_may_amplitud = i + 1
print(f"Mayor amplitud térmica: {mayor_amplitud}°C (Día {dia_may_amplitud})")

#Ejercicio 8:
notas = [
    [5, 4, 8],
    [8, 10, 10],
    [4, 2, 1],
    [3, 8, 9],
    [9, 6, 7],
]

print("Promedios por estudiante: ")

for i in range(len(notas)):
    promedio = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i + 1}: {promedio:2f}")

suma_materias = [0, 0, 0]

