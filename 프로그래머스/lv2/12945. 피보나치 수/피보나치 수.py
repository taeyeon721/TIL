def solution(n):
    matrix = [[1, 1], [1, 0]]
    ans = power(matrix, n)
    answer = ans[1][0]%1234567
    return answer


def power(mat, n):
    if n == 1:
        return mat
    else:
        tmp = power(mat, n//2)
        if n%2 == 1:
            return mul(mul(tmp, tmp), mat)
        else:
            return mul(tmp, tmp)
    
    
def mul(mat1, mat2):
    nmat = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                nmat[i][j] += mat1[i][k]*mat2[k][j]%1234567
    return nmat