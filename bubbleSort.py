# Adolfo Tun estuvo aqui XD
# Metodo burbuja
with open("valores.txt") as file:
    lista = []

    for i in file:
        lista.append(int(i.strip()))

# funcion ordena
def bubbleSort(arreglo): 
    
    tamano = len(arreglo) 
  
    for i in range(0, tamano): 
     
        for j in range(0, tamano-1): 
  
            if arreglo[j] > arreglo[j+1] : 
                
                temporal = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temporal

# retorna un vector ordenado
bubbleSort(lista)

# se imprime el vector como comprobación
print ("El vector esta arreglado:") 
for i in range(len(lista)): 
    print ("%d" %lista[i]),

# revisar el almacenamiento del vector en el
# nuevo archivo.txt (bubbleSort.txt)
with open("bubbleSort.txt", "w") as file02:
    file02.write("---- Vector ordenado: ----\n")
    file02.write('%s\n' %lista)
    file02.close() 