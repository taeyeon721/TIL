import sys
from collections import deque


def bfs(root):
    queue = deque([root])
    visited = [0]*(N+1)
    visited[root] = 1

    while queue:
        n = queue.popleft()
        for m in tr[n]:
            if not visited[m]:
                visited[m] = 1
                queue.append(m)
    return visited.count(1)


N, M = map(int, sys.stdin.readline().split())
tr = [[] for _ in range(N+1)]
listH = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    tr[b].append(a)
for i in range(1, N+1):
    listH[i] = bfs(i)
ans = list(filter(lambda x: listH[x] == max(listH), range(len(listH))))
print(*ans)