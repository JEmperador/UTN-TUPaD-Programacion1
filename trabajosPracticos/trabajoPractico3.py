# 1.

# nombre = input("Ingrese su nombre: ").strip()

# while not nombre.isalpha():
#     print("Error: Nombre invalido. Solo debe contener letras.")
#     nombre = input("Ingrese su nombre: ").strip()


# cantidad = input("Ingrese la cantidad de productos que desea comprar: ")

# while not cantidad.isdigit() or int(cantidad) <= 0:
#     print("Error: Cantidad invalida. Debe ser un número entero positivo.")
#     cantidad = input("Ingrese la cantidad de productos que desea comprar: ").strip()

# totalSinDescuento = 0
# totalConDescuento = 0

# for i in range(1, int(cantidad) + 1):
#     precio = input(f"Producto {i} - Precio: ")

#     while not precio.isdigit() or int(precio) <= 0:
#         print("Error: Precio invalido. Debe ser un número entero positivo.")
#         precio = input(f"Producto {i} - Precio: ").strip()

#     descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()

#     while descuento not in ["s", "n"]:
#         print("Error: Descuento invalido. Debe ser 'S' o 'N'.")
#         descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()

#     precio = int(precio)
#     totalSinDescuento += precio

#     if descuento == "s":
#         precioConDescuento = precio * 0.9
#         totalConDescuento += precioConDescuento
#     else:
#         totalConDescuento += precio

# ahorro = totalSinDescuento - totalConDescuento
# promedio = totalConDescuento / int(cantidad)

# print("\n--- Resumen ---")
# print(f"Cliente: {nombre}")
# print(f"Cantidad de productos: {cantidad}")
# print(f"Total sin descuentos: ${totalSinDescuento}")
# print(f"Total con descuentos: ${totalConDescuento:.2f}")
# print(f"Ahorro: ${ahorro:.2f}")
# print(f"Promedio por producto: ${promedio:.2f}")

# 2.

# usuarioValido = "alumno"
# claveValida = "python123"

# intentos = 0
# limiteIntentos = 3
# acceso = False

# while intentos < limiteIntentos:
#     print(f"Intento {intentos + 1}/{limiteIntentos}")
#     usuario = input("Usuario: ").strip()
#     clave = input("Clave: ").strip()

#     if usuario == usuarioValido and clave == claveValida:
#         print("Acceso concedido.")
#         acceso = True
#         break
#     else:
#         print("Error: credenciales inválidas.")
#         intentos += 1

# if not acceso:
#     print("Cuenta bloqueada.")
# else:
#     while True:
#         print("\n1. Estado  2. Cambiar clave  3. Mensaje  4. Salir")
#         opcion = input("Opción: ").strip()

#         if not opcion.isdigit():
#             print("Error: ingrese un número válido.")
#             continue

#         opcion = int(opcion)

#         if opcion < 1 or opcion > 4:
#             print("Error: opción fuera de rango.")
#             continue

#         match opcion:
#             case 1:
#                 print("Estado: Inscripto")

#             case 2:
#                 nuevaClave = input("Nueva clave: ").strip()

#                 if len(nuevaClave) < 6:
#                     print("Error: mínimo 6 caracteres.")
#                     continue

#                 confirmacion = input("Confirmar clave: ").strip()

#                 if nuevaClave != confirmacion:
#                     print("Error: las claves no coinciden.")
#                     continue

#                 claveValida = nuevaClave
#                 print("Clave cambiada correctamente.")

#             case 3:
#                 print("¡Seguí adelante, vas bien!")

#             case 4:
#                 print("Saliendo del programa...")
#                 break

# 3.

# operador = input("Ingrese nombre del operador: ").strip()

# while not operador.isalpha():
#     print("Error: Nombre inválido.")
#     operador = input("Ingrese nombre del operador: ").strip()

# lunes1 = lunes2 = lunes3 = lunes4 = ""
# martes1 = martes2 = martes3 = ""

# while True:
#     print("\n1. Reservar\n2. Cancelar\n3. Ver agenda\n4. Resumen\n5. Salir")
#     opcion = input("Opción: ").strip()

#     if not opcion.isdigit():
#         print("Error: ingrese un número válido.")
#         continue

#     opcion = int(opcion)

#     if opcion < 1 or opcion > 5:
#         print("Error: opción fuera de rango.")
#         continue

#     if opcion == 1:
#         dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         while not dia.isdigit() or int(dia) not in [1, 2]:
#             print("Día inválido.")
#             dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         dia = int(dia)

#         nombre = input("Nombre del paciente: ").strip()

#         while not nombre.isalpha():
#             print("Error: Nombre inválido.")
#             nombre = input("Nombre del paciente: ").strip()

