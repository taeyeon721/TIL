import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = 1000001
ans = INF
for i in range(3):
    dp = [[0]*3 for _ in range(N)]
    dp[0] = [INF, INF, INF]
    dp[0][i] = arr[0][i]
    for j in range(1, N):
        dp[j][0] = arr[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = arr[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = arr[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    dp[N-1][i] = INF
    ans = min(ans, min(dp[N-1]))
print(ans)