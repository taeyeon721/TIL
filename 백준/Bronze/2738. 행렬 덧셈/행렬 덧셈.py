N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(N)]
mat2 = [list(map(int, input().split())) for _ in range(N)]
nmat = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        nmat[i][j] = mat1[i][j] + mat2[i][j]
for i in range(N):
    print(*nmat[i])