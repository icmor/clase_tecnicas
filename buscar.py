""" Funciones de Búsqueda """

from popup import popup


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
    pass


@verify
def binary_search(num, numeros):
    pass
