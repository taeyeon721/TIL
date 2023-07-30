from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    lst = list(map(int, input().split()))
    for i in range(lst[0]-1):
        adj[lst[i+1]].append(lst[i+2])
        visited[lst[i+2]] += 1
q = deque()
res = []
for i in range(1, N+1):
    if visited[i] == 0:
        q.append(i)
        res.append(i)
while q:
    i = q.popleft()
    for ni in adj[i]:
        visited[ni] -= 1
        if visited[ni] == 0:
            q.append(ni)
            res.append(ni)
if len(res) != N:
    print(0)
else:
    for i in range(N):
        print(res[i])