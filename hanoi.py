''' Torres de Hanoi '''
import time
from popup import popup


def hanoi(height):
    moves = ''

    def move(h, source, dest, free):
        nonlocal moves
        if h == 1:
            moves += f"Mueve el tope de {source} a {dest}\n"
            return

        move(h-1, source, free, dest)
        move(1, source, dest, free)
        move(h-1, free, dest, source)

    start = time.perf_counter()
    move(height, "izquierdo", "derecho", "medio")
    total = round(time.perf_counter() - start, 2)

    with open('hanoi.txt', 'w') as file:
        for line in moves:
            file.write(line)

    popup("Calculamos la secuencia para resolver\n"
          + f"Torres de Hanoi de una altura de {height}\n"
          + f"Tiempo de ejecución: {total}\n"
          + "Resultado guardado en: hanoi.txt")
