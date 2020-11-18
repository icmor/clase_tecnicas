from popup import popup
import json
import time


def mergesort(array):
    if len(array) > 1:
        middle = len(array) // 2
        right = array[:middle]
        left = array[middle:]

        mergesort(right)
        mergesort(left)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                k += 1

            else:
                array[k] = right[j]
                j += 1
                k += 1

        # Checamos si quedo algun elemento en las listas
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1


def call_mergesort(numeros):
    start = time.perf_counter()
    mergesort(numeros)
    total = round(time.perf_counter() - start, 2)
    with open("ordenados_mergesort.txt", "w") as file:
        json.dump(numeros, file, indent=0)
        popup(f"¡Los números han sido ordenados!\n\
Tiempo de ejecución: {total}s\n\
Archivo con resultados: ordenados_mergesort.txt")

