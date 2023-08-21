N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for i in range(N-1):
    for j in range(i+1):
        if dp[i-j][j] == 0:
            continue
        if 0 <= i-j+arr[i-j][j] < N:
            dp[i-j+arr[i-j][j]][j] += dp[i-j][j]
        if 0 <= j+arr[i-j][j] < N:
            dp[i-j][j+arr[i-j][j]] += dp[i-j][j]
for i in range(N, 1, -1):
    for j in range(i):
        if dp[N-1-j][N-i+j] == 0:
            continue
        if 0 <= N-1-j+arr[N-1-j][N-i+j] < N:
            dp[N-1-j+arr[N-1-j][N-i+j]][N-i+j] += dp[N-1-j][N-i+j]
        if 0 <= N-i+j+arr[N-1-j][N-i+j] < N:
            dp[N-1-j][N-i+j+arr[N-1-j][N-i+j]] += dp[N-1-j][N-i+j]
print(dp[N-1][N-1])