import sys

input = sys.stdin.readline
N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if not g[i][j]:
                if g[i][k] == 1 and g[k][j] == 1:
                    g[i][j] = 1
for i in range(N):
    print(*g[i])