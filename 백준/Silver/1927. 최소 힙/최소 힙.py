import heapq, sys
input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(q, n)
    else:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)