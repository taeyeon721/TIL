def bfs(g,s,visited):
    q = [1]
    visited[s] = 1
    while q:
        v = q.pop(0)
        for i in g[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N = int(input())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
X = int(input())
for _ in range(X):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
bfs(adj, 1, visited)
print(visited.count(1)-1)
