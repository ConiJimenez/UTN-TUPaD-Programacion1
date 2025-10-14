# EJERCICIO N° 1:
def hola_mundo():
    return "Hola Mundo!"

print(hola_mundo())

# EJERCICIO N° 2:

# Definición de funciones: 
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa Principal:
nombre_ingresado = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_ingresado))

# EJERCICIO N° 3:

# Definición de funciones: 
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# Programa Principal:
nombre_ingresado = input("Ingrese su nombre: ")
apellido_ingresado = input("Ingrese su apellido: ")
edad_ingresada = input("Ingrese su edad: ")
residencia_ingresada = input("Ingrese su lugar de residencia: ")
print(informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada))
