# Python Tutorial

# Tipos de datos
ints = 10
floats = 10.0
strings = "Hola"
booleans = True
booleans = False
tipo_none = None
lista = [10, "hola", 10.32]
print(lista)

# Operaciones datos
## Misma interface entre objetos
10 == 10.0
[32, 213] == [10, 100, 12343]
[596] + [12, 32]
"hello" + " world"

## Aritmetica basica
+ - * / () // ** %

## Operaciones con listas
lista[0] #Acceder primer elemento
start = 0
end = 2
lista[start:end] # Retorna una lista con los valores
                 # desde start hasta end sin incluir end
len(lista)  #length tamaño de lista
lista.append(10, 20, 30) # añadir elemento al final
lista + [10, 32] # Concatenar listas
lista.sort() # Ordenar Listas

# Control de flujo
if x == 5:
    print("x es igual a 5")
elif x == 10:
    print("x es igual a 10")
else:
    print("x no es 5")

## Operadores Condicionales
==
!=
>
<
>=
<=
and
or
not
in

# Loops
while condicion:
    pass

for i in range(start, stop, step):
    pass

for i in lista:

continue
break

# Input Output
print()
input()

# Funciones
def foo (x, y, z):
    return x

file = with open("valores.txt") as file:
# Buenas practicas

lista = [] # lista vacia

# Rellena lista
for linea in file:
    lista.append(int(linea.strip()))
