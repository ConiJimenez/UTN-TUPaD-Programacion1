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