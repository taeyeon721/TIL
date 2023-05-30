from collections import deque
A, B = map(int, input().split())
q = deque()
q.append((A, 1))
ans = -1
while q:
    n, c = q.popleft()
    if n == B:
        ans = c
        break
    else:
        if n*2 <= B:
            q.append((n*2, c+1))
        if n*10+1 <= B:
            q.append((n*10+1, c+1))
print(ans)