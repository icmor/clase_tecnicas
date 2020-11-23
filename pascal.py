""" Pascal's Triangle """

from popup import popup
import time
import json


def pascal(n):

    memo = {}

    def compute_pascal(row, column):

        if (row, column) in memo:
            return memo[(row, column)]

        if column == 1 or column == row:
            num = 1
        else:
            num = compute_pascal(row-1, column) + compute_pascal(row-1, column-1)

        memo[(row, column)] = num
        return num

    start = time.perf_counter()
    triangle = []
    for i in range(1, n+1):
        row = []
        for j in range(1, i+1):
            row.append(compute_pascal(i, j))

        triangle.append(row)

    total = round(time.perf_counter() - start, 2)
    with open("pascal.txt", 'w') as file:
        json.dump(triangle, file, indent=0)

    popup(f"Generamos {n} filas del árbol de Pascal\n"
          + f"Tiempo de ejecución: {total}\n"
          + "Archivo con resultado: pascal.txt")
