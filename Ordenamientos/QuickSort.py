# Quick Sort Reading form InputFiles folder
# Tracks Execution Time, Assignations and Comparisons

import datetime
import time

start_time = time.time()

arr = []
inc = [5, 10, 100, 1000, 10000, 100000]

comp=0
asign=0

restantes = ["Orden","Reverso"]
InpFileR = "Ordenamientos/InputFiles/Random{incid}_{id}.txt"
InpFileOtros = "Ordenamientos/InputFiles/{nombre}{incid}.txt"
OutFile = "Ordenamientos/Stats/QuickSortStats.txt"

def release_list(a):
   del a[:]
   del a
   
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        comp+=1
        if array[j] <= pivot:
            i = i + 1
            asign+=2
            (array[i], array[j]) = (array[j], array[i])
    asign+=2
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1

def quickSort(array, low, high, nombreArchivo):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1, nombreArchivo)
        quickSort(array, pi + 1, high, nombreArchivo) 
    else:
        with open(OutFile, "a") as sFile:
            print(nombreArchivo, file=sFile)
            print("Tiempo de Ejecucion\t\tComparaciones\tAsignaciones", file=sFile)
            print("%s\t\t\t%s\t%s\n" % (time.time()-start_time,comp,asign), file=sFile)       

def salida(nombreArchivo):
    inp = open (nombreArchivo,"r")
    for line in inp.readlines(): #Read line into array
        for i in line.split(): #loop over the elemets, split by whitespace
            arr.append(int(i)) #convert to integer and append to the list      
    inp.close()
    start_time = time.time() 
    print(arr)
    quickSort(arr, 0, len(arr)-1, nombreArchivo)
    print(arr)
    
for c in range(0,6):
    
    for a in range(1,11):
        nombreArchivo = InpFileR.format(incid=inc[c],id = a)
        salida(nombreArchivo)
    
    for m, n  in enumerate(restantes):
        nombreArchivo = InpFileOtros.format(nombre=n,incid=inc[c])
        salida(nombreArchivo) 
