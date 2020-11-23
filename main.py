""" Técnicas Algorítmicas Evaluación Segundo Parcial
Equipo: Iñaki Cornejo, Wenceslao Trejo, Adolfo Tun y Fernando Manzano"""

import pathlib
import tkinter as tk
import json
from mergesort import *
from points import *
from suma_max import suma_max
from karatsuba import karatsuba
from factorial import factorial
from fibonacci import fibonacci
from hanoi import hanoi
from pascal import pascal

path = pathlib.Path.cwd().joinpath("valores.txt")

# Checamos si existe el archivo valores.txt
if not path.exists():
    raise FileNotFoundError("No se encontró el archivo valores.txt")


# Almacenamos el contenido de valores.txt en un arreglo de enteros.
with open(path, 'r') as file:
    numeros = json.load(file)

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
btn_closest = tk.Button(text="Puntos\nmás cercanos", master=frm_dv, height=5,
                          command=lambda: closest_points(numeros))
btn_closest.grid(column=1, row=1, sticky="nsew", pady=(20, 0))
btn_sum = tk.Button(text="Suma máxima\n de un arreglo", master=frm_dv,
                          height=5, command=lambda: suma_max(numeros))
btn_sum.grid(column=0, row=2, sticky="nsew", pady=(0, 20))
btn_karatsuba = tk.Button(text="Karatsuba", master=frm_dv, height=5,
                         command=lambda: karatsuba(numeros[:100_000]))
btn_karatsuba.grid(column=1, row=2, sticky="nsew", pady=(0, 20))

# Algoritmos Recursivos
frm_recur = tk.Frame(relief=tk.GROOVE, borderwidth=2)
frm_recur.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_recur.columnconfigure(0, weight=1)
frm_recur.columnconfigure(1, weight=1)
frm_recur.rowconfigure(1, weight=1)
frm_recur.rowconfigure(2, weight=1)
lbl_recur = tk.Label(text="Algoritmos Recursivos", master=frm_recur)
lbl_recur.grid(column=0, row=0, columnspan=2, padx=15, pady=15)
btn_factorial = tk.Button(text="Factorial", master=frm_recur, height=5,
                          command=factorial)
btn_factorial.grid(column=0, row=1, sticky="nsew", pady=(20, 0))
btn_fib = tk.Button(text="Fibonacci", master=frm_recur, height=5,
                          command=fibonacci)
btn_fib.grid(column=1, row=1, sticky="nsew", pady=(20, 0))
btn_hanoi = tk.Button(text="Torres de Hanoi", master=frm_recur,
                          height=5, command=lambda: hanoi(22))
btn_hanoi.grid(column=0, row=2, sticky="nsew", pady=(0, 20))
btn_pascal = tk.Button(text="Triangulo de\nPascal", master=frm_recur, height=5,
                         command=lambda: pascal(2_000))
btn_pascal.grid(column=1, row=2, sticky="nsew", pady=(0, 20))

root.mainloop()  # Loop Principal
