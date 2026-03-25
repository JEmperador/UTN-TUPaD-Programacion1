import random

# 1

# listaNotas = [6, 8, 5, 10, 3, 1, 7, 2, 9, 4]
# alumno = 0
# mayorNota = listaNotas[0]
# menorNota = listaNotas[0]
# mejorAlumno = 0
# peorAlumno = 0

# print("\nLista completa")

# for i in listaNotas:
#     alumno += 1

#     print(f"Nota {alumno}: {i}")

# total = 0
# cantidad = len(listaNotas)

# for i in listaNotas:
#     total += i

# print(f"\nPromedio = {total/cantidad}")

# print(f"\nComparaciones")
# alumno = 0
# for i in listaNotas:
#     alumno += 1

#     if i > mayorNota:
#         mayorNota = i
#         mejorAlumno = alumno

#     if i < menorNota:
#         menorNota = i
#         peorAlumno = alumno

# print(f"\nMayor nota = {mayorNota}, del alumno {mejorAlumno}")
# print(f"\nMenor nota = {menorNota}, del alumno {peorAlumno}")

# ---

# Con un solo for

# listaNotas = [6, 8, 5, 10, 3, 1, 7, 2, 9, 4]

# mayorNota = listaNotas[0]
# menorNota = listaNotas[0]
# mejorAlumno = 1
# peorAlumno = 1

# total = 0

# print("Lista completa")

# for alumno, nota in enumerate(listaNotas, start=1):

#     print(f"Nota {alumno}: {nota}")

#     total += nota

#     if nota > mayorNota:
#         mayorNota = nota
#         mejorAlumno = alumno

#     if nota < menorNota:
#         menorNota = nota
#         peorAlumno = alumno

# cantidad = len(listaNotas)
# print(f"\nPromedio = {total/cantidad}\n")

# print("Comparaciones")
# print(f"Mayor nota = {mayorNota}, del alumno {mejorAlumno}")
# print(f"Menor nota = {menorNota}, del alumno {peorAlumno}")

# ---

# 2

# listaProductos = []
# totalProductos = 3

# for i in range(totalProductos):
#     producto = input("Ingrese un producto: ")
#     listaProductos.append(producto)

# listaProductos.sort()
# print(f"\nLista ordenada: {listaProductos}")

# producto = input("\nElimine un producto por su nombre: ")

# if producto in listaProductos:
#     listaProductos.remove(producto)
#     print("\nLista actualizada:", listaProductos)
# else:
#     print("El producto no existe en la lista")

# ---

# 3

# inicioValido = 1
# finValido = 100
# cantidad = 15

# listaAleatoria = random.sample(range(inicioValido, finValido + 1), cantidad)
# listaPares = []
# listaImpares = []

# for numero in listaAleatoria:
#     if numero % 2 == 0:
#         listaPares.append(numero)
#     else:
#         listaImpares.append(numero)

# print(f"Lista completa: {listaAleatoria}\n")
# print(f"Pares ({len(listaPares)}): {listaPares}\n")
# print(f"Impares ({len(listaImpares)}): {listaImpares}\n")

# ---

# 4

# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# datosSinRepeticion = list(set(datos))

# print(f"Resultado: {datosSinRepeticion}")

# ---

# 5

# estudiantes = ["Marco", "Eren", "Zeke", "Grisha", "Mikasa", "Armin", "Levi", "Ymir"]

# print(f"Estudiantes: {estudiantes}")

# opcion = int(input("Seleccione una opcion (0: Eliminar /1: Agregar) estudiante: "))

# while opcion > 1 or opcion < 0:
#     opcion = int(
#         input("Seleccione una opcion valida, (0: Eliminar /1: Agregar) estudiante: ")
#     )

# opcion = int(opcion)

# match opcion:
#     case 0:
#         estudiante = input("\nElimine un estudiante por su nombre: ")

