import sys


def find_root(x):
    if root[x] != x:
        root[x] = find_root(root[x])
    return root[x]


def union(x, y):
    x = find_root(x)
    y = find_root(y)
    root[y] = x


N = int(sys.stdin.readline())   # 도시의 수
M = int(sys.stdin.readline())   # 계획에 속한 도시의 수
root = [i for i in range(N+1)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N):
    for j in range(N-1):
        if arr[i][j]:
            union(i+1, j+1)
route = list(map(int, sys.stdin.readline().split()))
ans = set(map(find_root, route))
print('YES' if len(ans) == 1 else 'NO')