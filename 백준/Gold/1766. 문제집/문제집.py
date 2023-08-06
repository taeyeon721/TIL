import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
lst = [0]*(N+1)
for i in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    lst[B] += 1
q = []
for i in range(1, N+1):
    if lst[i] == 0:
        q.append(i)
ans = []
while q:
    n = heapq.heappop(q)
    ans.append(n)
    for i in adj[n]:
        lst[i] -= 1
        if lst[i] == 0:
            heapq.heappush(q, i)
print(*ans)