import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(N-max(dp))