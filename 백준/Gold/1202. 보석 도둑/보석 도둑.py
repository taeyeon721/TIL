import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
q =[]
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(q, (M, V))
C = []
for _ in range(K):
    C.append(int(input()))
C.sort()
ans = 0
tmp = []
for c in C:
    while q and q[0][0] <= c:
        heapq.heappush(tmp, -q[0][1])
        heapq.heappop(q)
    if tmp:
        ans -= heapq.heappop(tmp)
print(ans)