#         if estudiante in estudiantes:
#             estudiantes.remove(estudiante)
#             print("\nLista de estudiantes actualizada:", estudiantes)
#         else:
#             print("El estudiante no esta en la lista")
#     case 1:
#         estudiante = input("\nAgregue un estudiante por su nombre: ")

#         if estudiante in estudiantes:
#             print("El estudiante esta en la lista")
#         else:
#             estudiantes.append(estudiante)
#             print("\nLista de estudiantes actualizada:", estudiantes)

# ---

# 6

# lista = [0, 1, 2, 3, 4, 5, 6]

# posicion = -1

# print(f"Lista: {lista}")

# ultimoValor = lista[posicion]

# lista.pop(posicion)  # No es necesario el -1 pero es mas facil de leer

# lista.insert(0, ultimoValor)

# print(f"\nLista actualizada {lista}")

# ---

# En una linea

# print(f"Lista: {lista}")

# lista.insert(0, lista.pop())

# print(f"Lista: {lista}")

# ---

# 7

# minimas = 0
# maximas = 0

# mayorAmplitud = -1
# diaMayor = 0

# matrizTemperaturas = [
#     [20, 15],
#     [18, 12],
#     [25, 18],
#     [10, 8],
#     [10, 5],
#     [18, 8],
#     [20, 10],
# ]

# for fila in matrizTemperaturas:
#     maximas += fila[0]
#     minimas += fila[1]

# promedioMaximas = maximas / len(matrizTemperaturas)
# promedioMinimas = minimas / len(matrizTemperaturas)

# for i in range(len(matrizTemperaturas)):
#     maxima = matrizTemperaturas[i][0]
#     minima = matrizTemperaturas[i][1]

#     amplitud = maxima - minima

#     if amplitud > mayorAmplitud:
#         mayorAmplitud = amplitud
#         diaMayor = i + 1

# print(f"promedio de temperaturas máximas: {promedioMaximas}")
# print(f"Promedio de temperaturas mínimas: {promedioMinimas}")
# print(f"Mayor amplitud {mayorAmplitud} el dia {diaMayor}")

# ---

# Con un solo for

# mayorAmplitud = -1
# diaMayor = 0

# sumaMaximas = 0
# sumaMinimas = 0

# matrizTemperaturas = [
#     [20, 15],
#     [18, 12],
#     [25, 18],
#     [10, 8],
#     [10, 5],
#     [18, 8],
#     [20, 10],
# ]

# for i in range(len(matrizTemperaturas)):
#     maxima = matrizTemperaturas[i][0]
#     minima = matrizTemperaturas[i][1]

#     sumaMaximas += maxima
#     sumaMinimas += minima

#     amplitud = maxima - minima

#     if amplitud > mayorAmplitud:
#         mayorAmplitud = amplitud
#         diaMayor = i + 1

# promedioMaximas = sumaMaximas / len(matrizTemperaturas)
# promedioMinimas = sumaMinimas / len(matrizTemperaturas)

# print(f"Promedio de temperaturas máximas: {promedioMaximas}")
# print(f"Promedio de temperaturas mínimas: {promedioMinimas}")
# print(f"Mayor amplitud {mayorAmplitud} el día {diaMayor}")

# ---

# 8

# cabeceraMaterias = ["Programación", "Matemática", "Arquitectura"]

# matrizNotas = [
#     [10, 7, 9],  # 1
#     [8, 6, 7],   # 2
#     [6, 8, 10],  # 3
#     [7, 10, 8],  # 4
#     [9, 8, 9],   # 5
# ]

# for i, fila in enumerate(matrizNotas):
#     promedio = sum(fila) / len(fila)
#     print(f"Estudiante {i + 1}, promedio general: {promedio:.2f}")

# for j in range(len(cabeceraMaterias)):
#     suma = 0

#     for i in range(len(matrizNotas)):
#         suma += matrizNotas[i][j]

#     promedio = suma / len(matrizNotas)
#     print(f"Promedio de {cabeceraMaterias[j]}: {promedio:.2f}")

# ---

# 9

# turno = False

