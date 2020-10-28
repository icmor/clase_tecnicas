""" Algoritmos para Manipular Grafos """

from popup import popup


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, x, y, w):
        """ Método para añadir un borde al grafo """
        self.graph.append([x, y, w])

    def kruskal(self):
        """ Algoritmo de Kruskal para encontrar el árbol recubridor
        mínimo """

        # Árbol resultante
        mst = []
