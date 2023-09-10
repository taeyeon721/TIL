import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
ans = 0
for _ in range(P):
    g = find(int(input()))
    if g == 0:
        break
    parent[g] = parent[g-1]
    ans += 1
print(ans)