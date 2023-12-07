N, K = map(int, input().split())
p = 1000000007


def f(n):
    x = 1
    for i in range(2, n+1):
        x = (x * i) % p
    return x


def power(n, r):
    if r == 1:
        return n
    else:
        tmp = power(n, r//2)
        if r % 2:
            return tmp * tmp * n % p
        else:
            return tmp * tmp % p


ans = f(N) * power(f(N-K) * f(K) % p, p-2) % p
print(ans)
