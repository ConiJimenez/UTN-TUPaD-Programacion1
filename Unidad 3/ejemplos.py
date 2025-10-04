#cant_personas = int(input("Ingrese una cantidad de personas: "))
#EDAD_MINIMA = 18
#cant_personas_mayores = 0

#for cont in range (cant_personas):
 #   print("Ingrese la edad n°",(cont+1))
  #  edad = int(input())
   # if edad >= EDAD_MINIMA:
        #cant_personas_mayores = cant_personas_mayores + 1
    #    cant_personas_mayores += 1

#porc = (cant_personas_mayores / cant_personas) * 100
#print("El porcentaje de personas mayores de edad es", porc)
# FIN

#CORTE = "*" 
#NOMBRE_INVALIDO = "XXXXXXXXX"
#edad_minima = float("inf")
#nombre_mas_joven = NOMBRE_INVALIDO

#nombre = input("Ingrese un nombre (" + CORTE + " para cortar): ")

#while nombre != CORTE:
    #edad = int(input("Ingrese la edad de " + nombre + ": "))
    #if edad < edad_minima:
    #    edad_minima = edad
   #     nombre_mas_joven = nombre
  #  nombre = input("Ingrese otro nombre (" + CORTE + " para cortar): ")

#if nombre_mas_joven == NOMBRE_INVALIDO:
 #   print("No se ingresaron personas")
#else:    
 #   print("La persona más joven (",edad_minima," años) es",nombre_mas_joven)
#FIN

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
    
a = float(input("Ingrese un primer número entero: "))
b = float(input("Ingrese un segundo número entero: "))

resultado = operaciones_basicas(a, b)

if resultado:
    suma, resta, multiplicacion, division = resultado     
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} * {b} = {multiplicacion}")
    print(f"{a} / {b} = {division}")
