import sys
from collections import deque
input = sys.stdin.readline

INF = -10**9
N, S, E, M = map(int, input().split())
g = [[] for _ in range(N)]
dist = [INF]*(N)
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
m = list(map(int, input().split()))


def bfs(s):
    q = deque()
    q.append(s)
    visited = [0]*(N)
    visited[s] = 1

    while q:
        now = q.popleft()
        if now == E:
            return True
        for b, c in g[now]:
            if not visited[b]:
                visited[b] = 1
                q.append(b)
    return False


def bellman(g, start):
    dist[start] = m[start]

    for n in range(N):
        for i in range(N):
            for b, c in g[i]:
                if dist[i] != INF and dist[b] < dist[i]-c+m[b]:
                    dist[b] = dist[i]-c+m[b]
                    if n == N-1 and bfs(b):
                        return 'Gee'


ans = bellman(g, S)
if ans == 'Gee':
    print(ans)
else:
    print(dist[E] if dist[E] != INF else 'gg')