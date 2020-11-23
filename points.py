''' Find closest pair of points '''
from popup import popup
import time
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance_to_point = None
        self.other = None

    def distance(self, point):
        return sqrt((point.x-self.x)**2 + (point.y - self.y)**2)

    def set_other(self, point):
        self.other = point
        self.distance_to_point = self.distance(point)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def closest_points(valores):

    def brute(array):
        minimum = Point(0, 0)
        minimum.distance_to_point = float('inf')
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                distance = Point.distance(array[i], array[j])
                if distance < minimum.distance_to_point:
                    minimum = array[i]
                    minimum.set_other(array[j])
        return minimum

    def min_distance(array):
        if len(array) <= 3:
            return brute(array)

        middle = len(array) // 2
        left = min_distance(array[:middle])
        right = min_distance(array[middle:])

        minimum = left if left.distance_to_point < right.distance_to_point \
            else right

        middle = array[len(array)//2]

        strip = [point for point in array
                 if abs(point.x - middle.x) < minimum.distance_to_point]
        strip.sort(key=lambda point: point.y)

        strip_min = minimum
        for i in range(len(strip)):
            j = i+1
            while j < len(strip) and strip[j].y - strip[i].y \
                    < strip_min.distance_to_point:
                strip_min = strip[i]
                strip_min.set_other(strip[j])
                j += 1

        return middle if middle.distance_to_point \
            < strip_min.distance_to_point else strip_min

    points = []
    for i in range(0, len(valores)-1, 2):
        points.append(Point(valores[i], valores[i+1]))
    start = time.perf_counter()
    point = min_distance(sorted(points, key=lambda point: point.x))
    total = round(time.perf_counter() - start, 2)
    popup("Se tomó un millón de puntos con coordenadas desde\n"
          + "-10,000,000 hasta 10,000,000 \n"
          + f"Los puntos más cercanos son {point} y {point.other}\n"
          + f"con una distancia de {round(point.distance_to_point, 2)}\n"
          + f"Tiempo de ejecución: {total}s\n")
