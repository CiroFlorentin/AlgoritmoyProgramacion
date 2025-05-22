lista_base = [5, 2, 9, 1, 6]


# # Lista de números aleatorios
# def lista_base_con_numeros_aleatorios():
#     lista = []
#     longitud = 100000
#     for i in range(longitud):
#         lista.append(random.randint(1, 10000))
#     return lista
# lista_base = lista_base_con_numeros_aleatorios()

# MERGE SORT
def merge(lista, lista_temporaria, inicio, medio, fin):
    fin_primera_parte = medio - 1
    indice_temporario = inicio
    tamano_de_lista = fin - inicio + 1

    while inicio <= fin_primera_parte and medio <= fin:
        if lista[inicio] <= lista[medio]:
            lista_temporaria[indice_temporario] = lista[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = lista[medio]
            medio += 1
        indice_temporario += 1

    while inicio <= fin_primera_parte:
        lista_temporaria[indice_temporario] = lista[inicio]
        indice_temporario += 1
        inicio += 1

    while medio <= fin:
        lista_temporaria[indice_temporario] = lista[medio]
        indice_temporario += 1
        medio += 1

    for i in range(tamano_de_lista):
        lista[fin] = lista_temporaria[fin]
        fin -= 1


def merge_sort_aux(lista, lista_temporaria, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort_aux(lista, lista_temporaria, inicio, medio)
        merge_sort_aux(lista, lista_temporaria, medio + 1, fin)
        merge(lista, lista_temporaria, inicio, medio + 1, fin)


def merge_sort(lista):
    lista_temporaria = [0] * len(lista)
    merge_sort_aux(lista, lista_temporaria, 0, len(lista) - 1)


# QUICK SORT
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def partition(array, low, high):
    pivote = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivote:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


quick_sort(lista_base, 0, len(lista_base) - 1)

# lista_copia = lista_base.copy()
# print(f"Lista desordenada: {lista_copia}")
# # Ejecutar y cronometrar los 2 métodos
# for metodo in ['Quick Sort', 'Merge Sort']:
#
#
#     inicio = time.time()
#     print(f"Ordenando con {metodo}")
#     if metodo == 'Quick Sort':
#         quick_sort(lista_copia,0,len(lista_copia)-1)
#     elif metodo == 'Merge Sort':
#         merge_sort(lista_copia)
#
#
#     fin = time.time()
#     print(f"{metodo} tomó {fin - inicio:.4f} segundos.")
#     print()
