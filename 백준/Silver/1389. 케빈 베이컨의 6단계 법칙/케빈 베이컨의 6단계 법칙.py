import sys

input = sys.stdin.readline
INF = 10**9
N, M = map(int, input().split())
k_b = [[INF]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    k_b[a-1][b-1] = 1
    k_b[b-1][a-1] = 1
for i in range(N):
    k_b[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and k_b[i][k] != 0 and k_b[k][j] != 0:
                k_b[i][j] = min(k_b[i][j], k_b[i][k]+k_b[k][j])
minV = INF
ans = 0
for i in range(N):
    if minV > sum(k_b[i]):
        minV = sum(k_b[i])
        ans = i
print(ans+1)