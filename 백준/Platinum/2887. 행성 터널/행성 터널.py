import sys
input = sys.stdin.readline
N = int(input())
P = [list(map(int, input().split()))+[i] for i in range(N)]
arr = []
for k in range(3):
    P.sort(key=lambda x: x[k])
    for i in range(N-1):
        d = min(abs(P[i][0]-P[i+1][0]), abs(P[i][1]-P[i+1][1]), abs(P[i][2]-P[i+1][2]))
        arr.append((P[i][3], P[i+1][3], d))
arr.sort(key=lambda x: x[2])
parent = [i for i in range(N)]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


ans = 0
for a, b, c in arr:
    x = find(a)
    y = find(b)
    if x != y:
        union(a, b)
        ans += c
print(ans)