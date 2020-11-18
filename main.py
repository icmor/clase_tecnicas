""" Técnicas Algorítmicas Evaluación Segundo Parcial
Equipo: Iñaki Cornejo, Wenceslao Trejo, Adolfo Tun y Fernando Manzano"""

import pathlib
import tkinter as tk
from buscar import linear_search, binary_search
from mergesort import *
from points import *

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
root.title("Tercer Parcial")

# Configuracion de frames y botones
# Algoritmos Divide y Venceras
frm_dv = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_dv.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_dv.columnconfigure(0, weight=1)
frm_dv.columnconfigure(1, weight=1)
frm_dv.rowconfigure(1, weight=1)
frm_dv.rowconfigure(2, weight=1)
lbl_dv = tk.Label(text="Algoritmos Divide y Venceras", master=frm_dv)
lbl_dv.grid(column=0, row=0, columnspan=2, padx=15, pady=15)
btn_mergesort = tk.Button(text="Mergesort", master=frm_dv, height=5,
                          command=lambda: call_mergesort(numeros.copy()))
btn_mergesort.grid(column=0, row=1, sticky="nsew", pady=(20, 0))
btn_closest = tk.Button(text="Puntos", master=frm_dv, height=5,
                          command=closest_points)
btn_closest.grid(column=1, row=1, sticky="nsew", pady=(20, 0))
btn_quicksort = tk.Button(text="Quicksort", master=frm_dv, height=5,
                          command=lambda: quicksort(numeros.copy()))
btn_quicksort.grid(column=0, row=2, sticky="nsew", pady=(0, 20))
btn_heapsort = tk.Button(text="Heapsort", master=frm_dv, height=5,
                         command=lambda: heapsort(numeros.copy()))
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
                    command=lambda: linear_search(linear_search_val, numeros))
btn_lin.grid(column=1, row=2, sticky="new")
lbl_bin = tk.Label(text="Búsqueda Binaria", master=frm_buscar,
                   relief=tk.SUNKEN)
lbl_bin.grid(column=0, row=3, columnspan=2, sticky="new")
binary_search_val = tk.StringVar()
ent_bin = tk.Entry(master=frm_buscar, textvariable=binary_search_val)
ent_bin.grid(column=0, row=4, sticky="new", pady=(5, 5))
btn_bin = tk.Button(text="Buscar", master=frm_buscar,
                    command=lambda: binary_search(binary_search_val, numeros))
btn_bin.grid(column=1, row=4, sticky="new")

# Algoritmos con Grafos
frm_grafos = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_grafos.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_grafos.columnconfigure(0, weight=1)
frm_grafos.rowconfigure(1, weight=1)
lbl_grafos = tk.Label(text="Algoritmos con Grafos", master=frm_grafos)
lbl_grafos.grid(column=0, row=0, padx=15, pady=15)
btn_kruskal = tk.Button(text="Algoritmo de Kruskal", master=frm_grafos,
                        height=5, command=kruskal)
btn_kruskal.grid(column=0, row=1, sticky="nsew", pady=(35, 35))

root.mainloop()  # Loop Principal
