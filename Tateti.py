import random
from string import ascii_lowercase

import numpy as np

abecedarioSinRepeticion = ascii_lowercase
ABECEDARIO = []

for i in abecedarioSinRepeticion:
    for j in abecedarioSinRepeticion:
        ABECEDARIO.append(i + j)


def mostrarTablero():
    for i in tablero:
        for j in i:
            print(j, end='\t')
        print()


# Función para verificar si la posición es válida
def Posicion():
    while True:
        posicion = input("Ingrese la posición: ")
        if TAM <= 3:
            es_numero = True
            for numero in posicion:
                if numero not in '123456789':
                    es_numero = False
            if es_numero:
                pos = int(posicion)
                if 1 <= pos <= TAM * TAM:
                    return str(pos)
                else:
                    print("Posición fuera de rango. Intente nuevamente.")
            else:
                print("Entrada no válida. Intente nuevamente.")
        else:
            for letra in ABECEDARIO[:TAM * TAM]:
                if posicion == letra or posicion.lower() == letra.lower():
                    return letra
            print("Letra no válida, intente nuevamente.")


def cordenada(posicion, marca):
    for i in range(TAM):
        for j in range(TAM):
            if tablero[i][j] == posicion:
                tablero[i][j] = marca
                return True


contador1 = 0
contador2 = 0


def DiagonalGanador():
    contadorX = 0
    contadorO = 0
    for i in range(TAM):
        if tablero[i][i] == 'X':
            contadorX += 1
            contadorO -= 1
        elif tablero[i][i] == 'O':
            contadorO += 1
            contadorX -= 1
    if contadorX == CANTIDAD_SEGUIDAS:
        print("El jugador 1 ha ganado por diagonal principal")
        return True
    if contadorO == CANTIDAD_SEGUIDAS:
        print("El jugador 2 ha ganado por diagonal principal")
        return True
    return False


def ContraDiagonalGanador():
    contadorX = 0
    contadorO = 0
    for i in range(TAM):
        j = TAM - 1 - i
        if tablero[i][j] == 'X':
            contadorX += 1
            contadorO -= 1
        elif tablero[i][j] == 'O':
            contadorO += 1
            contadorX -= 1
    if contadorX == CANTIDAD_SEGUIDAS:
        print("El jugador 1 ha ganado por diagonal secundaria")
        return True
    if contadorO == CANTIDAD_SEGUIDAS:
        print("El jugador 2 ha ganado por diagonal secundaria")
        return True
    return False


def HorizontalGanador():
    for i in range(TAM):
        contadorX = 0
        contadorO = 0
        for j in range(TAM):
            if tablero[i][j] == 'X':
                contadorX += 1
                contadorO -= 1
            elif tablero[i][j] == 'O':
                contadorO += 1
                contadorX -= 1
        if contadorX == CANTIDAD_SEGUIDAS:
            print("El jugador 1 ha ganado por fila")
            return True
        if contadorO == CANTIDAD_SEGUIDAS:
            print("El jugador 2 ha ganado por fila")
            return True
    return False


def VerticalGanador():
    for j in range(TAM):
        contadorX = 0
        contadorO = 0
        for i in range(TAM):
            if tablero[i][j] == 'X':
                contadorX += 1
                contadorO -= 1
            elif tablero[i][j] == 'O':
                contadorO += 1
                contadorX -= 1
        if contadorX == CANTIDAD_SEGUIDAS:
            print("El jugador 1 ha ganado por columna")
            return True
        if contadorO == CANTIDAD_SEGUIDAS:
            print("El jugador 2 ha ganado por columna")
            return True
    return False


def chequear_ganador():
    return (DiagonalGanador() or
            ContraDiagonalGanador() or
            HorizontalGanador() or
            VerticalGanador())


def jugador(turno_actual):
    if turno_actual == 0:
        print('Turno del jugador 1')
        return 1, 'X'
    # por si queres jugar contra otro
    else:
        print('Turno del jugador 2')
        return 0, 'O'


def jugadorAleatorio():
    posicionLibres = []
    for i in range(TAM):
        for j in range(TAM):
            if tablero[i][j] not in ['X', 'O']:
                posicionLibres.append(tablero[i][j])
    if posicionLibres:
        return random.choice(posicionLibres)
    return None


def play():
    automatico = input("Desea jugar contra la computadora? (s/n): ").lower() == 's'
    turno = 0
    total_turnos = TAM * TAM
    for _ in range(total_turnos):
        turno, marca = jugador(turno)
        mostrarTablero()
        while True:
            if automatico:
                if marca == 'X':
                    pos = Posicion()
                else:
                    pos = jugadorAleatorio()
                    print(f"El jugador 2 ha elegido la posición: {pos}")
            else:
                pos = Posicion()
            if cordenada(pos, marca):
                break
            elif marca == 'X':
                print("Posición ocupada, elija otra.")
        if chequear_ganador():
            mostrarTablero()
            break


while True:
    jugar = input('Desea jugar? (s/n): ').lower()
    if jugar == 's':
        TAM = int(input('Ingrese el tamaño del tablero: '))
        CANTIDAD_SEGUIDAS = int(input('Ingrese la cantidad de marcas seguidas para ganar: '))
        # Generar tablero dependiendo del tamaño
        if TAM <= 3:
            tablero = np.arange(1, TAM * TAM + 1).reshape(TAM, TAM).astype(str)
        else:
            letrasNecesarias = ABECEDARIO[:TAM * TAM]
            tablero = np.array(letrasNecesarias).reshape(TAM, TAM)

        play()
    else:
        break
