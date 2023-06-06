# 피보나치 수를 행렬의 거듭제곱을 통해 계산할 수 있음
# [[F(n+1), Fn], [Fn, F(n-1)]] = [[1, 1], [1, 0]]**n
n = int(input())
matrix = [[1, 1], [1, 0]]


def mul(mat1, mat2):
    nmat = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                nmat[i][j] += mat1[i][k] * mat2[k][j] % 1000000007
    return nmat


def power(mat, t):
    if t == 1:
        return mat
    else:
        tmp = power(mat, t//2)
        if t%2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), mat)


result = power(matrix, n)
print(result[0][1] % 1000000007)