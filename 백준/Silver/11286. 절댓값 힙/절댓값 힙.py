import sys, heapq
input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x:
        if x > 0:
            heapq.heappush(q, [x, x])
        else:
            heapq.heappush(q, [-x, x])
    else:
        if q:
            n = heapq.heappop(q)
            print(n[1])
        else:
            print(0)