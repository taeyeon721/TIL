from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
t = [0]
dp = [0]*(N+1)
for i in range(N):
    lst = list(map(int, input().split()))
    t.append(lst[0])
    for j in range(lst[1]):
        adj[lst[2+j]].append(i+1)
        visited[i+1] += 1
q = deque()
for i in range(1, N+1):
    if visited[i] == 0:
        dp[i] = t[i]
        q.append(i)
while q:
    i = q.popleft()
    for ni in adj[i]:
        visited[ni] -= 1
        dp[ni] = max(dp[i]+t[ni], dp[ni])
        if visited[ni] == 0:
            q.append(ni)
print(max(dp))