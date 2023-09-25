from collections import deque
N, K = map(int, input().split())
lst = [0]*100001
visited = [0]*100001
q = deque([N])
visited[N] = 1
while q:
    n = q.popleft()
    if n == K:
        break
    for i in (n-1, n+1, n*2):
        if 0 <= i <= 100000 and visited[i] == 0:
            visited[i] = visited[n]+1
            q.append(i)
            lst[i] = n
print(visited[K]-1)
ans = []
x = K
for _ in range(visited[K]):
    ans.append(x)
    x = lst[x]
ans.reverse()
print(*ans)