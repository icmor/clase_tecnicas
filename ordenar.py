""" Funciones de ordenamiento"""

from popup import popup
import json


def bubble_sort(numeros):
    tam = len(numeros) 
    for i in range(tam):
        for j in range(tam-i-1):
            if numeros[j] > numeros[j+1]: 
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

    with open("ordenados_burbuja.txt") as file:
        json.dump(numeros, file)

def insertion_sort(numeros):
    pass


def quicksort(numeros):
    pass


def heapsort(numeros):
    pass
