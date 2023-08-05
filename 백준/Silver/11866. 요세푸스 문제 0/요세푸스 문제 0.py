from collections import deque
N, K = map(int, input().split())
lst = range(1, N+1)
q = deque(lst)
i = 0
ans = []
while q:
    n = q.popleft()
    i += 1
    if i == K:
        ans.append(n)
        i = 0
    else:
        q.append(n)
print('<', end='')
for i in range(N-1):
    print(ans[i], end=', ')
print(f'{ans[N-1]}>')