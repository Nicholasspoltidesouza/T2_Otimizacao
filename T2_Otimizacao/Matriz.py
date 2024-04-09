import sys

def matriz(file_path):
    with open(file_path, 'r') as file:
        m, n = map(int, file.readline().split())
        grid = []
        for _ in range(m):
            row = list(map(int, file.readline().split()))
            grid.append(row)

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py file_path")
        sys.exit(1)

    file_path = sys.argv[1]
    print("Matriz de Resultados:", matriz(file_path))
