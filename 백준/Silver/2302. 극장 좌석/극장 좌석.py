import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
dp = [1]*41
lst = [0]+[int(input()) for _ in range(M)]+[N+1]
ans = 1
for i in range(2, 41):
    dp[i] = dp[i-1]+dp[i-2]
for i in range(1, M+2):
    n = lst[i]-lst[i-1]-1
    ans *= dp[n]
print(ans)