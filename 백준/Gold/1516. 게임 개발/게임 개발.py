import sys
from collections import deque

N = int(sys.stdin.readline())
g = [[] for _ in range(N+1)]
time = [0]
result = [0]*(N+1)
indegree = [0]*(N+1)
for i in range(1, N+1):
    lst = list(map(int, sys.stdin.readline().split()))
    time.append(lst[0])
    for j in lst[1:-1]:
        g[j].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        result[i] = time[i]
        q.append(i)
while q:
    n = q.popleft()
    for m in g[n]:
        indegree[m] -= 1
        result[m] = max(result[m], result[n] + time[m])

        if not indegree[m]:
            q.append(m)

for i in range(1, N+1):
    print(result[i])