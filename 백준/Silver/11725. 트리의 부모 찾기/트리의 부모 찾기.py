import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
parent = [i for i in range(N+1)]
visited = [0]*(N+1)
lst = [[] for _ in range(N+1)]
q = deque([1])
visited[1] = 1
for _ in range(N-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

while q:
    n = q.popleft()
    for i in lst[n]:
        if not visited[i]:
            parent[i] = n
            q.append(i)
            visited[i] = 1
for i in range(2, N+1):
    print(parent[i])