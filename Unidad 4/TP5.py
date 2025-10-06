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



