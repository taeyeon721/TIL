import sys
input = sys.stdin.readline

T = int(input())
dp = [1]*10001
k = 1
cnt = 1
for i in range(1, 10001):
    if cnt == 6:
        cnt = 0
        k += 1
    if i % 6 == 1:
        dp[i] = dp[i - 1] + k - 1
    else:
        dp[i] = dp[i-1] + k
    cnt += 1
for _ in range(T):
    n = int(input())
    print(dp[n])
