# 1.

# precios_frutas = {
#     "Banana": 1200,
#     "Ananá": 2500,
#     "Melón": 3000,
#     "Uva": 1450
# }

# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(f"El set de precios de frutas es: {precios_frutas}")

# 2.

# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1500
# precios_frutas["Melón"] = 2800

# print(f"El set de precios de frutas actualizado es: {precios_frutas}")

# 3.

# frutas = []

# for i, j in precios_frutas.items():
#     frutas.append(i)

# print(f"La lista de frutas es: {frutas}")

# 4.

# contactos = {}

# for i in range(5):
#     nombre = input("Ingrese el nombre del contacto: ")
#     numero = input("Ingrese el número de teléfono: ")
#     contactos[nombre] = numero

# print(f"La agenda telefónica es: {contactos}")

# nombre_contacto = input("Ingrese el nombre del contacto que desea consultar: ")

# if nombre_contacto in contactos:
#     print(f"El número de teléfono de {nombre_contacto} es: {contactos[nombre_contacto]}")
# else:
#     print(f"No se encontró el contacto {nombre_contacto} en la agenda telefónica.")

# 5.

# import string

# frase = input("Ingrese una frase: ")

# frase_limpia = frase.lower().translate(str.maketrans('', '', string.punctuation)) # Se quitan los signos de puntuación y se convierte a minúscula para contar las palabras de manera uniforme

# palabras = frase_limpia.split()
# palabras_unicas = set(palabras)

# diccionario_palabras = {}

# for palabra in palabras:
#     diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1

# print("Palabras únicas:", palabras_unicas)
# print("Recuento:", diccionario_palabras)

# 6.

# alumnos = {}
# cantidad_total_alumnos = 3

# for i in range(cantidad_total_alumnos):
#     nombre = input("Ingrese el nombre del alumno: ")

#     nota1 = float(input("Ingrese la nota 1: "))
#     nota2 = float(input("Ingrese la nota 2: "))
#     nota3 = float(input("Ingrese la nota 3: "))

#     alumnos[nombre] = (nota1, nota2, nota3)

# print("Alumnos y sus notas:", alumnos)

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{nombre} tiene promedio: {promedio}")

# 7.

# asistencias = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Ana"]

# print("Lista original:", asistencias)

# asistentes_unicos = set(asistencias)
# print("Asistentes únicos:", asistentes_unicos)

# conteo = {}

# for nombre in asistencias:
#     conteo[nombre] = conteo.get(nombre, 0) + 1

# print("Cantidad de asistencias por persona:", conteo)

# 8.

# MENU = (
#     "\nOpciones disponibles:\n"
#     "1. Consultar stock\n"
#     "2. Agregar unidades a producto existente\n"
#     "3. Agregar nuevo producto\n"
#     "4. Salir\n"
# )

# stock_productos = {
#     "CPU": 50,
#     "Motherboard": 30,
#     "RAM": 200,
#     "GPU": 30,
#     "CASE": 100,
#     "PSU": 60
# }

# opcion = ""

# while opcion != "4":
#     print(MENU)
#     opcion = input("Seleccione una opción: ")

#     match opcion:
#         case "1":
#             producto = input("Indique el producto: ")
#             if producto in stock_productos:
#                 print(f"Stock de {producto}: {stock_productos[producto]}")
#             else:
#                 print("El producto no existe")

#         case "2":
#             producto = input("Indique el producto: ")
#             if producto in stock_productos:
#                 unidades = int(input("Unidades a agregar: "))
#                 stock_productos[producto] += unidades
#                 print("Stock actualizado")
#             else:
#                 print("El producto no existe")

#         case "3":
#             producto = input("Ingrese el nuevo producto: ")
#             if producto in stock_productos:
#                 print("El producto ya existe")
#             else:
#                 cantidad = int(input("Cantidad inicial: "))
#                 stock_productos[producto] = cantidad
#                 print("Producto agregado")

#         case "4":
#             print("Saliendo del programa...")

#         case _:
#             print("Opción inválida")

# 9.

# agenda = {
#     ("Lunes", "07:00"): "Reunión con el equipo",
#     ("Martes", "10:00"): "Clase de programación",
#     ("Miércoles", "15:00"): "Entrevista con el cliente",
#     ("Jueves", "12:00"): "Almuerzo con el equipo",
#     ("Viernes", "09:00"): "Revisión de proyectos",
# }

# dia = input("Ingrese el día de la semana: ").capitalize()
# hora = input("Ingrese la hora (formato HH:MM): ")

# clave = (dia, hora)

# if clave in agenda:
#     print(f"En {dia} a las {hora} tienes: {agenda[clave]}")
# else:
#     print(f"No hay eventos programados para {dia} a las {hora}.")

# 10.

# paises_capitales = {
#     "Argentina": "Buenos Aires",
#     "Francia": "París",
#     "Japón": "Tokio",
#     "Brasil": "Brasilia",
# }

# capitales_paises = {}

# for pais, capital in paises_capitales.items():
#     capitales_paises[capital] = pais

# print(f"Paises y capitales: {paises_capitales}")
# print(f"Capitales y paises: {capitales_paises}")
