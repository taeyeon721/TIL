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
V, E = map(int, input().split())
edge = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append([A, B, C])
edge.sort(key=lambda x: x[2])
rep = [i for i in range(V+1)]

cnt = 0
w = 0
for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        w += c
        if cnt == V-1:
            break
print(w)