from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [0]*101
for _ in range(N+M):
    a, b = map(int, input().split())
    lst[a] = b
q = deque([])
visited = [0]*101
q.append([1, 0])
while q:
    n, t = q.popleft()
    if n == 100:
        break
    t += 1
    for i in range(1, 7):
        ni = n+i
        if ni > 100 or visited[ni]:
            continue
        visited[ni] = 1
        if lst[ni]:
            q.append([lst[ni], t])
        else:
            q.append([ni, t])
print(t)