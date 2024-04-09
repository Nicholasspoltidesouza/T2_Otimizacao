import sys
def recursivo_memorizacao(file_path):
    with open(file_path, 'r') as file:
        m, n = map(int, file.readline().split())
        grid = []
        for _ in range(m):
            row = list(map(int, file.readline().split()))
            grid.append(row)

    def recursivo_memorizacao(m, n, grid, i=0, j=0, memo=None):
        if memo is None:
            memo = {}
        if (i, j) in memo:
            return memo[(i, j)]
        if i == m - 1 and j == n - 1:  # Chegou ao destino
            return 1
        if i >= m or j >= n or grid[i][j] == 1:  # Fora dos limites ou posição bloqueada
            return 0
        memo[(i, j)] = recursivo_memorizacao(m, n, grid, i + 1, j, memo) + recursivo_memorizacao(m, n, grid, i, j + 1, memo)
        return memo[(i, j)]

    return recursivo_memorizacao(m, n, grid)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]
    print("Recursão com Memoria:", recursivo_memorizacao(file_path))

