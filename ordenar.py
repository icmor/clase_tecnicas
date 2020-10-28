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
Tiempo de ejecución: {total}\n\
Archivo con resultados: ordenados_burbuja.txt")


def insertion_sort(numeros):
    start = time.perf_counter()
    for i in range(1,len(numeros)):
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
Tiempo de ejecución: {total}\n\
Archivo con resultados: ordenados_insercion.txt")


def quicksort(numeros):
    pass


def heapsort(numeros):
    pass
