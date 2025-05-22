import random as rnd

import numpy as np

# Ejercicio 4: Ceros en la contra-diagonal
# Dada una matriz de 3x3 llena con el número 5, modificá la matriz de forma que la contra-diagonal (diagonal secundaria) contenga ceros y el resto de los elementos mantenga su valor original.
# matrix = np.full((3,3),5)
#
# for i in range(matrix.shape[0]):
#     for j in range(matrix.shape[1]):
#         if i+j == len(matrix)-1:
#             matrix[i][j] = 0
#
# print(matrix)
# Ejercicio 5: Suma de filas y columnas
# Solicitá al usuario que ingrese los valores de una matriz de 3x3. Luego, mostrá la matriz completa y calculá la suma de cada fila y de cada columna por separado.
#
# matrix = np.full((3,3),0)
#
# for i in range(matrix.shape[0]):
#     for j in range(matrix.shape[1]):
#         matrix[i][j] = int(input(f'Que numero desea colocar en la posicion {i} {j}: '))
#     print('\n')
# for i in range(matrix.shape[0]):
#    print(f'fila {i+1}: {sum(matrix[i])}')
#
# for j in range(matrix.shape[1]):
#    print(f'columna {j+1}: {sum(matrix[:,j])}')
# print(matrix)
#
# Ejercicio 6: Buscaminas simplificado
# Generá una matriz de 3x3 y colocá tres minas de forma aleatoria (representadas por el número 9). Luego, calculá cuántas minas hay alrededor de cada casilla no-minada, y completá el tablero con esos valores.

TABLERO = np.zeros((3, 3), dtype=int)
MINAS = 3

minas_colocadas = 0
while minas_colocadas < MINAS:
    fila = rnd.randint(0, 2)
    columna = rnd.randint(0, 2)
    if TABLERO[fila][columna] != 9:
        TABLERO[fila][columna] = 9
        minas_colocadas += 1

for i in range(3):
    for j in range(3):
        if TABLERO[i][j] != 9:
            contador = 0
            for x in range(max(0, i - 1), min(3, i + 2)):
                for y in range(max(0, j - 1), min(3, j + 2)):
                    if TABLERO[x][y] == 9:
                        contador += 1
            TABLERO[i][j] = contador

for i in range(3):
    for j in range(3):
        print(TABLERO[i][j], end=' ')
    print()
