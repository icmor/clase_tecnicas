""" Técnicas Algorítmicas Evaluación Segundo Parcial
Equipo: Iñaki Cornejo, Wenceslao Trejo, Adolfo Tun y Fernando Manzano"""

import pathlib
import tkinter as tk
from ordenar import bubble_sort, insertion_sort, quicksort, heapsort
from buscar import linear_search, binary_search
from grafos import Graph


path = pathlib.Path.cwd().joinpath("valores.txt")
numeros = []

# Checamos si existe el archivo valores.txt
if not path.exists():
    raise FileNotFoundError("No se encontró el archivo valores.txt")


# Almacenamos el contenido de valores.txt en un arreglo de enteros.
with open(path) as archivo:
    for linea in archivo:
        numeros.append(int(linea.strip()))

# Ventana Principal
root = tk.Tk()
root.title("Segundo Parcial")

# Configuracion de frames y botones
# Algoritmos de ordenamiento
frm_ordenar = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_ordenar.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_ordenar.columnconfigure(0, weight=1)
frm_ordenar.columnconfigure(1, weight=1)
frm_ordenar.rowconfigure(1, weight=1)
frm_ordenar.rowconfigure(2, weight=1)
lbl_ordenar = tk.Label(text="Algoritmos de Ordenamiento", master=frm_ordenar)
lbl_ordenar.grid(column=0, row=0, columnspan=2, padx=15, pady=15)
btn_burbuja = tk.Button(text="Burbuja", master=frm_ordenar, height=5,
                        command=bubble_sort)
btn_burbuja.grid(column=0, row=1, sticky="nsew", pady=(20, 0))
btn_insercion = tk.Button(text="Insercion", master=frm_ordenar, height=5,
                          command=insertion_sort)
btn_insercion.grid(column=1, row=1, sticky="nsew", pady=(20, 0))
btn_quicksort = tk.Button(text="Quicksort", master=frm_ordenar, height=5,
                          command=quicksort)
btn_quicksort.grid(column=0, row=2, sticky="nsew", pady=(0, 20))
btn_heapsort = tk.Button(text="Heapsort", master=frm_ordenar, height=5,
                         command=heapsort)
btn_heapsort.grid(column=1, row=2, sticky="nsew", pady=(0, 20))

# Algoritmos de Búsqueda
frm_buscar = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_buscar.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_buscar.columnconfigure(0, weight=1)
lbl_buscar = tk.Label(text="Algoritmos de Búsqueda", master=frm_buscar)
lbl_buscar.grid(column=0, row=0, columnspan=2, padx=15, pady=15)
lbl_lin = tk.Label(text="Búsqueda Lineal", master=frm_buscar, relief=tk.SUNKEN)
lbl_lin.grid(column=0, row=1, columnspan=2, sticky="new", pady=(20, 0))
linear_search_val = tk.StringVar()
ent_lin = tk.Entry(master=frm_buscar, textvariable=linear_search_val)
ent_lin.grid(column=0, row=2, sticky="new", pady=(5, 5))
btn_lin = tk.Button(text="Buscar", master=frm_buscar,
                    command=lambda: linear_search(linear_search_val))
btn_lin.grid(column=1, row=2, sticky="new")
lbl_bin = tk.Label(text="Búsqueda Binaria", master=frm_buscar,
                   relief=tk.SUNKEN)
lbl_bin.grid(column=0, row=3, columnspan=2, sticky="new")
binary_search_val = tk.StringVar()
ent_bin = tk.Entry(master=frm_buscar, textvariable=binary_search_val)
ent_bin.grid(column=0, row=4, sticky="new", pady=(5, 5))
btn_bin = tk.Button(text="Buscar", master=frm_buscar,
                    command=lambda: binary_search(binary_search_val))
btn_bin.grid(column=1, row=4, sticky="new")

# Algoritmos con Grafos
graph = Graph(10)
frm_grafos = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_grafos.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_grafos.columnconfigure(0, weight=1)
frm_grafos.rowconfigure(1, weight=1)
lbl_grafos = tk.Label(text="Algoritmos con Grafos", master=frm_grafos)
lbl_grafos.grid(column=0, row=0, padx=15, pady=15)
btn_kruskal = tk.Button(text="Algoritmo de Kruskal", master=frm_grafos,
                        height=5, command=graph.kruskal)
btn_kruskal.grid(column=0, row=1, sticky="nsew", pady=(35, 35))

root.mainloop()  # Loop Principal
