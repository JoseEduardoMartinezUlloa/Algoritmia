import random

cant=100000

for i in range(1, cant+1):
    with open("Random100000_10.txt","a") as f:
        j = random.randint(1, 1000000) # Rango de un millon para aumentar la entropia
        print("%s" % (j), file=f);
        