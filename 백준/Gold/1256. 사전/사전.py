import math


def f():
    global ans, N, M, K
    F = math.factorial(N + M) // (math.factorial(N) * math.factorial(M))
    if K > F*N//(N+M):
        ans += 'z'
        K -= (F*N//(N+M))
        M -= 1
    else:
        ans += 'a'
        N -= 1
    if N == 0 or M == 0:
        return
    f()


N, M, K = map(int, input().split())
F = math.factorial(N+M)//(math.factorial(N)*math.factorial(M))
if F < K:
    print(-1)
else:
    ans = ''
    f()
    if N:
        ans += 'a'*N
    if M:
        ans += 'z'*M
    print(ans)