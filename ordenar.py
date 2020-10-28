""" Funciones de ordenamiento"""

from popup import popup


def bubble_sort(numeros):
    tam = len(numeros) 
    for i in range(0, tam): 
        for j in range(0, tam-1): 
            if numeros[j] > numeros[j+1]: 
                temporal = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = numeros
    return numeros

def insertion_sort(numeros):
    pass


def quicksort(numeros):
    pass


def heapsort(numeros):
    pass
