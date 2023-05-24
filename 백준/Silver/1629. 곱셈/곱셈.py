def f(i, j, k):
    if i == 1 or j == 1:
        return i % k
    elif j % 2 == 0:
        n = f(i, j//2, k)
        return (n * n) % k
    else:
        return (i * f(i, j-1, k)) % k


A, B, C = map(int, input().split())
print(f(A, B, C))