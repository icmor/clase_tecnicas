''' Find the largest sum of a subarray in an array '''
from popup import popup
import time


def suma_max(datos):
    ''' Divide y venceras
    Suma maxima de un subarreglo '''

    def suma_max_medio(arreglo, izq, mitad, der):
        '''    Encuentra la suma de los valores maximos
        de la derecha e izquierda del subarreglo '''

        # Suma de los elementos de la izq
        suma = 0
        izq_sum = -10000

        for i in range(mitad, izq-1, -1):
            suma += arreglo[i]

            if (suma > izq_sum):
                izq_sum = suma

        # Suma de los elementos de la derecha
        suma = 0
        der_sum = -10000

        for i in range(mitad + 1, der + 1):
            suma += arreglo[i]

            if (suma > der_sum):
                der_sum = suma

        return max(izq_sum + der_sum, izq_sum, der_sum)

    def suma_max_subarreglo(arreglo, izq, der):
        ''' Suma los maximos valores del arreglo '''

        # Verifica si hay un solo elemento
        if (izq == der):
            return arreglo[izq]

        # Mitad del arreglo
        mitad = (izq + der) // 2

        izq_sum = suma_max_subarreglo(arreglo, izq, mitad)
        der_sum = suma_max_subarreglo(arreglo, mitad+1, der)
        mitad_sum = suma_max_medio(arreglo, izq, mitad, der)

        return max(izq_sum, der_sum, mitad_sum)

    start = time.perf_counter()
    max_sum = suma_max_subarreglo(datos, 0, len(datos)-1)
    total = round(time.perf_counter() - start, 2)
    popup(f"Tomamos un arreglo de tamaño {len(datos)}\n"
          + f"La suma maxima del subarreglo es: {max_sum}\n"
          + f"Tiempo de ejecución: {total}")
