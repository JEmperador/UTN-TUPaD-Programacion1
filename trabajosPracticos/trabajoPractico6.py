import math

# 1.

# def imprimir_hola_mundo():
#     print("Hola Mundo")


# imprimir_hola_mundo()

# 2.

# def saludar_usuario(nombre):
#     print(f"Hola, {nombre}!")


# saludar_usuario("Javier")

# 3.

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese su residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)

# 4.

# def calcular_area_circulo(radio):
#     area = math.pi * radio**2
#     return area


# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * math.pi * radio
#     return perimetro


# radio = float(input("Ingrese el radio del círculo: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5.

# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     return horas


# segundos = int(input("Ingrese la cantidad de segundos: "))

# horas = segundos_a_horas(segundos)

# print(f"La cantidad de horas es: {horas:.2f}")

# 6.

# def tabla_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")


# numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

# tabla_multiplicar(numero)

# 7.

# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b

#     if b != 0:
#         division = a / b
#     else:
#         division = "No se puede dividir por cero"

#     return suma, resta, multiplicacion, division


# a = float(input("Ingrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))

# suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# print(f"Suma: {suma:.2f}")
# print(f"Resta: {resta:.2f}")
# print(f"Multiplicación: {multiplicacion:.2f}")
# print(f"División: {division:.2f}")

# 8.

# def calcular_imc(peso, altura):
#     imc = peso / (altura**2)
#     return imc


# peso = float(input("Ingrese su peso en kilogramos: "))
# altura = float(input("Ingrese su altura en metros: "))

# imc = calcular_imc(peso, altura)

# print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# 9.

# def celsius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit


# celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

# 10.

# def calcular_promedio(a, b, c):
#     promedio = (a + b + c) / 3
#     return promedio


# a = float(input("Ingrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))
# c = float(input("Ingrese el tercer número: "))

# promedio = calcular_promedio(a, b, c)
# print(f"El promedio es: {promedio:.2f}")
