""" Algoritmos para Manipular Grafos """

from popup import popup
import time
import json


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []
        self.mar = []

    def borde(self, u, v, p):
        """ Método para añadir un borde al grafo """
        self.grafo.append([u, v, p])

    # Funcion para hallar un conjunto basada en Union/Find
    def find(self, padre, i):
        if padre[i] == i:
            return i
        return self.find(padre, padre[i])

    # Funcion que une dos conjuntos (Union/Find)
    def union(self, padre, nivel, x, y):
        x1 = self.find(padre, x)
        y1 = self.find(padre, y)

        if nivel[x1] < nivel[y1]: padre[x1] = y1
        elif nivel[x1] > nivel[y1]: padre[y1] = x1
        else:
            padre[y1] = x1
            nivel[x1] += 1

    # Algoritmo de Kruskal para encontrar el minimo arbol recubridor
    def kruskal(self):

        self.mar = []
        i = 0
        j = 0

        # Ordena los bordes de acuerdo a su peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        padre = []
        nivel = []

        for nodo in range(self.vertices):
            padre.append(nodo)
            nivel.append(0)

        while j < self.vertices - 1:

            u, v, p = self.grafo[i]
            i += 1
            x = self.find(padre, u)
            y = self.find(padre, v)

            if x != y:
                j = j + 1
                self.mar.append([u, v, p])
                self.union(padre, nivel, x, y)

        costo = 0
        message = "\n\n----------Arbol minimo recubridor----------\n\n"
        for u, v, peso in self.mar:
            costo += peso
            message += f"Borde: {u}____{v}, Peso: {peso}\n"
        message += f"\nCosto del minimo arbol recubridor: {costo}"
        return message


# Funcion auxiliar
def kruskal():
    grafo = Grafo(10)
    grafo.borde(0, 1, 5)
    grafo.borde(1, 2, 4)
    grafo.borde(0, 3, 4)
    grafo.borde(1, 3, 2)
    grafo.borde(0, 4, 1)
    grafo.borde(3, 4, 2)
    grafo.borde(4, 5, 1)
    grafo.borde(3, 5, 5)
    grafo.borde(5, 6, 7)
    grafo.borde(3, 6, 11)
    grafo.borde(6, 7, 1)
    grafo.borde(3, 7, 2)
    grafo.borde(6, 8, 4)
    grafo.borde(7, 8, 6)
    grafo.borde(2, 8, 1)
    grafo.borde(2, 7, 4)
    grafo.borde(8, 9, 0)
    grafo.borde(2, 9, 2)

    message = "----------Grafo a utilizar----------\n\n"
    for u, v, peso in grafo.grafo:
            message += f"Borde: {u}____{v}, Peso: {peso}\n"
    start = time.perf_counter()
    message += grafo.kruskal()
    total = round(time.perf_counter() - start, 8)
    message += f"\n\nTiempo de ejecución: {total}\nArchivo: grafos_kruskal.txt\n"
    with open("grafos_kruskal.txt", 'w') as file:
        json.dump(grafo.mar, file)
    popup(message)
