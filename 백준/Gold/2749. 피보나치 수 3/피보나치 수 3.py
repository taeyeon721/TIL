def mul(mat1, mat2):
    nmat = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                nmat[i][j] += mat1[i][k]*mat2[k][j] % 1000000
    return nmat


def power(mat, b):
    if b == 1:
        return mat
    else:
        tmp = power(mat, b//2)
        if b%2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)


n = int(input())
matrix = [[1, 1], [1, 0]]
ans = power(matrix, n)
print(ans[1][0]%1000000)
