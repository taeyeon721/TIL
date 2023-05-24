from collections import deque

N, K = map(int, input().split())
q = deque([])
visited = [0]*100001
ans = 0
q.append([N, 0])
visited[N] = 1
while q:
    loc, t = q.popleft()
    if loc == K:
        ans = t
        break
    else:
        if 0 <= loc-1 <= 100000:
            if not visited[loc-1]:
                q.append([loc-1, t+1])
                visited[loc-1] = 1
        if 0 <= loc+1 <= 100000:
            if not visited[loc+1]:
                q.append([loc+1, t+1])
                visited[loc+1] = 1
        if 0 <= 2*loc <= 100000:
            if not visited[2*loc]:
                q.append([2*loc, t+1])
                visited[2*loc] = 1
print(ans)