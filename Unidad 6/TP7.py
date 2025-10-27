#EJERCICIO 1:
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#EJERCICIO 2:

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#EJERCICIO 3: 
frutas = list(precios_frutas.keys())

print(frutas)

#EJERCICIO 4:
contactos = {}

for i in range(5):
    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese el número teléfonico: ")
   
    
    contacto = {"nombre": nombre, "telefono": telefono}

    contactos[nombre] = telefono

    print(contactos)

consulta_nombre = input("Ingrese el nombre que desea consultar: ")

#EJERCICIO 5:
frase = input("Ingresa una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print("\nPalabras únicas:")
print(palabras_unicas)

recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(recuento)

#EJERCICIO 6:
alumnos = {}

for i in range(3):
    nombre = input("Ingrese su nombre: ")

    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    notas = (nota1, nota2, nota3)

    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    
    total = 0 
    for nota in notas:
        total += nota

    promedio = total / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#EJERCICIO 7:
parcial1 = set()
parcial2 = set()

print("Ingrese los nombres de los alumnos que aprobaron el Parcial 1 (enter para terminar): ")
while True:
    alumno = input("Nombre del alumno: ")
    if alumno == "":
        break
    parcial1.add(alumno)

print("Ingrese los nombre de los alumnos que aprobaron el Parcial 2 (enter para terminar): ")
while True:
    alumno = input("Nombre del alumno: ")
    if alumno == "":
        break
    parcial2.add(alumno)

ambos = parcial1 & parcial2
print("Aprobó ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobó solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobó al menos un parcial de ambos:", al_menos_uno)

#EJERCICIO 8:
stock_mercaderia = {"aceite": 300, "fideos": 250, "coca-cola": 200}

#Consultar stock:
producto = input("Ingrese el producto a consultar: ")
print(stock_mercaderia.get(producto, "Producto no encontrado"))  

#Agregar unidades al stock si el producto ya existe:
producto_actualizar = input("Ingrese el producto a actualizar: ")
if producto_actualizar in stock_mercaderia:
    unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
    stock_mercaderia[producto_actualizar] += unidades
    print(f"Nuevo stock de {producto_actualizar}: {stock_mercaderia[producto_actualizar]}")
else:
    print("El producto no existe. Se puede agregar como nuevo.")

#Agregar nuevo producto si no existe:
nuevo_producto = input("Ingrese el nombre del nuevo producto que desea agregar: ")
if nuevo_producto not in stock_mercaderia:
    unidades = int(input("Ingrese la cantidad inicial de unidades: "))
    stock_mercaderia[nuevo_producto] = unidades
    print(f"Porducto {nuevo_producto} agregado con {unidades} unidades.")
else:
    print("El producto ya existe. Utilice opción de actualizar stock")

#Mostrar el stock final:
print("Stock final: ")
for nombre, cantidad in stock_mercaderia.items():
    print(f"{nombre}: {cantidad}")

#EJERCICIO 9:
agenda = {("Lunes", "10.00"): "Reunión con equipo", ("Martes", "13.00"): "Asistir a congreso", ("Viernes", "08.00"): "Ateneo de casos" }






#EJERCICIO 10:
