def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element (in this case, the middle element)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)


def quick_sortt(lista, inicio, fin):
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivot = lista[inicio]
    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivot:
            posterior -= 1
        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior += 1
        while anterior < posterior and lista[anterior] <= pivot:
            anterior += 1
        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior -= 1
        lista[anterior] = pivot
    quick_sortt(lista, inicio, anterior - 1)
    quick_sortt(lista, anterior + 1, fin)


lista = quick_sortt(my_list, 0, len(my_list) - 1)
print(lista)
