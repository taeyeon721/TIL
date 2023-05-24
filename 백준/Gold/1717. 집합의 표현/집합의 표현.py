import sys
sys.setrecursionlimit(10**6)


def find_root(x):
    if root[x] != x:
        root[x] = find_root(root[x])
    return root[x]


def union(x, y):
    x = find_root(x)
    y = find_root(y)
    root[x] = y


n, m = map(int, sys.stdin.readline().split())
root = [i for i in range(n+1)]
for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    if not t:
        union(a, b)
    else:
        print('YES' if find_root(a) == find_root(b) else 'NO')