#         if dia == 1:
#             if nombre in [lunes1, lunes2, lunes3, lunes4]:
#                 print("Paciente ya registrado en Lunes.")
#             elif lunes1 == "":
#                 lunes1 = nombre
#                 print("Turno reservado en Lunes.")
#             elif lunes2 == "":
#                 lunes2 = nombre
#                 print("Turno reservado en Lunes.")
#             elif lunes3 == "":
#                 lunes3 = nombre
#                 print("Turno reservado en Lunes.")
#             elif lunes4 == "":
#                 lunes4 = nombre
#                 print("Turno reservado en Lunes.")
#             else:
#                 print("No hay cupos disponibles en Lunes.")
#         else:
#             if nombre in [martes1, martes2, martes3]:
#                 print("Paciente ya registrado en Martes.")
#             elif martes1 == "":
#                 martes1 = nombre
#                 print("Turno reservado en Martes.")
#             elif martes2 == "":
#                 martes2 = nombre
#                 print("Turno reservado en Martes.")
#             elif martes3 == "":
#                 martes3 = nombre
#                 print("Turno reservado en Martes.")
#             else:
#                 print("No hay cupos disponibles en Martes.")

#     elif opcion == 2:
#         dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         while not dia.isdigit() or int(dia) not in [1, 2]:
#             print("Día inválido.")
#             dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         dia = int(dia)

#         nombre = input("Nombre del paciente: ").strip()

#         while not nombre.isalpha():
#             print("Nombre inválido.")
#             nombre = input("Nombre del paciente: ").strip()

#         encontrado = False

#         if dia == 1:
#             if lunes1 == nombre:
#                 lunes1 = ""
#                 encontrado = True
#             elif lunes2 == nombre:
#                 lunes2 = ""
#                 encontrado = True
#             elif lunes3 == nombre:
#                 lunes3 = ""
#                 encontrado = True
#             elif lunes4 == nombre:
#                 lunes4 = ""
#                 encontrado = True
#         else:
#             if martes1 == nombre:
#                 martes1 = ""
#                 encontrado = True
#             elif martes2 == nombre:
#                 martes2 = ""
#                 encontrado = True
#             elif martes3 == nombre:
#                 martes3 = ""
#                 encontrado = True

#         if encontrado:
#             print("Turno cancelado.")
#         else:
#             print("Paciente no encontrado.")

#     elif opcion == 3:
#         dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         while not dia.isdigit() or int(dia) not in [1, 2]:
#             print("Día inválido.")
#             dia = input("Día (1=Lunes, 2=Martes): ").strip()

#         dia = int(dia)

#         if dia == 1:
#             print("\nAgenda Lunes")
#             print(f"1: {lunes1 if lunes1 else '(libre)'}")
#             print(f"2: {lunes2 if lunes2 else '(libre)'}")
#             print(f"3: {lunes3 if lunes3 else '(libre)'}")
#             print(f"4: {lunes4 if lunes4 else '(libre)'}")
#         else:
#             print("\nAgenda Martes")
#             print(f"1: {martes1 if martes1 else '(libre)'}")
#             print(f"2: {martes2 if martes2 else '(libre)'}")
#             print(f"3: {martes3 if martes3 else '(libre)'}")

#     elif opcion == 4:
#         ocupadosLunes = 0
#         ocupadosMartes = 0

#         if lunes1:
#             ocupadosLunes += 1
#         if lunes2:
#             ocupadosLunes += 1
#         if lunes3:
#             ocupadosLunes += 1
#         if lunes4:
#             ocupadosLunes += 1

#         if martes1:
#             ocupadosMartes += 1
#         if martes2:
#             ocupadosMartes += 1
#         if martes3:
#             ocupadosMartes += 1

#         print("\nResumen:")
#         print(f"Lunes  → Ocupados: {ocupadosLunes} | Libres: {4 - ocupadosLunes}")
#         print(f"Martes → Ocupados: {ocupadosMartes} | Libres: {3 - ocupadosMartes}")

#         if ocupadosLunes > ocupadosMartes:
#             print("Día con más turnos: Lunes")
#         elif ocupadosMartes > ocupadosLunes:
#             print("Día con más turnos: Martes")
#         else:
#             print("Empate en cantidad de turnos.")

#     elif opcion == 5:
#         print("Sistema cerrado.")
#         break

# 4.

# energia = 100
# tiempo = 12
# cerradurasAbiertas = 0
# alarma = False
# codigoParcial = ""
# rachaForzar = 0

# nombre = input("Ingrese nombre del agente: ").strip()

# while not nombre.isalpha():
#     print("Nombre inválido.")
#     nombre = input("Ingrese nombre del agente: ").strip()

# while (
#     energia > 0
#     and tiempo > 0
#     and cerradurasAbiertas < 3
#     and not (alarma and tiempo <= 3)
# ):

