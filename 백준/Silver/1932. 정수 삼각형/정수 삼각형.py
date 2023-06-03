import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*N for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    if i == 0:
        dp[i][0] = lst[0]
    else:
        dp[i][0] = lst[0] + dp[i-1][0]
    for j in range(i):
        if j == i-1:
            dp[i][j+1] = dp[i-1][j] + lst[i]
        else:
            dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1]) + lst[j+1]
print(max(dp[N-1]))