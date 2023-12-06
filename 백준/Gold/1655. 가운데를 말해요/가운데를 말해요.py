import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
min_heap = []
max_heap = []

for _ in range(N):
    num = int(input())
    if len(min_heap) == len(max_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    if len(min_heap) == 0:
        print(-max_heap[0])
        continue

    if -max_heap[0] > min_heap[0]:
        n = -heappop(max_heap)
        m = heappop(min_heap)
        heappush(max_heap, -m)
        heappush(min_heap, n)
    print(-max_heap[0])