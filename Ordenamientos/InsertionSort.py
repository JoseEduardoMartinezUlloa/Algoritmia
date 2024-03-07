#Selection Sort Reading From InputFiles Folder
#Tracks Execution Time, Assignations and Comparisons

import datetime
import time

arr=[]
inc=[5,10,100,1000,10000,100000]

start_time = time.time()
restantes = ["Orden","Reverso"]
InpFileR = "Ordenamientos/InputFiles/Random{incid}_{id}.txt"
InpFileOtros = "Ordenamientos/InputFiles/{nombre}{incid}.txt"
OutFile = "Ordenamientos/Stats/InsertionSortStats.txt"

def insertionSort(arr, nombreArchivo):
    comp=0
    asign=0
    n = len(arr)  # Get the length of the array
    
    if n <= 1: return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        comp+=1
        while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
            asign+=1
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        asign+=1
        arr[j+1] = key
    with open(OutFile, "a") as sFile:
        print(nombreArchivo, file=sFile)
        print("Tiempo de Ejecucion\t\tComparaciones\tAsignaciones", file=sFile)
        print("%s\t\t\t%s\t%s\n" % (time.time()-start_time,comp,asign), file=sFile)
        
def release_list(a):
   del a[:]
   del a
   
def salida(nombreArchivo):
    inp = open (nombreArchivo,"r")
    for line in inp.readlines(): #Read line into array
        for i in line.split(): #loop over the elemets, split by whitespace
            arr.append(int(i)) #convert to integer and append to the list      
    inp.close()
    print(arr)
    start_time = time.time() 
    insertionSort(arr, nombreArchivo)
    print(arr)
    release_list(arr)
    
for c in range(0,6):
    
    for a in range(1,11):
        nombreArchivo = InpFileR.format(incid=inc[c],id = a)
        salida(nombreArchivo)
    
    for m, n  in enumerate(restantes):
        nombreArchivo = InpFileOtros.format(nombre=n,incid=inc[c])
        salida(nombreArchivo) 