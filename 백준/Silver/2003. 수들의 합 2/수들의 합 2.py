import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
s = 0
e = 1
ans = 0
while e <= N and s <= e:
    tmp = sum(lst[s:e])
    if tmp == M:
        ans += 1
        s += 1
        e += 1
    elif tmp < M:
        e += 1
    else:
        s += 1
print(ans)