import heapq
import sys
input = sys.stdin.readline
N = int(input())
q = []
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
heapq.heappush(q, lst[0][1])
for i in range(1, N):
    if q[0] > lst[i][0]:
        heapq.heappush(q, lst[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, lst[i][1])
print(len(q))