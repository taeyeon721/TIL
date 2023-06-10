def f(lst):
    if len(lst) == M:
        ans.append(lst)
        return
    else:
        for j in range(lst[-1]+1, N+1):
            if used[j] == 0:
                nlst = lst + [j]
                used[j] = 1
                f(nlst)
                used[j] = 0


N, M = map(int, input().split())
used = [0]*(N+1)
ans = []
for i in range(1, N+1):
    used[i] = 1
    f([i])
    used[i] = 0
ans.sort()
for lst in ans:
    print(*lst)