# 1.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = n * factorial(n - 1)
#         return result

# num = int(input("Ingrese un número para calcular su factorial: "))

# for i in range(1, num + 1):
#     print(f"{i}! = {factorial(i)}")

# 2.

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# posicion = int(input("Ingrese la posición en la secuencia de Fibonacci: "))

# print(f"Fibonacci en la posición {posicion}: {fibonacci(posicion)}")

# print("Serie de Fibonacci hasta la posición indicada:")
# for i in range(posicion + 1):
#     print(f"Posición {i} = {fibonacci(i)}")

# 3.

# def potencia(n, m):
#     if m == 0:
#         return 1
#     elif m < 0:
#         result = 1 / potencia(n, -m)
#         return result
#     else:
#         result = n * potencia(n, m - 1)
#         return result

# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))

# resultado = potencia(base, exponente)

# print(f"{base}^{exponente} = {resultado}")

# 4.

# def decimal_a_binario(n):
#     if n == 0:
#         return ""
#     else:
#         result = decimal_a_binario(n // 2) + str(n % 2)
#         return result

# try:
#     numero_decimal = int(input("Ingrese un número decimal para convertir a binario: "))

#     if numero_decimal < 0:
#         raise ValueError("Número no válido. Debe ser un entero positivo.")

#     if numero_decimal == 0:
#         print("El número binario es: 0")

#     else:
#         numero_binario = decimal_a_binario(numero_decimal)

#         print(f"El número decimal {numero_decimal} en binario es: {numero_binario}")

# except ValueError as error:
#     print(f"Error: {error}")

# 5.

# def es_palindromo(palabra):
#     palabra = palabra.lower()

#     if len(palabra) <= 1:
#         return True

#     if palabra[0] != palabra[-1]:
#         return False

#     result = es_palindromo(palabra[1:-1])
#     return result

# texto = input("Ingrese una palabra: ")

# if es_palindromo(texto):
#     print("Es un palíndromo")
# else:
#     print("No es un palíndromo")

# 6.

# def suma_digitos(n):
#     if n < 10:
#         return n
#     else:
#         result = (n % 10) + suma_digitos(n // 10)
#         return result
    
# numero = int(input("Ingrese un número para sumar sus dígitos: "))

# if numero < 0:
#     print("Número no válido. Debe ser un entero positivo.")
# else:
#     resultado = suma_digitos(numero)
#     print(f"La suma de los dígitos de {numero} es: {resultado}")

# 7.

# def contar_bloques(n):
#     if n <= 0:
#         return 0
#     else:
#         result = n + contar_bloques(n - 1)
#         return result

# num_bloques = int(input("Ingrese el número de bloques: "))

# if num_bloques < 0:
#     print("Número no válido. Debe ser un entero positivo.")
# else:    
#     total_bloques = contar_bloques(num_bloques)
#     print(f"El número total de bloques necesarios para construir la pirámide es: {total_bloques}")

# 8.

# def contar_digitos(numero, digito):
#     if numero == 0:
#         return 0
#     else:
#         if numero % 10 == digito:
#             count = 1 
#         else:
#             count = 0
        
#         result = count + contar_digitos(numero // 10, digito)
#         return result
    
# try:
#     numero = int(input("Ingrese un número para contar sus dígitos: "))
#     digito = int(input("Ingrese el dígito a contar: "))

#     if numero < 0 or digito < 0 or digito > 9:
#         raise ValueError("Número no válido. El número debe ser un entero positivo y el dígito debe estar entre 0 y 9.")

#     cantidad_digitos = contar_digitos(numero, digito)

#     print(f"El dígito {digito} aparece {cantidad_digitos} veces en el número {numero}.")
# except ValueError as error:
#     print(f"Error: {error}")