#     print("\n--- ESTADO ---")
#     print(f"Energía: {energia}")
#     print(f"Tiempo:  {tiempo}")
#     print(f"Cerraduras abiertas: {cerradurasAbiertas}")
#     print(f"Alarma: {'ON' if alarma else 'OFF'}")

#     print("\n1) Forzar cerradura")
#     print("2) Hackear panel")
#     print("3) Descansar")

#     opcion = input("Opción: ").strip()

#     while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
#         print("Opción inválida.")
#         opcion = input("Opción: ").strip()

#     opcion = int(opcion)

#     if opcion == 1:
#         energia -= 20
#         tiempo -= 2
#         rachaForzar += 1

#         if rachaForzar >= 3:
#             print("La cerradura se trabó. Alarma activada.")
#             alarma = True
#             rachaForzar = 0

#         elif energia < 40:
#             riesgo = input("Riesgo activo. Elija un número (1-3): ").strip()

#             while not riesgo.isdigit() or int(riesgo) not in [1, 2, 3]:
#                 print("Número inválido.")
#                 riesgo = input("Riesgo activo. Elija un número (1-3): ").strip()

#             if int(riesgo) == 3:
#                 print("Fallaste. Alarma activada.")
#                 alarma = True
#             else:
#                 cerradurasAbiertas += 1
#                 print("Cerradura abierta.")

#         else:
#             cerradurasAbiertas += 1
#             print("Cerradura abierta.")

#     elif opcion == 2:
#         energia -= 10
#         tiempo -= 3
#         rachaForzar = 0
#         codigoParcial = ""

#         print("Hackeando...")

#         for i in range(4):
#             print(f"Paso {i + 1}/4")
#             codigoParcial += "A"

#         if len(codigoParcial) >= 8 and cerradurasAbiertas < 3:
#             cerradurasAbiertas += 1
#             print("Código completo. Cerradura abierta.")
#         else:
#             print(f"Progreso del código: {len(codigoParcial)}/8 caracteres.")

#     elif opcion == 3:
#         tiempo -= 1
#         rachaForzar = 0
#         energia += 15

#         if energia > 100:
#             energia = 100

#         if alarma:
#             energia -= 10
#             print("Descanso afectado por alarma (-10 extra energía).")

#         print("Descansaste.")

# if cerradurasAbiertas == 3:
#     print("\nVICTORIA: abriste la bóveda.")
# elif alarma and tiempo <= 3:
#     print("\nDERROTA: sistema bloqueado por alarma.")
# else:
#     print("\nDERROTA: te quedaste sin recursos.")

# 5
# print("--- BIENVENIDO A LA ARENA ---")

# nombre = input("Nombre del Gladiador: ").strip()

# while not nombre.isalpha():
#     print("Error: Solo se permiten letras.")
#     nombre = input("Nombre del Gladiador: ").strip()

# vidaJugador = 100
# vidaEnemigo = 100
# pociones = 3
# danioBase = 15
# danioEnemigo = 12
# turnoJugador = True

# print("\n=== INICIO DEL COMBATE ===")

# while vidaJugador > 0 and vidaEnemigo > 0:

#     print("\n=== NUEVO TURNO ===")
#     print(
#         f"{nombre} (HP: {vidaJugador}) vs Enemigo (HP: {vidaEnemigo}) | Pociones: {pociones}"
#     )

#     if turnoJugador:
#         print("\nElige acción:")
#         print("1. Ataque Pesado")
#         print("2. Ráfaga Veloz")
#         print("3. Curar")

#         opcion = input("Opción: ").strip()

#         while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
#             print("Error: Ingrese un número válido.")
#             opcion = input("Opción: ").strip()

#         opcion = int(opcion)

#         if opcion == 1:
#             danio = danioBase

#             if vidaEnemigo < 20:
#                 danio = danioBase * 1.5
#                 print("¡Golpe crítico!")

#             vidaEnemigo -= danio
#             print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

#         elif opcion == 2:
#             print(">> ¡Inicias una ráfaga de golpes!")

#             for i in range(3):
#                 vidaEnemigo -= 5
#                 print("> Golpe conectado por 5 de daño")

#         elif opcion == 3:
#             if pociones > 0:
#                 vidaJugador += 30
#                 pociones -= 1
#                 print("Te curaste 30 puntos de vida.")
#             else:
#                 print("¡No quedan pociones!")

#         turnoJugador = False

#     else:
#         if vidaEnemigo > 0:
#             vidaJugador -= danioEnemigo
#             print(f">> ¡El enemigo contraataca por {danioEnemigo} puntos!")

#         turnoJugador = True

# print("\n=== FIN DEL COMBATE ===")

# if vidaJugador > 0:
#     print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
# else:
#     print("DERROTA. Has caído en combate.")
