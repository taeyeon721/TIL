N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]
for j in range(1, N+1):
    w, v = map(int, input().split())
    for i in range(1, K+1):
        if i-w >= 0:
            dp[i][j] = max(dp[i][j-1], dp[i-w][j-1]+v)
        else:
            dp[i][j] = dp[i][j-1]
print(dp[K][N])