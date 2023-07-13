import sys
input = sys.stdin.readline
st1 = input().strip()
st2 = input().strip()
dp = [[0]*(len(st1)+1) for _ in range(len(st2)+1)]
for i in range(1, len(st2)+1):
    for j in range(1, len(st1)+1):
        if st1[j-1] == st2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(st2)][len(st1)])