#Ejercicio 1:
edad = int (input("Ingrese su edad: "))
if edad >= 18:
    print ("Es mayor de edad")

#Ejercicio 2:
nota = int (input("Ingrese su nota: "))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#Ejercicio 3:
num = int (input("Ingrese un número: "))
if num % 2 == 0:
    print ("Ha ingresado un número par")
elif num % 2 != 0:
    print ("Por favor, ingrese un número par")

#Ejercicio 4:
edad = int (input("Ingrese su edad: "))
if edad < 12:
    print ("Usted es un/a niño/a")
elif edad >= 12 & edad < 18:
    print ("Usted es un/a adolescente")
elif edad >= 18 & edad < 30:
    print ("Usted es un adulto/a joven")
if edad >= 30:
    print ("Usted es un/a adulto/a")

#Ejercicio 5:
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6:
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if moda is None:
    print("No se puede determinar el sesgo porque no hay una única moda")
elif media > mediana > moda:
    print("Distribución con sesgo positivo (hacia la derecha)")
elif media < mediana < moda:
    print("Distribución con sesgo negativo (hacia la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("Distribución con forma indefinida")

#Ejercicio 7:
frase = input("Ingrese una frase o palabra: ")
if frase.endswith(('a', 'e', 'i', 'o', 'u')):
    frase += "!"
    print (frase)

#Ejercicio 8:
nombre = input("Ingrese su nombre: ")
num = input("Ingrese 1. Si quiere su nombre en mayúsculas. 2. Si quiere su nombre en minúsculas o 3. Si quiere su nombre con la primera letra mayúscula: ")
if num == "1":
    print("nombre.upper()")
elif num == "2":
    print("nombre.lower()")
elif num == "3":
    print("nombre.capitalize()")
else:
    print("Opción no válida.")
