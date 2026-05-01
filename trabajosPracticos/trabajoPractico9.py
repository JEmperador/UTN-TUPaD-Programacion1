import os

NOMBRE_ARCHIVO = "productos.txt"

# Funciones

# def crear_archivo(nombre_archivo):
#     if not os.path.exists(nombre_archivo):
#         with open(nombre_archivo, "w") as archivo:
#             archivo.write("Lapicera,120.5,30\n")
#             archivo.write("Cuaderno,350.0,15\n")
#             archivo.write("Regla,80.0,25\n")
#         print(f"Archivo '{nombre_archivo}' creado con productos iniciales.")
#     else:
#         print(f"El archivo '{nombre_archivo}' ya existe. No se sobreescribió.")


# def mostrar_productos(nombre_archivo):
#     with open(nombre_archivo, "r") as archivo:
#         for linea in archivo:
#             nombre, precio, cantidad = linea.strip().split(",")
#             print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# def agregar_producto(nombre_archivo, nombre, precio, cantidad):
#     with open(nombre_archivo, "a") as archivo:
#         archivo.write(f"{nombre},{precio},{cantidad}\n")
#     print(f"Producto '{nombre}' agregado correctamente.")


# def cargar_productos(nombre_archivo):
#     productos = []
#     with open(nombre_archivo, "r") as archivo:
#         for linea in archivo:
#             nombre, precio, cantidad = linea.strip().split(",")
#             productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
#     return productos


# def buscar_producto(productos, nombre_busqueda):
#     producto_encontrado = False
#     for producto in productos:
#         if producto["nombre"].lower() == nombre_busqueda.lower():
#             print(f"Producto encontrado:")
#             print(f"  Nombre   : {producto['nombre']}")
#             print(f"  Precio   : ${producto['precio']}")
#             print(f"  Cantidad : {producto['cantidad']}")
#             producto_encontrado = True
#     if not producto_encontrado:
#         print(f"Error: El producto '{nombre_busqueda}' no existe en el catálogo.")


# def guardar_productos(nombre_archivo, productos):
#     with open(nombre_archivo, "w") as archivo:
#         for producto in productos:
#             archivo.write(
#                 f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
#             )
#     print(f"Archivo '{nombre_archivo}' actualizado correctamente.")


# def separador(signo, longitud):
#     separador = signo * longitud
#     return separador


# 1.

# crear_archivo(NOMBRE_ARCHIVO)

# mostrar_productos(NOMBRE_ARCHIVO)


# 2.

# print(f"\n{separador('-', 3)} Productos en el archivo {separador('-', 3)} ")
# mostrar_productos(NOMBRE_ARCHIVO)


# 3.

# print(f"\n{separador('-', 3)} Agregar nuevo producto {separador('-', 3)}")
# nombre_nuevo = input("Ingrese el nombre del producto: ")
# precio_nuevo = input("Ingrese el precio del producto: ")
# cantidad_nueva = input("Ingrese la cantidad del producto: ")

# agregar_producto(NOMBRE_ARCHIVO, nombre_nuevo, precio_nuevo, cantidad_nueva)

# print(f"\n{separador('-', 3)} Productos actualizados {separador('-', 3)}")
# mostrar_productos(NOMBRE_ARCHIVO)


# 4.

# productos = cargar_productos(NOMBRE_ARCHIVO)
# print(f"\n{separador('-', 3)} {len(productos)} productos cargados en memoria {separador('-', 3)}")


# 5.

# print(f"\n{separador('-', 3)} Buscar producto {separador('-', 3)}")
# nombre_busqueda = input("Ingrese el nombre del producto a buscar: ")
# buscar_producto(productos, nombre_busqueda)


# 6.

# guardar_productos(NOMBRE_ARCHIVO, productos)

# print(f"\n{separador('-', 3)} Contenido final del archivo {separador('-', 3)}")
# mostrar_productos(NOMBRE_ARCHIVO)
