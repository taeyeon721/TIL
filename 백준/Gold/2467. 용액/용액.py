import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
s = 0
e = N-1
ans = [lst[s], lst[e]]
minV = 10**10
while s < e:
    tmp = lst[s] + lst[e]
    if abs(tmp) <= minV:
        minV = abs(tmp)
        ans = [lst[s], lst[e]]

    if tmp < 0:
        s += 1
    else:
        e -= 1
print(*ans)