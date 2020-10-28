""" Técnicas Algorítmicas Evaluación Segundo Parcial
Equipo: Iñaki Cornejo, Wenceslao Trejo, Adolfo Tun y Fernando Manzano"""

ARCHIVO = "valores.txt"
numeros = []

# Almacenamos el contenido de valores.txt en un arreglo de enteros.
with open(ARCHIVO) as archivo:
    for linea in archivo:
        numeros.append(int(linea.strip()))
