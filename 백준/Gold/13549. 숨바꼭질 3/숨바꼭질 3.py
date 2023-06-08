from collections import deque
N, K = map(int, input().split())
q = deque([N])
visited = [-1]*100001
visited[N] = 0
while q:
    n = q.popleft()
    if n == K:
        break
    else:
        if 0 <= n*2 <= 100000 and visited[n*2] == -1:
            q.appendleft(n*2)
            visited[n*2] = visited[n]
        if 0 <= n-1 <= 100000 and visited[n-1] == -1:
            q.append(n-1)
            visited[n-1] = visited[n] + 1
        if 0 <= n+1 <= 100000 and visited[n+1] == -1:
            q.append(n+1)
            visited[n+1] = visited[n] + 1
print(visited[K])