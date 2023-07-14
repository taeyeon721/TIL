import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
inc = [1]*N
dec = [1]*N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if lst[N-i-1] > lst[N-j-1]:
            dec[N-i-1] = max(dec[N-i-1], dec[N-j-1]+1)
dp = [0]*N
for i in range(N):
    dp[i] = inc[i]+dec[i]-1
print(max(dp))