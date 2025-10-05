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


