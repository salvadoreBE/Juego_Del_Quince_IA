import heapq
from collections import deque

def manhattan_distance(tablero):
    # Heurística de distancia Manhattan
    distancia = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j] != 0:
                fila = (tablero[i][j] - 1) // 3
                columna = (tablero[i][j] - 1) % 3
                distancia += abs(fila - i) + abs(columna - j)
    return distancia

def resolver_puzzle(inicio, meta):
    # Método de búsqueda A* 
    visitado = set()
    queue = [(manhattan_distance(inicio), inicio)]
    while queue:
        _, nodo = heapq.heappop(queue)
        if nodo == meta:
            return nodo
        visitado.add(tuple(map(tuple, nodo)))
        for i, fila in enumerate(nodo):
            for j, val in enumerate(fila):
                if val == 0:
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 3 and 0 <= nj < 3:
                            nuevo_tablero = [fila[:] for fila in nodo]
                            nuevo_tablero[i][j], nuevo_tablero[ni][nj] = nuevo_tablero[ni][nj], nuevo_tablero[i][j]
                            if tuple(map(tuple, nuevo_tablero)) not in visitado:
                                prioridad = manhattan_distance(nuevo_tablero)
                                heapq.heappush(queue, (prioridad, nuevo_tablero))

def puzzle(tablero):
    for fila in tablero:
        print(fila)

if __name__ == '__main__':
    inicio = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solucion = resolver_puzzle(inicio, meta)
    puzzle(solucion)