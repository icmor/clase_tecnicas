''' Function Wrappers '''
import time
from popup import popup
import sys
import json


def high_limit(func, archivo):
    def wrapper():
        sys.setrecursionlimit(50_000)
        start = time.perf_counter()
        resultados = []
        valores = [num for num in range(5_000)]
        for num in valores:
            resultados.append(func(num))
        total = round(time.perf_counter() - start, 2)

        with open(archivo, 'w') as file:
            json.dump(resultados, file, indent=0)
        popup("Calculamos los primeros 5,000 factoriales\n"
              + f"Tiempo de ejecucion: {total}\n"
              + f"Resultado en el archivo: {archivo}")
    return wrapper
