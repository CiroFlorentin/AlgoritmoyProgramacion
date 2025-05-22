"""1-rangoHasta(n) -> Lista de números: dado un número "n", retorna la lista de números desde el 0 hasta el N incluído. Por ejemplo: rangoHasta(5) -> [0,1,2,3,4,5]."""

# def rangoHasta(n,rango=None):
#     if rango is None:
#         rango = []
#     if n<0:
#         return rango
#
#     rangoHasta(n-1,rango)
#     rango.append(n)
#     return rango
# print(rangoHasta(5))

'''2- rango(desde, hasta) -> lista de números: similar a rango, pero ahora se puede especificar el "desde". Ej: rango(5, 10) -> [5,6,7,8,9,10]. No hace falta validar que desde sea menor a hasta o tener rangos decrecientes.'''

# def rangoHasta(desde, hasta, lista = None):
#     if lista is None:
#         lista = []
#     if hasta == desde:
#         lista.append(desde)
#         return lista
#     if hasta > desde:
#         rangoHasta(desde, hasta - 1, lista)
#         lista.append(hasta)
#         return lista
#     elif desde > hasta:
#         rangoHasta(desde - 1, hasta, lista)
#         lista.append(desde)
#         return lista
#
# print(rangoHasta(15, 10))


"""3- sumaHasta(n) -> numero. Retorna la suma de los numeros desde el 0 hasta el N. Por ejemplo. sumaHasta(5) = 5 + 4 + 3 + 2 + 1 + 0 => 15"""
#
# def sumaHasta(n):
#     if n == 0:
#         return 0
#     return n + sumaHasta(n - 1)
#
# print(sumaHasta(5))

'''4- removerTodos(lista, elemento): -> lista, Dada una lista y un elemento, retorna otra lista igual a la original, pero sin el "elemento" dado. En caso en que el elemento aparezca múltiples veces, lo remueve de todas. Ejemplo: remover([1,2,3,1,6,7,1,9,1], 1) -> [2,3,6,7,9]'''

# def removerTodos(lista,elemento ):
#     if elemento in lista:
#         lista.remove(elemento)
#         return removerTodos(lista,elemento)
#     return lista
#
# print(removerTodos([1,2,3,1,6,7,1,9,1], 1))

"""5- aparear(unaLista, otra) -> lista de pares (x, y): tal que "x" pertence a "unaLista", e y pertenece a "otra". Ejemplo: aparear([1,2,3], ['a','b','c']) -> [ (1,'a'), (2,'b'), (3,'c')]"""

# def aparear(unaLista, otra):
#     if len(unaLista) != len(otra):
#         return 'Tus listas son dispares'
#
#     if not unaLista or not otra:
#         return []
#
#     return [(unaLista[0], otra[0])] + aparear(unaLista[1:], otra[1:])
# print(aparear([1,2,3], ['a','b','c']))

"""6- aMayusculas(unString) -> otro string igual pero en mayusculas. Acordarse que los strings también se pueden tratar como listas"""

# def Mayusculas(unString):
#         if not unString:
#             return ''
#
#         return unString[0].upper() + Mayusculas(unString[1:])
#
# print(Mayusculas('Hola gente'))

'''sumarN(n, numeros): Realizar una función que dada una lista de números y un número N, retorna la suma de todos los N primeros elementos. Ejemplo sumarN(3, [2, 4, 6, 8, 10, 12]) -> 2+4+6 = 24'''

# def sumarN(n, numeros,suma=0):
#     if n == 0 or not numeros :
#         return suma
#     suma += numeros[0]
#     print( suma, end=" + "  if n > 1 else " = ")
#     return numeros[0] + sumarN(n-1, numeros[1:])
#
#
# print(sumarN(3, [2, 4, 6, 8, 10, 12]))
