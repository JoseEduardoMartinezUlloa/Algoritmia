def tromino_tiling(n, hole_x, hole_y, output_file):
    size = 2**n
    board = [[0] * size for _ in range(size)]
    tiles = []
    tile_count = 0

    def place_tile(x, y, pos):
        nonlocal tile_count
        tile_count += 1
        tiles.append((x, y, pos))
        if pos == "AI":
            board[x][y+1] = board[x+1][y] = board[x+1][y+1] = tile_count
        elif pos == "AD":
            board[x][y] = board[x+1][y] = board[x+1][y+1] = tile_count
        elif pos == "BI":
            board[x][y] = board[x][y+1] = board[x+1][y+1] = tile_count
        elif pos == "BD":
            board[x][y] = board[x][y+1] = board[x+1][y] = tile_count

    def cover_board(top_x, top_y, size, hole_x, hole_y):
        if size == 2:
            if hole_x < top_x + 1 and hole_y < top_y + 1:
                place_tile(top_x, top_y, "BD")
            elif hole_x < top_x + 1 and hole_y >= top_y + 1:
                place_tile(top_x, top_y, "AD")
            elif hole_x >= top_x + 1 and hole_y < top_y + 1:
                place_tile(top_x, top_y, "BI")
            else:
                place_tile(top_x, top_y, "AI")
            return
        
        mid_x, mid_y = top_x + size // 2, top_y + size // 2
        if hole_x < mid_x and hole_y < mid_y:
            place_tile(mid_x-1, mid_y-1, "BD")
            cover_board(top_x, top_y, size//2, hole_x, hole_y)
            cover_board(top_x, mid_y, size//2, mid_x-1, mid_y)
            cover_board(mid_x, top_y, size//2, mid_x, mid_y-1)
            cover_board(mid_x, mid_y, size//2, mid_x, mid_y)
        elif hole_x < mid_x and hole_y >= mid_y:
            place_tile(mid_x-1, mid_y-1, "AD")
            cover_board(top_x, top_y, size//2, mid_x-1, mid_y-1)
            cover_board(top_x, mid_y, size//2, hole_x, hole_y)
            cover_board(mid_x, top_y, size//2, mid_x, mid_y-1)
            cover_board(mid_x, mid_y, size//2, mid_x, mid_y)
        elif hole_x >= mid_x and hole_y < mid_y:
            place_tile(mid_x-1, mid_y-1, "BI")
            cover_board(top_x, top_y, size//2, mid_x-1, mid_y-1)
            cover_board(top_x, mid_y, size//2, mid_x-1, mid_y)
            cover_board(mid_x, top_y, size//2, hole_x, hole_y)
            cover_board(mid_x, mid_y, size//2, mid_x, mid_y)
        else:
            place_tile(mid_x-1, mid_y-1, "AI")
            cover_board(top_x, top_y, size//2, mid_x-1, mid_y-1)
            cover_board(top_x, mid_y, size//2, mid_x-1, mid_y)
            cover_board(mid_x, top_y, size//2, mid_x, mid_y-1)
            cover_board(mid_x, mid_y, size//2, hole_x, hole_y)
    
    cover_board(0, 0, size, hole_x-1, hole_y-1)
    
    with open(output_file, 'w') as f:
        f.write(f"{tile_count}\n")
        for tile in tiles:
            f.write(f"{tile[0] + 1} {tile[1] + 1} {tile[2]}\n")

# Lectura del archivo de entrada
def leer_archivo(archivo):
    with open(archivo, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        x, y = map(int, lines[1].strip().split())
    return n, x, y

def main():
    archivo_salida = 'Problema 3\\tablero.out'  # Nombre del archivo de salida
    archivo_entrada = 'Problema 3\\tablero.in'  # Nombre del archivo de entrada

    # Solicitar al usuario que ingrese el tamaño del tablero
    n = int(input("Por favor, ingresa el tamaño del tablero (n): "))

    # Solicitar al usuario que ingrese las coordenadas del agujero
    x = int(input("Por favor, ingresa la coordenada x del agujero: "))
    y = int(input("Por favor, ingresa la coordenada y del agujero: "))

    # Escribir las entradas del usuario en el archivo de entrada
    with open(archivo_entrada, 'w') as f:
        f.write(f"{n}\n{x} {y}\n")

    tromino_tiling(n, x, y, archivo_salida)

if __name__ == "__main__":
    main()
