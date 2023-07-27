import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
M = int(input())
dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1
for i in range(2, N):
    for j in range(N-i):
        if dp[j+1][i+j-1] == 1 and lst[j] == lst[i+j]:
            dp[j][i+j] = 1
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])