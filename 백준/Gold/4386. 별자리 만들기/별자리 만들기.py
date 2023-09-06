import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
dist = []
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        dist.append([((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2), i, j])
dist.sort()
for d in dist:
    s, x, y = d
    if find(x) != find(y):
        union(x, y)
        ans += s
print(round(ans, 2))