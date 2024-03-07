# Shell Sort Reading from InputFiles folder
# Tracks Execution Time, Assignations and Comparisons

import datetime
import time
import math

start_time = time.time()

arr = []
inc = [5, 10, 100, 1000, 10000, 100000]

restantes = ["Orden","Reverso"]
InpFileR = "Ordenamientos/InputFiles/Random{incid}_{id}.txt"
InpFileOtros = "Ordenamientos/InputFiles/{nombre}{incid}.txt"
OutFile = "Ordenamientos/Stats/ShellSortStats.txt"

def release_list(a):
   del a[:]
   del a
   
def shellSort(arr, nombreArchivo):
    asign = 0
    comp =0
    n = len(arr)
    interval = n//2
    
    while interval > 0:
        for i in range(int(interval),n):
            temp = arr[i]
            j = i
            comp+=1
            while j >= interval and arr[j-int(interval)] > temp:
                asign+=1
                arr[j] = arr[j-interval]
                j -= interval
            asign+=1
            arr[j] = temp
        interval //= 2
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
    print(arr)
    start_time = time.time() 
    shellSort(arr, nombreArchivo)
    print(arr)
    release_list(arr)
    

for c in range(0,6):
    
    for a in range(1,11):
        nombreArchivo = InpFileR.format(incid=inc[c],id = a)
        salida(nombreArchivo)
    
    for m, n  in enumerate(restantes):
        nombreArchivo = InpFileOtros.format(nombre=n,incid=inc[c])
        salida(nombreArchivo) 

        

 
