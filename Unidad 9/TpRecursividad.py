# EJERCICIO 1:
 
def factorial(n):
    if n == 1:        
        return 1
    else:               
        return n * factorial(n - 1)

num = int(input("Ingrese un número: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")

# EJERCICIO 2:

def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese un número: "))

for i in range(num + 1):
    print(fibonacci(i))

# EJERCICIO 3:
def potencia(base, exponente):
    if exponente == 0:   
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 5))

# EJERCICIO 4:
def decimal_a_binario(n):
    if n == 0:                 # Caso base
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(10))  

# Ejercicio 5:

def es_palindromo(palabra):
    if len(palabra) <= 1:        
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])  
        else:
            return False

print(es_palindromo("oso"))   
print(es_palindromo("hola"))  

# EJERCICIO 6:

def suma_digitos(n):
    if n < 10:             
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1234))  

# EJERCICIO 7:

def contar_bloques(n):
    if n == 1:             
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(4))   

# EJERCICIO 8:

def contar_digito(numero, digito):
    if numero == 0:        
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

print(contar_digito(12233421, 2))   