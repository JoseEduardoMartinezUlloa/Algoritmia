# Bubble Sort Reading from InputFiles folder
# Tracks Execution Time, Asignations and Comparisons

import datetime
import time

start_time = time.time()

arr = []

InpFile = "Ordenamientos\InputFiles\Reverso100000.txt"
OutFile = "Ordenamientos\Stats\BubbleSortStats.txt"

def bubbleSort(arr):
    n = len(arr)
    comp = 0
    asign = 0
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                comp+=1
                asign+=1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            comp+=1
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            with open(OutFile, "a") as sFile:
                print(InpFile, file=sFile)
                print("Tiempo de Ejecucion\t\tComparaciones\tAsignaciones", file=sFile)
                print("%s\t\t\t%s\t%s\n" % (time.time()-start_time,comp,asign), file=sFile)
            return
    

inp = open (InpFile,"r")
#read line into array 
for line in inp.readlines():
    # loop over the elemets, split by whitespace
    for i in line.split():
        # convert to integer and append to the list
        arr.append(int(i))      
inp.close()
bubbleSort(arr)


