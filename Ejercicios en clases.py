"""EJERCICIOS DE CLASES"""
import numpy as np

# Ejercicio 1
# lista = arr.array('i',(random.randint(1,10) for _ in range(40)))
# print(lista)
# acumulador = 0
# for i in lista:
#     acumulador += 1
#     print(f'calificaciòn nro: {acumulador}:{lista[i]}')
# conteo = {}
# for num in lista:
#     if num in conteo:
#         conteo[num] += 1
#     else:
#         conteo[num] = 1
#
# conteo_ordenado = dict(sorted(conteo.items()))
# print()
# print(f'CALIFICAION PROMEDIO: ')
# for i in conteo_ordenado:
#     print(f' \t \t {i} = {conteo[i]}')

# Ejercicio 2
matrix = np.array([range(3), range(3), range(3)])

print()
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == j:
            matrix[i][j] = 10
        else:
            matrix[i][j] = 0
print(matrix)

Ejercicio
3
matrix = np.array([range(3), range(3), range(3)])
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == j:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 10
print(matrix)
