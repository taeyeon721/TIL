import sys
from collections import deque


def bfs():
    for i in range(1, V+1):
        if not visited[i]:
            visited[i] = 1
            q = deque([i])

        while q:
            n = q.popleft()
            for j in adjList[n]:
                if not visited[j]:
                    visited[j] = visited[n]*(-1)
                    q.append(j)
                else:
                    if visited[j] == visited[n]:
                        return 'NO'
    return 'YES'


K = int(sys.stdin.readline())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    adjList = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        adjList[a].append(b)
        adjList[b].append(a)
    visited = [0]*(V+1)
    ans = bfs()
    print(ans)