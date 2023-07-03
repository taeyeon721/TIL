import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1, N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][2] = min(dp[i-1][j+1][1], dp[i-1][j+1][0]) + arr[i-1][j]
        if 0 < j:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + arr[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i-1][j]

ans = float('inf')
for lst in dp[N]:
    if ans > min(lst):
        ans = min(lst)
print(ans)