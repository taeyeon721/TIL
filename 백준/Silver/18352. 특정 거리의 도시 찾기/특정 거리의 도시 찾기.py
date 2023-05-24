from collections import deque
import sys


def bfs(graph, root):
    queue = deque([[0, root]])

    while queue:
        s, e = queue.popleft()
        if visited[e] == 0:
            visited[e] = visited[s]+1
            if visited[e] > K+1:
                return
            for n in graph[e]:
                if visited[n] == 0:
                    queue.append([e, n])


N, M, K, X = map(int, sys.stdin.readline().split())
adjList = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)
bfs(adjList, X)
if K+1 in visited:
    city_list = list(filter(lambda x: visited[x] == K+1, range(len(visited))))
    for i in city_list:
        print(i)
else:
    print(-1)