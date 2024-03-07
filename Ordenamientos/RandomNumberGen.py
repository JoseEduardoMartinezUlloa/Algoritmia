import random

inc = [5, 10, 100, 1000, 10000, 100000]

for i in range(0, 6):
    with open("Random100000_10.txt","a") as f:
        j = random.randint(1, inc[i]) # Rango de un millon para aumentar la entropia
        print("%s" % (j), file=f);
        
