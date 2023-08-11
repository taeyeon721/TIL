def mul(mat1, mat2):
    nmat = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                nmat[i][j] += mat1[i][k]*mat2[k][j]%mod
    return nmat


def power(mat, t):
    if t == 1:
        return mat
    else:
        tmp = power(mat, t//2)
        if t%2:
            return mul(mul(tmp, tmp), mat)
        else:
            return mul(tmp, tmp)


a, b = map(int, input().split())
matrix = [[1, 1], [1, 0]]
mod = 10**9
A = power(matrix, a+1)
B = power(matrix, b+2)
ans = (B[0][1]-A[0][1]+mod)%mod
print(ans)