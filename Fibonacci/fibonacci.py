#Programa recursivo para obtener tiempos de posiciones de Fibonacci recursivamente
# Jose Eduardo Martinez Ulloa 25-02-24

import datetime
import time

start_time = time.time()

def recur_fibo(n):
    c = 0
    if n <= 1:
       return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
   

numPos = 2

if numPos <= 0:
   print("Favor de ingresar un numero positivo.")
else:
   print("Fibonacci sequence:")
   for i in range(numPos):
       print(recur_fibo(i))
       with open("Tiempos.txt", "a") as f:
            print("%s seconds " % (time.time() - start_time), file=f)