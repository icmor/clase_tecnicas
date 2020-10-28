""" Funciones de Búsqueda """

from popup import popup


def verify(func):
    def wrapper(entry):
        value = entry.get()
        if value.isdigit():
            func(int(value))
        else:
            popup("Por favor ingresa un número.")
        entry.set("")
    return wrapper


@verify
def linear_search(number):
    pass


@verify
def binary_search(number):
    pass
