n = int(input())
m = int(input())
matrix = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for row in matrix:
    print(*row)

