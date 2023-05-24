def f(n, w):
    global ans
    if w < 500:
        return
    if n == N:
        ans += 1
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                f(n+1, w-K+A[i])
                visited[i] = 0


N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
visited = [0]*N
f(0, 500)
print(ans)