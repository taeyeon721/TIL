from collections import deque
N = int(input())
q = deque(list(range(1, N+1)))
while len(q) > 1:
    q.popleft()
    n = q.popleft()
    q.append(n)
print(*q)