def mul(mat1, mat2):
    nmat = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                nmat[i][j] += (mat1[i][k]*mat2[k][j])%1000
    return nmat


def power(mat, b):
    if b == 1:
        return mat
    else:
        tmp = power(mat, b//2)
        if b % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = power(matrix, B)
for i in range(N):
    for j in range(N):
        print(answer[i][j] % 1000, end=' ')
    print()