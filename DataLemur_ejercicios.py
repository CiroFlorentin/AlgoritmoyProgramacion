# Base 13
"""
Dado un entero num, devuelva su representación de cuerda en la base 13.

En caso de que no utilices la base 13 tanto (quién hace, verdad?), aquí es un resumen rápido: al igual que la base 10 utiliza dígitos de 0 a 9. Pero también para 10, 11 y 12, usamos las letras A, B y C.

Por ejemplo:

    9 en la base 13 sigue "9"
    10 en la base 13 es "A"
    11 en la base 13 es "B"
    12 en la base 13 es "C"
    13 en la base 13 es "10"
    14 en la base 13 es "11"
    49 en la base 13 es "3A"(desde 3 x 13 + 10 = 49)
    69 en la base 13 es "54"(desde 5 x 13 +4 = 69)
"""
# def base13(num):
#     if num == 0:
#         return "0"
#     digitos = []
#     digitos_ordenados = []
#     if num < 0:
#         num = -num
#         digitos.append('-')
#
#     while num > 0:
#         numero = num % 13
#         if numero < 10:
#             digitos.append(str(numero))
#         else:
#             digitos.append(chr(ord('A') + numero - 10))
#         num //= 13
#     for i in digitos[::-1]:
#         if i == '-':
#             digitos_ordenados.insert(0, i)
#         else:
#             digitos_ordenados.append(i)
#     return ''.join(digitos_ordenados)
# print(base13(-1845))

#Misma Raya
"""
Se te ha dado un m x nla matriz. Su tarea es determinar si la matriz tiene rayas diagonales donde todos los elementos en cada diagonal de arriba-izquierda a abajo-derecha son de la misma franja que es, son idénticos.
En este contexto, cada franja diagonal corre desde la esquina superior izquierda hasta la esquina inferior derecha de la matriz. Compruebe si cada rayas diagonales consiste enteramente en el mismo número.
Regreso True si todas las rayas diagonales son de la misma raya, de lo contrario volver False.
"""
# def diagonal_iguales(matriz):
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if i > 0 and j > 0:
#                 if matriz[i][j] != matriz[i - 1][j - 1]:
#                     return False
#     return True
# matriz = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]
# print(diagonal_iguales(matriz))

# Formula Factorial
"""
Dado un número nn, escribir una fórmula que devuelva n!n.!
En caso de que se haya olvidado de la fórmula factorial, n!=n∗(n−1)∗(n−2)∗.....2∗1n! = n ∗"en n−11),(n −2)∗..∗1
Por ejemplo, 5!=5∗4∗3∗2∗1=1205! = 5 ∗4 y 3 2 2 = 1=120 para que devolvamos 120.
Supone es nn es un entero no negativo.
"""
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num - 1)
# print(factorial(5))

# Intersection of Two Lists
"""
Escriba una función para obtener la intersección de dos listas.
Por ejemplo, si A = [1, 2, 3, 4, 5], y B = [0, 1, 3, 7] entonces deberías regresar [1, 3].
La intersección de dos listas es la lista de elementos que están presentes en ambas listas.
"""
# def interseccion(a,b):
#     lista_intersectada = []
#     for i in a:
#         if i in b:
#             lista_intersectada.append(i)
#     return lista_intersectada
# a = [1, 2, 3, 4, 5]
# b = [0, 1, 3, 7]
# print(interseccion(a,b))

# Another One

"""
Estamos tratando de crear un clon digital de DJ Khaled. No se necesita una IA elegante o las alorithms.
Sólo toma un número y agrega otro:
Más específicamente, se le da una matriz entera digits, donde cada uno digits[i] es el dígito de todo positivo número. Se ordena desde el dígito más significativo a la menos significativa.
Devuelva una serie de dígitos del número después de añadir otro a la entrada.
Ejemplo número 1
Entrada: digits = [1, 2, 3]
Producto: [1, 2, 4]
Ejemplo 2
Entrada: digits = [6, 9]
Producto: [7, 0]
"""
# def anadir_digito(digits):
#     num = 0
#     for i in range(len(digits)):
#         num += digits[i] * (10 ** (len(digits) - i - 1))
#     num += 1
#     resultado = []
#     while num > 0:
#         resultado.append(num % 10)
#         num //= 10
#     return resultado[::-1]
# print(anadir_digito([1, 2, 3]))
# print(anadir_digito([6, 9]))
# print(anadir_digito([9, 9, 9]))

# Weakest Strong Link
"""Conoces esa frase, cómo una cadena es tan fuerte como su eslabón más débil?

Imagina que tenías una valla de eslabón de cadena, representada como una matriz. Para el eslabón de cadena en la posición (i j), la matriz de entrada strength[i][j]indica lo fuerte que es la cadena en esa posición (donde más fuerte significa un número más alto). Los números en la matriz son únicos.

El enlace fuerte más débil se define como el eslabón de cadena más débil de su hilera, pero también el eslabón más fuerte de su columna.

Dada una matriz strength, devuelva el eslabón más débil si existe; de lo contrario, retornega -1. Si existe un eslabón más débil, siempre es exactamente uno, y se puede probar que ningún otro vínculo satisfará ambas condiciones simultáneamente.
"""
# def eslabon_mas_debil(matriz):
#     m = len(matriz)
#     n = len(matriz[0])
#     min_rows = [0] * m
#     max_cols = [0] * n
#     for i in range(m):
#         min_rows[i] = min(matriz[i])
#     for f in range(m):
#         for c in range(n):
#             max_cols[c] = max(matriz[f][c], max_cols[c])
#
#     for i in range(m):
#         for j in range(n):
#             if matriz[i][j] == min_rows[i] and matriz[i][j] == max_cols[j]:
#                 return matriz[i][j]
#     return -1
# matriz = [[9, 8, 10],[6, 15, 4]]
# print(eslabon_mas_debil(matriz))

# Fizz Buzz Sum
"""Escriba una función fizz_buzz_sum encontrar la suma de todos los múltiplos de 3 o 5 por debajo de un valor objetivo.

Por ejemplo, si el valor objetivo era de 10, los múltiplos de 3 o 5 por debajo de 10 son 3, 5, 6, y 9.

Porque 3+5+6+9=233 5 5x 6 +9= 2323, nuestra función volvería 23."""

def fizz_buzz_sum(n):
    sum = 0
    numeros = []
    for i in range(n):

        if (i % 3 == 0 or i % 5 == 0) and i != 0:
            numeros.append(i)
            sum += i
    print(numeros)
    return sum
print(fizz_buzz_sum(15)) # 23