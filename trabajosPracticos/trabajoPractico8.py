import os

# 1.

# # ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.
# division = 10 / 0

# # TypeError: Ocurre cuando se intenta realizar una operación con tipos de datos incompatibles.
# a = 10
# b = input("Introduzca un número: ")
# resultado = a / b
# print(f"Resultado: {resultado}")

# # NameError: Ocurre cuando se intenta acceder a una variable que no ha sido definida.
# print(variable_inexistente)

# # IndexError: Ocurre cuando se intenta acceder a un índice que no existe en una lista.
# numeros = [1, 2, 3]
# print(numeros[5])

# # ValueError: Ocurre cuando se intenta convertir un valor a un tipo de dato que no es compatible.
# numero = int("hola")

# # KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
# diccionario = {"a": 1, "b": 2}
# print(diccionario["c"])

# # SyntaxError: Ocurre cuando el código no sigue la sintaxis correcta del lenguaje de programación.
# nombre = "Juan

# # FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
# archivo = open("archivo_inexistente.txt", "r")

# -----

# 2.

# print("Punto 2: Ejemplos de errores corregidos\n")

# # ZeroDivisionError corregido: se verifica que el divisor no sea cero antes de dividir
# print("\n\nEjemplo de ZeroDivisionError corregido:")
# divisor = 5
# if divisor != 0:
#     division = 10 / divisor
#     print(f"División: {division}\n")

# # TypeError corregido: se convierte el input a int antes de operar
# print("\n\nEjemplo de TypeError corregido:")
# a = 10
# b = int(input("Introduzca un número: "))
# resultado = a / b
# print(f"Resultado: {resultado}\n")

# # NameError corregido: se define la variable antes de usarla
# print("\n\nEjemplo de NameError corregido:")
# variable_existente = "Hola, mundo"
# print(f"Variable existente: {variable_existente}\n")

# # IndexError corregido: se usa un índice válido dentro del rango de la lista
# print("\n\nEjemplo de IndexError corregido:")
# numeros = [1, 2, 3]
# print(f"Elemento en el índice 2: {numeros[2]}\n")

# # ValueError corregido: se convierte un string que sí representa un número
# print("\n\nEjemplo de ValueError corregido:")
# numero = int("42")
# print(f"Número: {numero}\n")

# # KeyError corregido: se accede a una clave que sí existe en el diccionario
# print("\n\nEjemplo de KeyError corregido:")
# diccionario = {"a": 1, "b": 2}
# print(f"Valor de la clave 'a': {diccionario['a']}\n")

# # SyntaxError corregido: se cierra correctamente la cadena de texto
# print("\n\nEjemplo de SyntaxError corregido:")
# nombre = "Juan"
# print(f"Nombre: {nombre}\n")

# # FileNotFoundError corregido: se verifica si el archivo existe antes de abrirlo
# print("\n\nEjemplo de FileNotFoundError corregido:")
# if os.path.exists("archivo_existente.txt"):
#     archivo = open("archivo_existente.txt", "r")

# -----

# 3.

# print("Punto 3: Ejemplos de errores usando try-except\n")

# # ZeroDivisionError
# print("\n\nEjemplo de ZeroDivisionError:")
# try:
#     division = 10 / 0
# except:
#     print("Ocurrió un error al intentar dividir.\n")

# # TypeError
# print("\n\nEjemplo de TypeError:")
# try:
#     a = 10
#     b = input("Introduzca un número: ")
#     resultado = a / b
#     print(f"Resultado: {resultado}")
# except:
#     print("Ocurrió un error al intentar realizar la operación.\n")

# # NameError
# print("\n\nEjemplo de NameError:")
# try:
#     print(variable_inexistente)
# except:
#     print("Ocurrió un error al intentar acceder a la variable.\n")

# # IndexError
# print("\n\nEjemplo de IndexError:")
# try:
#     numeros = [1, 2, 3]
#     print(numeros[5])
# except:
#     print("Ocurrió un error al intentar acceder al elemento de la lista.\n")

# # ValueError
# print("\n\nEjemplo de ValueError:")
# try:
#     numero = int("hola")
# except:
#     print("Ocurrió un error al intentar convertir el valor.\n")

# # KeyError
# print("\n\nEjemplo de KeyError:")
# try:
#     diccionario = {"a": 1, "b": 2}
#     print(diccionario["c"])
# except:
#     print("Ocurrió un error al intentar acceder a la clave del diccionario.\n")

# # FileNotFoundError
# print("\n\nEjemplo de FileNotFoundError:")
# try:
#     archivo = open("archivo_inexistente.txt", "r")
# except:
#     print("Ocurrió un error al intentar abrir el archivo.\n")

# -----

# 4.

# print("Punto 4: Ejemplos de manejo de errores con try-except y tipo de error\n")

