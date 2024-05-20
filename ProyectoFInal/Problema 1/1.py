import itertools

def generar_tableros(N, M):
    tablero = [0] * (N * N)
    for posiciones in itertools.combinations(range(N * N), M):
        for pos in posiciones:
            tablero[pos] = 1
        yield tablero
        for pos in posiciones:
            tablero[pos] = 0

def es_valido(tablero, N):
    for i in range(N):
        for j in range(N):
            if tablero[i*N + j] == 1:
                if any(tablero[(i+dx)*N + (j+dy)] == 1 for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)] if 0 <= i+dx < N and 0 <= j+dy < N):
                    return False
    return True

def resolver(N):
    M = N if N % 2 == 0 else N - 1
    soluciones = []
    for tablero in generar_tableros(N, M):
        if es_valido(tablero, N):
            soluciones.append(tablero[:])
            if len(soluciones) == 10:
                break
    return M, soluciones

def imprimir_soluciones(N, M, soluciones):
    with open(f'Problema 1\\CABAL_{N:02}.TXT', 'w') as f:
        f.write(str(M) + '\n')
        f.write(str(len(soluciones)) + '\n')
        for solucion in soluciones:
            for i in range(N):
                f.write(' '.join(str(solucion[i*N + j]) for j in range(N)) + '\n')
            f.write('\n')

def main():
    print("Ingrese el tamaño del tablero: ")
    N = int(input())
    if N < 1 or N > 20:
        print("El tamaño del tablero debe estar entre 1 y 20.")
        return
    M, soluciones = resolver(N)
    imprimir_soluciones(N, M, soluciones)

if __name__ == '__main__':
    main()
