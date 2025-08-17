#Todo el trabajo realizado
#Ejercicio 1: 

print("Hola mundo!")

#Ejercicio 2: 

nombre = input("Por favor, ingrese su nombre: ")

print(f"Hola {nombre}!")

#Ejercicio 3:

nombre = input("Por favor, escribe tu nombre: ")

apellido = input(f"Por favor {nombre}, escribe tu apellido: ")

edad = input(f"Por favor {nombre} {apellido}, escribe tu edad: ")

lugarDeResidencia = input(f"Por favor {nombre} {apellido}, escribe tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia} ")

#Ejercicio 4: 

radio = float(input("Ingrese el radio de un círculo: "))

pi = 3.14159

area = pi * radio * radio

print("El área del círculo es: ", area)

#Ejercicio 5: 

segundos = int(input("Ingrese a continuación los segundos que quiere pasar a horas: "))

hora = segundos / 3600

print(f" {segundos} segundos corresponden a  {hora} horas .")

#Ejercicio 6:

numero = int(input("A continuación ingrese un número entero: "))

Multiplicar1 = 1 * numero
Multiplicar2 = 2 * numero 
Multiplicar3 = 3 * numero 
Multiplicar4 = 4 * numero 
Multiplicar5 = 5 * numero 
Multiplicar6 = 6 * numero 
Multiplicar7 = 7 * numero
Multiplicar8 = 8 * numero
Multiplicar9 = 9 * numero
Multiplicar10 = 10 * numero

print(f"1 * {numero} = {Multiplicar1}")
print(f"2 * {numero} = {Multiplicar2}")
print(f"3 * {numero} = {Multiplicar3}")  
print(f"4 * {numero} = {Multiplicar4}")
print(f"5 * {numero} = {Multiplicar5}")
print(f"6 * {numero} = {Multiplicar6}")
print(f"7 * {numero} = {Multiplicar7}")
print(f"8 * {numero} = {Multiplicar8}")
print(f"9 * {numero} = {Multiplicar9}")
print(f"10 * {numero} = {Multiplicar10}")

#Ejercicio 7:

num1= int(input("Ingrese un número entero mayor a cero: "))

num2 = int(input("Ingrese otro número entero mayor a cero: "))

suma = num1 + num2

resta = num1 - num2

multiplicacion = num1 * num2

division = num1 / num2

print(f"La suma es igual a {suma}, la resta es igual a {resta}, la multiplicación es igual a {multiplicacion} y la división es igual a {division}  ")

#Ejercicio 8:

altura = float(input("Ingrese su altura en metros cuadrados: "))

peso = float(input("Ingrese su pes en kilogramos: "))

imc = peso / altura

print(f"Su índice de masa corporal es igual a {imc} ")

#Ejercicio 9:

tempCelsius = int(input("Ingrese la temperatura en grados celsius: "))

tempFarenheit = 9/5 * tempCelsius + 32

print(f"Los {tempCelsius} grados Celsius equivalen a {tempFarenheit} grados Farenheit.")

#Ejercicio 10:

num1 = float(input("Ingrese un primer número: "))
num2 = float(input("Ingrese un segundo número: "))
num3 = float(input("Ingrese un tercer número: "))

promedio = (num1 + num2 + num3) / 2

print(f"El promedio de los tres números es igual a {promedio}.")
