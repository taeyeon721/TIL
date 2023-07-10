import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
s = sorted(list(set(lst)))
ans = {s[i]: i for i in range(len(s))}
for num in lst:
    print(ans[num], end=' ')