# tableroTateti = [
#     ["-", "-", "-"],
#     ["-", "-", "-"],
#     ["-", "-", "-"],
# ]

# print("Este juego es TA-TE-TI...\n")

# jugadorUno = input("Jugador 1 ingrese su nombre: ")
# jugadorDos = input("Jugador 2 ingrese su nombre: ")

# while True:

#     for fila in tableroTateti:
#         print(" ".join(fila))

#     if turno == False:
#         jugadorActual = jugadorUno
#         simbolo = "X"
#     else:
#         jugadorActual = jugadorDos
#         simbolo = "O"

#     print(f"\nTurno de {jugadorActual} ({simbolo})")

#     fila = int(input("Ingrese fila (1-3): ")) - 1
#     columna = int(input("Ingrese columna (1-3): ")) - 1

#     if tableroTateti[fila][columna] == "-":
#         tableroTateti[fila][columna] = simbolo
#         turno = not turno
#     else:
#         print("Casilla ocupada, intente de nuevo")

# ---

# 10

# ventas = [
#     [10, 5, 8, 7, 6, 9, 4],
#     [3, 6, 2, 5, 7, 0, 6],
#     [9, 8, 7, 6, 5, 4, 3],
#     [4, 3, 5, 6, 7, 8, 9]
# ]

# dias = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]

# print("Total por producto:")
# for i, producto in enumerate(ventas):
#     total = sum(producto)
#     print(f"Producto {i + 1}: {total}")

# totalesDias = []

# for j in range(len(dias)):
#     totalDia = sum(ventas[i][j] for i in range(len(ventas)))
#     totalesDias.append(totalDia)

# diaMax = totalesDias.index(max(totalesDias))
# print(f"\nDía con más ventas: {dias[diaMax]} ({totalesDias[diaMax]})")

# print("\nVentas por día:")
# for i, total in enumerate(totalesDias):
#     print(f"{dias[i]}: {total}")

# totalesProductos = [sum(producto) for producto in ventas]
# productoMax = totalesProductos.index(max(totalesProductos))

# print(f"\nProducto más vendido: Producto {productoMax + 1} ({totalesProductos[productoMax]})")

# ---

# 11

# estudiantes = [
#     "Marco",
#     "Eren",
#     "Zeke",
#     "Grisha",
#     "Mikasa",
#     "Armin",
#     "Levi",
#     "Ymir",
#     "Historia",
#     "Annie",
# ]

# print(f"Estudiantes: {estudiantes}")

# estudiante = input("\nIngrese el nombre de un estudiante a buscar: ")

# if estudiante in estudiantes:
#     posicion = estudiantes.index(estudiante)
#     print(
#         f"\nEl estudiante {estudiante} se encuentra en la lista en la posición {posicion}"
#     )
# else:
#     print("\nEl estudiante no se encuentra en la lista")

# ---

# 12

# numeros = []
# cantidad = 8
# contador = 1

# while contador <= cantidad:
#     numero = int(input("Ingrese un numero entero: "))
#     numeros.append(numero)
#     contador += 1

# numerosMenorAMayor = sorted(numeros)
# numerosMayorAMenor = sorted(numeros, reverse=True)

# print("\nLista original:", numeros)
# print(f"\nMenor a mayor: {numerosMenorAMayor}")
# print(f"\nMayor a menor: {numerosMayorAMenor}")

# ---

# 13

# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# mayorPuntaje = puntajes[0]
# menorPuntaje = puntajes[0]
# valorBusqueda = 990

# for i in puntajes:
#     if i > mayorPuntaje:
#         mayorPuntaje = i

#     if i < menorPuntaje:
#         menorPuntaje = i

# ranking = sorted(puntajes, reverse=True)

# if i in ranking:
#     posicion = ranking.index(valorBusqueda)

# print(f"\nMayor puntaje: {mayorPuntaje}")
# print(f"\nMenor puntaje: {menorPuntaje}")
# print(f"\nRanking: {ranking}")
# print(f"\nEl puntaje 990 esta en la posición: {posicion}")
