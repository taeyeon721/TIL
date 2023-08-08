from collections import deque
F, S, G, U, D = map(int, input().split())
q = deque()
visited = [0]*(F+1)
q.append([S, 0])
visited[S] = 1
ans = -1
while q:
    n, t = q.popleft()
    if n == G:
        ans = t
        break
    if n+U <= F and visited[n+U] == 0:
        visited[n+U] = 1
        q.append([n+U, t+1])
    if n-D > 0 and visited[n-D] == 0:
        visited[n-D] = 1
        q.append([n-D, t+1])
if ans == -1:
    print('use the stairs')
else:
    print(ans)