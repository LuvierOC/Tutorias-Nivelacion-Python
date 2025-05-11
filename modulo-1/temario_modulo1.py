# VARIABLES, TIPOS DE DATOS Y OPERADORES
nombre = "Carlos"
edad = 25
altura = 1.75
activo = True

print(type(nombre))

# Operadores aritméticos
suma = edad + 5
multiplicacion = edad * 2
division = altura / 2
modulo = edad % 2

# Operadores relacionales
es_mayor = edad > 18
es_igual = nombre == "Carlos"

# Operadores lógicos
es_valido = es_mayor and activo

print(f"Nombre: {nombre}, Edad futura: {suma}, ¿Es válido?: {es_valido}")

# ESTRUCTURAS DE CONTROL DE FLUJO
# Condicionales
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Bucles
print("Contando con for:")
for i in range(5):
    print(i)

print("Contando con while:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# FUNCIONES Y MODULARIDAD
def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

mensaje = saludar("Ana")
resultado_suma = sumar(10, 20)
print(mensaje)
print(f"Suma: {resultado_suma}")

# INTRODUCCIÓN A LISTAS, TUPLAS Y DICCIONARIOS
frutas = ["manzana", "pera", "uva"]
coordenadas = (10.5, 20.7)
persona = {"nombre": "Laura", "edad": 30}

print(frutas[0])
print(coordenadas[1])
print(persona["nombre"])

# MANIPULACIÓN DE ESTRUCTURAS DE DATOS BÁSICAS
frutas.append("banana")
persona["altura"] = 1.68
for fruta in frutas:
    print(f"Fruta: {fruta}")

# PROGRAMACIÓN FUNCIONAL BÁSICA
numeros = [1, 2, 3, 4, 5]

# lambda
cuadrado = list(map(lambda x: x**2, numeros))
print(f"Cuadrados: {cuadrado}")

# map
doble = list(map(lambda x: x * 2, numeros))
print(f"Dobles: {doble}")

# filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")

# reduce
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(f"Suma total: {suma_total}")
