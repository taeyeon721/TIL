import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)
    visited[b] += 1
lst = list(filter(lambda x: visited[x] == 0, range(1, N+1)))
q = deque(lst)
while q:
    i = q.popleft()
    result.append(i)
    for ni in adjList[i]:
        visited[ni] -= 1
        if visited[ni] == 0:
            q.append(ni)
print(*result)