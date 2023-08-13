from collections import deque
import sys
input = sys.stdin.readline


def dfs(i):
    visited[i] = 1
    print(i, end=" ")
    for ni in adj[i]:
        if visited[ni] == 0:
            dfs(ni)


def bfs(V):
    visited[V] = 1
    q = deque([V])
    while q:
        n = q.popleft()
        print(n, end=" ")
        for i in adj[n]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(N+1):
    adj[i].sort()
visited = [0]*(N+1)
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)