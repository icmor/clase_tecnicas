""" Funciones de ordenamiento"""

from popup import popup
import json
import time

def bubble_sort(numeros):
    start = time.perf_counter()
    n = len(numeros)
    for i in range(n):
        for j in range(n-i-1):
            if numeros[j] > numeros[j+1]: 
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

    total = round(time.perf_counter() - start, 2)
    with open("ordenados_burbuja.txt", "w") as file:
        json.dump(numeros, file)
    popup(f"¡Los números han sido ordenados!\n\
Tiempo de ejecución: {total}s\n\
Archivo con resultados: ordenados_burbuja.txt")


def insertion_sort(numeros):
    start = time.perf_counter()
    for i in range(1, len(numeros)):
        j = i - 1
        valor = numeros[i]
        while j >= 0 and valor < numeros[j]:
            numeros[j+1] = numeros[j]
            j -= 1
        numeros[j+1] = valor

    total = round(time.perf_counter() - start, 2)
    with open("ordenados_insercion.txt", "w") as file:
        json.dump(numeros, file)
    popup(f"¡Los números han sido ordenados!\n\
Tiempo de ejecución: {total}s\n\
Archivo con resultados: ordenados_insercion.txt")


def quicksort(numeros):
    def sort(left, right):
        if (left >= right):
            return
        pivot = numeros[(left+right)//2]
        mid = partition(left, right, pivot)
        sort(left, mid-1)
        sort(mid, right)

    def partition(left, right, pivot):
        while left <= right:
            while numeros[left] < pivot:
                left += 1
            while numeros[right] > pivot:
                right -= 1

            if left <= right:
                numeros[left], numeros[right] = numeros[right], numeros[left]
                left += 1
                right -= 1
        return left

    start = time.perf_counter()
    sort(0, len(numeros) - 1)
    total = round(time.perf_counter() - start, 4)

    with open("ordenados_quicksort.txt", "w") as file:
        json.dump(numeros, file)
    popup(f"¡Los números han sido ordenados!\n\
Tiempo de ejecución: {total}s\n\
Archivo con resultados: ordenados_quicksort.txt")

def heapsort(numeros):
    pass
