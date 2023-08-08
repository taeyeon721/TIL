def power(X, Y):
    if X == 1:
        return Y
    else:
        tmp = power(X//2, Y)
        if X % 2 == 1:
            return tmp*tmp*Y%C
        else:
            return tmp*tmp%C


A, B, C = map(int, input().split())
ans = power(B, A)
print(ans%C)