""" Funciones de Búsqueda """

from popup import popup
import time


def verify(func):
    def wrapper(entry, numeros):
        value = entry.get()
        if value.isdigit():
            func(int(value), numeros)
        else:
            popup("Por favor ingresa un número.")
        entry.set("")
    return wrapper


@verify
def linear_search(num, numeros):
    start = time.perf_counter()
    for index, x in enumerate(numeros):
        if x == num:
            total = round(time.perf_counter() - start, 6)
            message = f"El número {num} fue encontrado en el índice: {index}\n"
            break
    else:
        total = round(time.perf_counter() - start, 6)
        message = f"No se encontró el número {num}\n"

    popup(message + f"Tiempo de ejecución: {total}s")


@verify
def binary_search(num, numeros):
    numeros.sort()
    start = time.perf_counter()
    high = len(numeros)
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if numeros[mid] == num:
            total = round(time.perf_counter() - start, 6)
            message = f"El número {num} fue encontrado en el índice: {mid}\n"
            break
        if num < numeros[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        total = round(time.perf_counter() - start, 6)
        message = f"No se encontró el número {num}\n"

    popup(message + f"Tiempo de ejecución: {total}s")
