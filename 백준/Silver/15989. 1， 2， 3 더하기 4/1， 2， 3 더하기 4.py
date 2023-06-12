import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [1]*(n+1)
    k = 1
    cnt = 1
    for i in range(1, n+1):
        if cnt == 6:
            cnt = 0
            k += 1
        if i % 6 == 1:
            dp[i] = dp[i - 1] + k - 1
        else:
            dp[i] = dp[i-1] + k
        cnt += 1
    print(dp[n])