# # ZeroDivisionError
# print("\n\nEjemplo de manejo de ZeroDivisionError:")
# try:
#     division = 10 / 0
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # TypeError
# print("\n\nEjemplo de manejo de TypeError:")
# try:
#     a = 10
#     b = input("Introduzca un número: ")
#     resultado = a / b
#     print(f"Resultado: {resultado}")
# except TypeError:
#     print("Error: No se puede operar entre tipos de datos incompatibles.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # NameError
# print("\n\nEjemplo de manejo de NameError:")
# try:
#     print(variable_inexistente)
# except NameError:
#     print("Error: La variable no está definida.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # IndexError
# print("\n\nEjemplo de manejo de IndexError:")
# try:
#     numeros = [1, 2, 3]
#     print(numeros[5])
# except IndexError:
#     print("Error: El índice está fuera del rango de la lista.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # ValueError
# try:
#     numero = int("hola")
# except ValueError:
#     print("Error: No se puede convertir ese valor a número entero.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # KeyError
# print("\n\nEjemplo de manejo de KeyError:")
# try:
#     diccionario = {"a": 1, "b": 2}
#     print(diccionario["c"])
# except KeyError:
#     print("Error: La clave no existe en el diccionario.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# # FileNotFoundError
# print("\n\nEjemplo de manejo de FileNotFoundError:")
# try:
#     archivo = open("archivo_inexistente.txt", "r")
# except FileNotFoundError:
#     print("Error: El archivo no fue encontrado.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")

# -----

# 5.

# print("Punto 5: Ejemplos de manejo de errores con try-except, tipo de error, else y finally\n")

# # ZeroDivisionError
# print("\n\nEjemplo de manejo de ZeroDivisionError:")
# try:
#     division = 10 / 0
# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print(f"División exitosa: {division}\n")
# finally:
#     print("Operación de división finalizada.\n")

# # TypeError
# print("\n\nEjemplo de manejo de TypeError:")
# try:
#     a = 10
#     b = input("Introduzca un número: ")
#     resultado = a / b
# except TypeError:
#     print("Error: No se puede operar entre tipos de datos incompatibles.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print(f"Resultado: {resultado}\n")
# finally:
#     print("Operación de cálculo finalizada.\n")

# # NameError
# print("\n\nEjemplo de manejo de NameError:")
# try:
#     print(variable_inexistente)
# except NameError:
#     print("Error: La variable no está definida.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print("Variable accedida correctamente.\n")
# finally:
#     print("Operación de acceso a variable finalizada.\n")

# # IndexError
# print("\n\nEjemplo de manejo de IndexError:")
# try:
#     numeros = [1, 2, 3]
#     print(numeros[5])
# except IndexError:
#     print("Error: El índice está fuera del rango de la lista.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print("Elemento accedido correctamente.\n")
# finally:
#     print("Operación de acceso a lista finalizada.\n")

# # ValueError
# print("\n\nEjemplo de manejo de ValueError:")
# try:
#     numero = int("hola")
# except ValueError:
#     print("Error: No se puede convertir ese valor a número entero.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print(f"Conversión exitosa: {numero}\n")
# finally:
#     print("Operación de conversión finalizada.\n")

# # KeyError
# print("\n\nEjemplo de manejo de KeyError:")
# try:
#     diccionario = {"a": 1, "b": 2}
#     print(diccionario["c"])
# except KeyError:
#     print("Error: La clave no existe en el diccionario.\n")
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
# else:
#     print("Clave accedida correctamente.\n")
# finally:
#     print("Operación de acceso a diccionario finalizada.\n")

# # FileNotFoundError
# print("\n\nEjemplo de manejo de FileNotFoundError:")
# try:
#     archivo = open("archivo_inexistente.txt", "r")
# except FileNotFoundError:
#     print("Error: El archivo no fue encontrado.\n")
#     archivo = None
# except Exception as e:
#     print(f"Error inesperado: {e}\n")
#     archivo = None
# else:
#     print("Archivo abierto correctamente.\n")
# finally:
#     if archivo:
#         archivo.close()
#     print("Operación de archivo finalizada.\n")

# -----

# 6.

# print("Punto 6: Ejemplos de manejo de errores con try-except y tipo de error\n")

# try:
#     numero = int(input("Ingrese un número: "))
#     print(f"El número ingresado es: {numero}\n")
# except ValueError:
#     print("Debe ingresar un número válido.\n")
# except Exception as e:
#     print(f"Se produjo un error inesperado: {e}\n")

# -----

# 7.

# print("Punto 7: Ejemplo de manejo de errores con bucle while para solicitar un número válido\n")

# numero_valido = False

# while not numero_valido:
#     try:
#         numero = int(input("Ingrese un número: "))
#         print(f"El número ingresado es: {numero}")
#         numero_valido = True
#     except ValueError:
#         print("Debe ingresar un número válido. Intente nuevamente.")
#     except Exception as e:
#         print(f"Se produjo un error inesperado: {e}. Intente nuevamente.")