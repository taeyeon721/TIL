import sys
input = sys.stdin.readline
N, x, P = map(int, input().split())
lst = []
if N != 0:
    lst = list(map(int, input().split()))
lst.append(x)
lst.sort(reverse=True)
ans = lst.index(x)+1
if len(lst) > P:
    if lst[-1] == x:
        ans = -1
print(ans)