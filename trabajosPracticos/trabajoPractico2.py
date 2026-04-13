# 1.

# edad = int(input("Ingrese su edad: "))

# if edad > 18:
#     print("Eres mayor de edad.")

# 2.

# numero = int(input("Ingrese su nota (expresada en número/s): "))

# if numero >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# 3.

# numero = int(input("Ingrese un número: "))

# while numero % 2 != 0:
#     print("Por favor, ingrese un número par.")
#     numero = int(input("Ingrese otro número par: "))

# print("Correcto, el número es par.")

# 4.

# edad = int(input("Ingrese su edad: "))

# while edad < 0:
#     print("Edad inválida. Por favor, ingrese una edad válida.")
#     edad = int(input("Ingrese su edad: "))
# if edad < 12:
#     print("Es niño/a")
# elif edad >= 12 and edad < 18:
#     print("Es adolescente")
# elif edad >= 18 and edad < 30:
#     print("Es adulto/a joven")
# else:
#     print("Es adulto/a")

# 5-a.

# contraseña = input("Ingrese la contraseña: ").strip().lower()

# while len(contraseña) < 8 or len(contraseña) > 14:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
#     contraseña = input("Ingrese la contraseña nuevamente: ")

# print("Ha ingresado una contraseña correcta.")

# 5-b.

# contraseña = input("Ingrese la contraseña: ").strip().lower()

# if len(contraseña) <= 8 or len(contraseña) >= 14:
#     print("Contraseña inválida. Debe tener entre 8 y 14 caracteres.")
# else:
#     print("Contraseña válida.")

# 6.

# kWh = float(input("Ingrese el consumo mensual de kWh: "))

# while kWh < 0:
#     print("Por favor, ingrese un consumo válido.")
#     kWh = float(input("Ingrese el consumo mensual de kWh: "))

# if kWh < 150:
#     print("Consumo bajo.")
# elif kWh <= 300:
#     print("Consumo medio.")
# else:
#     print("Consumo alto.")

# if kWh > 500:
#     print("Considere medidas de ahorro energético.")

# 7.

# palabra = input("Ingrese una frase o palabra: ").strip().lower()
# vocales = "aeiouAEIOU"

# while len(palabra) < 0 or palabra.lstrip('-').isdigit():
#     print("Por favor, ingrese una frase o palabra válida.")
#     palabra = input("Ingrese una frase o palabra: ")

# if palabra[-1] in vocales:
#     palabra += "!"
#     print(f"La frase o palabra queda: {palabra}")
# else:
#     print(f"La frase o palabra es: {palabra}.")

# 8.

# nombre = input("Ingrese su nombre: ").strip().lower()
# opcion = int(input("Ingrese una opción (1, 2 o 3): "))

# match opcion:
#     case 1:
#         nombre_mayusculas = nombre.upper()
#         print(f"Tu nombre es: {nombre_mayusculas}")
#     case 2:
#         nombre_minusculas = nombre.lower()
#         print(f"Tu nombre es: {nombre_minusculas}")
#     case 3:
#         nombre_title = nombre.title()
#         print(f"Tu nombre es: {nombre_title}")
#     case _:
#         print("Opción no válida")

# 9.

# terremoto = float(input("Ingrese la magnitud del terremoto: "))

# while terremoto < 0:
#     print("Por favor, ingrese una magnitud válida.")
#     terremoto = float(input("Ingrese la magnitud del terremoto: "))

# if terremoto < 3:
#     print("Terremoto muy leve (imperceptible).")
# elif terremoto >= 3 and terremoto < 4:
#     print("Terremoto leve (ligeramente perceptible).")
# elif terremoto >= 4 and terremoto < 5:
#     print("Terremoto moderado (sentido por personas, pero generalmente no causa daños).")
# elif terremoto >= 5 and terremoto < 6:
#     print("Terremoto fuerte (puede causar daños en estructuras débiles).")
# elif terremoto >= 6 and terremoto < 7:
#     print("Terremoto muy fuerte (puede causar daños significativos).")
# else:
#     print("Terremoto extremo (puede causar graves daños a gran escala).")

# 10.

# hemisferio = input("Ingrese el hemisferio (N/S): ").strip().lower()
# h = hemisferio[0]

# mes = input("Ingrese el mes: ").strip().lower()
# dia = int(input("Ingrese el día: "))

# meses_validos = [
#     "enero", "febrero", "marzo", "abril", "mayo", "junio",
#     "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
# ]

# if mes not in meses_validos:
#     print("Mes no válido.")
# else:
#     validacion1 = (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia < 21)
#     validacion2 = (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia < 21)
#     validacion3 = (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia < 21)
#     validacion4 = (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia < 21)

#     if validacion1:
#         estacion = "invierno"
#     elif validacion2:
#         estacion = "primavera"
#     elif validacion3:
#         estacion = "verano"
#     elif validacion4:
#         estacion = "otoño"
#     else:
#         estacion = None

#     if estacion is None:
#         print("Fecha no válida.")
#     elif h == "n":
#         print(f"Es {estacion}.")
#     elif h == "s":
#         estaciones_opuestas = {
#             "invierno": "verano",
#             "verano": "invierno",
#             "primavera": "otoño",
#             "otoño": "primavera"
#         }
#         print(f"Es {estaciones_opuestas[estacion]}.")
#     else:
#         print("Hemisferio no válido.")
