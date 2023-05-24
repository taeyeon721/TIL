import sys


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    x = find(x)
    y = find(y)
    rep[max(x, y)] = min(x, y)


input = sys.stdin.readline
N = int(input())
edge = []
ans = 0
for i in range(N):
    lst = list(input())
    for j in range(N):
        if lst[j] == '0':
            continue
        w = ord(lst[j])
        if w > 96:
            w -= 96
        else:
            w -= 38
        edge.append([i, j, w])
        ans += w
edge.sort(key=lambda x: x[2])
rep = [i for i in range(N)]

cnt = 0
for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans -= c
        if cnt == N-1:
            break
for i in set(rep):
    if find(i) != 0:
        ans = -1
        break
print(ans)