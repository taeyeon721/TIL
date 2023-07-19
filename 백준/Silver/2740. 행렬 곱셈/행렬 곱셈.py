import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mat1 = []
for _ in range(N):
    lst = list(map(int, input().split()))
    mat1.append(lst)
M, K = map(int, input().split())
mat2 = []
for _ in range(M):
    lst = list(map(int, input().split()))
    mat2.append(lst)

ans = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            ans[i][j] += mat1[i][k] * mat2[k][j]
for i in range(N):
    print(*ans[i])