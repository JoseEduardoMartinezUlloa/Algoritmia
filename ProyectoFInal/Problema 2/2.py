import random
def generar_entrada():
    try:
        cant_num = int(input("ingrese la cantidad de tarjetas a crear: "))
        if cant_num <= 0 or cant_num > 1000:
            print("solo se admiten valores entre 1 y 1000.")
            return
        with open("Problema 2\\tarjetas.in", "w") as entradaw:
            entradaw.write(f"{cant_num}\n")
            for _ in range(cant_num):
                ran_num = random.randint(1, 200000)
                entradaw.write(f"{ran_num}\n")
        print(f"se generaron {cant_num} valores aleatorios en el archivo 'tarjetas.in'.")
    except ValueError:
        print("debe ingresar un número válido.")

def eliminar_tarjetas(n, tarjetas):
    # creamos una lista de longitud n donde almacenaremos la longitud máxima de la subsecuencia creciente hasta el índice i
    lis = [1] * n
    
    # inicializamos la lista de padres con índices invalidos (-1)
    parent = [-1] * n
    
    #iterando de  indices 1 a n-1
    for i in range(1, n):
        #iterando por cada i indices de 0 a i-1
        for j in range(0, i):
            if tarjetas[i] > tarjetas[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                parent[i] = j
    
    # encontramos la longitud máxima de la subsecuencia creciente
    max_lis = max(lis)
    
    # encontramos el índice del último elemento de la subsecuencia creciente más larga
    max_index = lis.index(max_lis)
    
    # reconstruimos la subsecuencia creciente
    secuencia = []
    while max_index >= 0:
        secuencia.append(max_index)
        max_index = parent[max_index]
    
    # devolvemos la longitud de la subsecuencia creciente y la subsecuencia misma
    return max_lis, sorted(secuencia)

def main():
    generar_entrada()
    # leer la entrada
    with open("Problema 2\\tarjetas.in", "r") as entrada:
        n = int(entrada.readline())
        tarjetas = [int(entrada.readline()) for _ in range(n)]
    
    # calcular las tarjetas a eliminar
    _, tarjetas_restantes = eliminar_tarjetas(n, tarjetas)
    
    # escribir la salida
    with open("Problema 2\\tarjetas.out", "w") as salida:
        salida.write(str(len(tarjetas_restantes)) + "\n")
        for i, tarjeta in enumerate(tarjetas_restantes, start=1):
            salida.write(f"{tarjeta+1} ({tarjetas[tarjeta]})\n")  # número de índice (tarjeta) a la izquierda y valor de la tarjeta a la derecha
    print(f"se generaron los resultados en el archivo 'tarjetas.out'.")

if __name__ == "__main__":
    main()




