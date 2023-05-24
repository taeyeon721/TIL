import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sumA = 0
D = [[0]*(N+1) for _ in range(N+1)]
D[1][1] = arr[0][0]
for i in range(1, N):
    D[1][i+1] = D[1][i] + arr[0][i]
    D[i+1][1] = D[i][1] + arr[i][0]
for i in range(1, N):
    for j in range(1, N):
        D[i+1][j+1] = D[i+1][j] + D[i][j+1] -D[i][j] + arr[i][j]
for _ in range(M):
    i1, j1, i2, j2 = map(int, sys.stdin.readline().split())
    print(D[i2][j2]-D[i1-1][j2]-D[i2][j1-1]+D[i1-1][j1-1])