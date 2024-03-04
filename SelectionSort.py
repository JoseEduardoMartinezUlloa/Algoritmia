#Selection Sort Reading From InputFiles Folder
# Tracks Execution Time, Asignations and Comparisons

import datetime
import time

start_time = time.time()

arr = []
i = 0
inc = [5, 10, 100, 1000, 10000, 100000]

InpFile = "Ordenamientos/InputFiles/Random{incid}_{id}.txt"
OutFile = "Ordenamientos/Stats/SelectionSortStatst.txt"

def selectionSort(array, size, id):
    comp = 0
    asign = 0
    
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            comp+=1
            if array[j] < array[min_index]: # select the minimum element in every iteration
                min_index = j
        asign+=2
        (array[ind], array[min_index]) = (array[min_index], array[ind]) # swapping the elements to sort the array
    
    with open(OutFile, "a") as sFile:
        print(InpFile.format(id = id), file=sFile)
        print("Tiempo de Ejecucion\t\tComparaciones\tAsignaciones", file=sFile)
        print("%s\t\t\t%s\t%s\n" % (time.time()-start_time,comp,asign), file=sFile)

for c in range(0,6):
    for a in range(1,11):
        inp = open (InpFile.format(incid=inc[c],id = a),"r")
        for line in inp.readlines(): #Read line into array
            for i in line.split(): #loop over the elemets, split by whitespace
                arr.append(int(i)) #convert to integer and append to the list      
        inp.close()
        print(arr)
        selectionSort(arr, len(arr), a)
        print(arr)
        
