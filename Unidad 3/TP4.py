# Ejercicio 1:
i = 0

while i <= 100:
    print(i)
    i += 1

# Ejercicio 2:
num = input("Ingrese un número entero: ")


numero_entero = int(num)
if numero_entero < 0:
    numero_entero = -numero_entero
else:
    print("Entrada inválida. Debe ingresar un número entero.")

cantidad_digitos = len(str(numero_entero))
print("El número tiene", cantidad_digitos, "digito(s).")

#Ejercicio 3:
num_inicial = int(input("Ingrese el primer número: "))
num_final = int(input("Ingrese el segundo número: "))

if num_inicial > num_final:
    num_inicial, num_final = num_final, num_inicial

suma = 0

for i in range(num_inicial + 1, num_final):
    suma += i

print("La suma de los dos números enteros entre", num_inicial, "y", num_final, "es:", suma)

#Ejercicio 4:
suma = 0
num = int(input("Ingrese un número entero (0 para terminar): "))

while True:
    num = int(input("Ingrese otro número entero (0 para terminar): "))
    if num == 0:
        break
suma += num

print("La suma total es:", suma)

#Ejercicio 5:
numSecreto = 7
intentos = 0
print("Adivina el número entre 0 y 9")

while True: 
    numUsuario = int(input("Ingresa tu intento: "))
    intentos += 1

    if numUsuario == numSecreto:
        print("Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

#Ejercicio 6:
for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)
    
#Ejercicio 7:
numero = int(input("Ingresa un número entero positivo: "))

if numero >= 0:
    suma = 0
    for i in range(0, numero + 1):
        suma += i
    print("La suma de los números entre 0 y", numero, "es:", suma)
else:
    print("El número debe ser positivo.")

#Ejercicio 8:
totalNumeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(totalNumeros):
    numero = int(input("Ingresa un número entero (" + str(i + 1) + "/" + str(totalNumeros) + "): "))
    
    if numero % 2 == 0:
        pares += 1
    else: 
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1


#Ejercicio 9:

#Ejercicio 10:
