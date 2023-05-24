import sys
input = sys.stdin.readline

INF = 10**11
N, M = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    g[A].append([B, C])

dist = [INF]*(N+1)


def bellman_ford(g, start):
    dist[start] = 0

    for i in range(N):
        for n in range(1, N+1):
            for b, c in g[n]:
                if dist[n] != INF and dist[b] > dist[n]+c:
                    dist[b] = dist[n]+c
                    if i == N-1:
                        return -1


ans = bellman_ford(g, 1)
if ans == -1:
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] != INF else -1)