from collections import deque
N, K = map(int, input().split())
lst = list(input().split())
res = sorted(lst)
q = deque([[lst, 0]])
visited = {"".join(lst)}
ans = -1
while q:
    l, cnt = q.popleft()
    if l == res:
        ans = cnt
        break
    for i in range(N-K+1):
        rl = l[i:i+K]
        rl.reverse()
        nl = l[:i]+rl+l[i+K:]
        s = "".join(nl)
        if s not in visited:
            q.append([nl, cnt+1])
            visited.add(s)
print(ans)