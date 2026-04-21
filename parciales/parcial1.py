# herramientas = []
# existencias = []

# OPCION_SALIR = 8

# MENU = (
#     "\nOpciones disponibles:\n"
#     "1. Carga Inicial de Herramientas\n"
#     "2. Carga de Existencias\n"
#     "3. Visualización de Inventario\n"
#     "4. Consulta de Stock (existencias)\n"
#     "5. Reporte de Agotados\n"
#     "6. Alta de Nuevo Producto\n"
#     "7. Actualización de Stock (Venta/Ingreso)\n"
#     "8. Salir\n"
#     "Seleccione una opción: "
# )

# opcion_string = input(MENU)

# while not opcion_string.isdigit() or int(opcion_string) not in range(1, OPCION_SALIR + 1):
#     print("\nError: Opción no válida.\nIngrese un número entre 1 y 8.")
#     opcion_string = input(MENU)
# opcion = int(opcion_string)

# while opcion != OPCION_SALIR:

#     if opcion == 1:

#         print("\nSelecciono la opción 1 - Carga Inicial de Herramientas")
#         cantidad_string = input("Ingrese la cantidad de herramientas a cargar: ")

#         while not cantidad_string.isdigit() or int(cantidad_string) <= 0:
#             print("Error: Opción no válida.\nIngrese un número entero positivo.")
#             cantidad_string = input("Ingrese la cantidad de herramientas a cargar: ")
#         cantidad = int(cantidad_string)

#         for i in range(cantidad):
#             nombre = input("Ingrese el nombre de la herramienta: ")

#             while nombre == "" or nombre in herramientas:
#                 if nombre == "":
#                     print("Error: El nombre no puede estar vacío.\nIntente nuevamente.")

#                 else:
#                     print("Error: El nombre ya existe.\nIntente nuevamente.")

#                 nombre = input("Ingrese el nombre de la herramienta: ")
            
#             herramientas.append(nombre)
#             existencias.append(0)

#     elif opcion == 2:

#         print("\nSelecciono la opción 2 - Carga de Existencias")

#         if len(herramientas) == 0:
#             print("Error: No hay herramientas cargadas.\nPor favor, cargue las herramientas primero.")

#         else:
#             for i in range(len(herramientas)):
#                 cantidad_existencias = input(f"Ingrese la cantidad de existencias para {herramientas[i]}: ")

#                 while not cantidad_existencias.isdigit() or int(cantidad_existencias) < 0:
#                     print("Error: Opción no válida.\nIngrese un número entero positivo o cero.")
#                     cantidad_existencias = input(f"Ingrese la cantidad de existencias para {herramientas[i]}: ")
#                 existencias[i] = int(cantidad_existencias)

#     elif opcion == 3:

#         print("\nSelecciono la opción 3 - Visualización de Inventario")

#         if len(herramientas) == 0:
#             print("Error: No hay herramientas cargadas en el inventario.")

#         else:
#             print("Inventario Actual:")

#             for i in range(len(herramientas)):
#                 print(f"  {herramientas[i]}: {existencias[i]} unidades")

#     elif opcion == 4:

#         print("\nSelecciono la opción 4 - Consulta de Stock (existencias)")
#         nombre_consulta = input("Ingrese el nombre de la herramienta a consultar: ")

#         if nombre_consulta in herramientas:
#             index = herramientas.index(nombre_consulta)
#             print(f"{herramientas[index]} tiene {existencias[index]} unidades disponibles.")
#         else:
#             print("Error: La herramienta no existe en el catálogo.")

#     elif opcion == 5:

#         print("\nSelecciono la opción 5 - Reporte de Agotados")
#         hay_agotados = False

#         for i in range(len(herramientas)):
#             if existencias[i] == 0:
#                 print(f"  {herramientas[i]} está agotado.")
#                 hay_agotados = True
        
#         if not hay_agotados:
#             print("No hay productos agotados.\nVolviendo al menú principal.")

#     elif opcion == 6:

#         print("\nSelecciono la opción 6 - Alta de Nuevo Producto")
#         nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")

#         if nuevo_nombre == "":
#             print("Error: El nombre no puede estar vacío.\nVolviendo al menú principal.")
        
#         elif nuevo_nombre in herramientas:
#             print("Error: El nombre ya existe.\nVolviendo al menú principal.")

#         else:
#             nuevo_stock = input("Ingrese el stock inicial del nuevo producto: ")

#             if not nuevo_stock.lstrip("-").isdigit() or int(nuevo_stock) < 0:
#                 print("Error: El stock debe ser un número entero positivo o cero.\nVolviendo al menú principal.")
            
#             else:
#                 herramientas.append(nuevo_nombre)
#                 existencias.append(int(nuevo_stock))
#                 print(f"Producto '{nuevo_nombre}' agregado con {nuevo_stock} unidades.")

#     elif opcion == 7:

#         print("\nSelecciono la opción 7 - Actualización de Stock (Venta/Ingreso)")
#         nombre_producto = input("Ingrese el nombre del producto para actualizar el stock: ")

#         if nombre_producto in herramientas:
#             index = herramientas.index(nombre_producto)
#             tipo_actualizacion = input("¿Desea realizar una venta (V) o un ingreso (I)? ").upper()

#             if tipo_actualizacion == "V":
#                 cantidad_venta = input("Ingrese la cantidad a vender: ")
#                 while not cantidad_venta.isdigit() or int(cantidad_venta) <= 0:
#                     print("Error: Opción no válida.\nIngrese un número entero positivo.")
#                     cantidad_venta = input("Ingrese la cantidad a vender: ")
                    
#                 if int(cantidad_venta) > existencias[index]:
#                     print("Error: No hay suficientes unidades para realizar la venta.\nVolviendo al menú principal.")

#                 else:
#                     existencias[index] -= int(cantidad_venta)
#                     print(f"Venta realizada. Stock actualizado de {herramientas[index]}: {existencias[index]} unidades.")

#             elif tipo_actualizacion == "I":
#                 cantidad_ingreso = input("Ingrese la cantidad a ingresar: ")
                
#                 while not cantidad_ingreso.isdigit() or int(cantidad_ingreso) <= 0:
#                     print("Error: Opción no válida.\nIngrese un número entero positivo.")
#                     cantidad_ingreso = input("Ingrese la cantidad a ingresar: ")
#                 existencias[index] += int(cantidad_ingreso)
#                 print(f"Ingreso realizado. Stock actualizado de {herramientas[index]}: {existencias[index]} unidades.")

#             else:
#                 print("Error: Opción de actualización no válida.\nVolviendo al menú principal.")
#         else:
#             print("Error: La herramienta no existe en el catálogo.")

#     opcion_string = input(MENU)
#     while not opcion_string.isdigit() or int(opcion_string) not in range(1, OPCION_SALIR + 1):
#         print("Error: Opción no válida.\nIngrese un número entre 1 y 8.")
#         opcion_string = input(MENU)
#     opcion = int(opcion_string)

# print("\nSelecciono la opción 8 - Salir")
# print("Gracias por usar el sistema de control de inventario. ¡Hasta luego!")