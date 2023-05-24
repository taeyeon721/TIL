import sys
input = sys.stdin.readline
M = int(input())
lst = list(map(int, input().split()))
K = int(input())


def combination(n, r):
    c = 1
    for i in range(n-r+1, n+1):
        c *= i
    for i in range(1, r+1):
        c //= i
    return c


ans = 0
for num in lst:
    if num >= K:
        ans += combination(num, K)
print(ans/combination(sum(lst), K))