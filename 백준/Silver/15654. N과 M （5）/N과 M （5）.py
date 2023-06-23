def f(s, m):
    if len(s) == m:
        ans.append(s)
        return
    else:
        for j in range(N):
            if lst[j] not in s:
                ns = s + [lst[j]]
                f(ns, m)


N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    S = [lst[i]]
    f(S, M)
ans.sort()
for x in ans:
    print(*x)