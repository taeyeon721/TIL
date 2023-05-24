n = int(input())
lst = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0], dp[1][0] = lst[0], lst[0]
for i in range(n-1):
    dp[0][i+1] = max(lst[i+1], dp[0][i]+lst[i+1])
for i in range(n-1):
    dp[1][i+1] = max(dp[0][i], dp[1][i]+lst[i+1])
print(max(max(dp[0]), max(dp[1])))