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
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# Programa Principal:
nombre_ingresado = input("Ingrese su nombre: ")
apellido_ingresado = input("Ingrese su apellido: ")
edad_ingresada = input("Ingrese su edad: ")
residencia_ingresada = input("Ingrese su lugar de residencia: ")
print(informacion_personal(nombre_ingresado, apellido_ingresado, edad_ingresada, residencia_ingresada))

#EJERCICIO 4:

#Definición de funciones:
def calcular_area_circulo(radio):
    import math
    area = math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro

#Programa Principal:
radio = float(input(("Ingrese el radio del círculo: ")))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es igual a {area}")
print(f"El perímetro del círculo es igual a {perimetro}")

#EJERCICIO 5:

#Definición de funciones:
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#Programa Principal:

segundos = int(input("Ingrese la cantidad de segundos que desea pasar a horas: "))

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos son {horas} horas.")

#EJERCICIO 6:

#Definición de funciones:



#Programa Principal:

#EJERCICIO 7:

#Definición de funciones:



#Programa Principal:

#EJERCICIO 8:

#Definición de funciones:



#Programa Principal:

#EJERCICIO 9:

#Definición de funciones:



#Programa Principal:

#EJERCICIO 10:

#Definición de funciones:



#Programa Principal: