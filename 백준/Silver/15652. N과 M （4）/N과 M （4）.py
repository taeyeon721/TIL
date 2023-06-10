def f(lst):
    if len(lst) == M:
        ans.append(lst)
        return
    else:
        for j in range(lst[-1], N+1):
            nlst = lst+[j]
            f(nlst)


N, M = map(int, input().split())
ans = []
for i in range(1, N+1):
    f([i])
ans.sort()
for lst in ans:
    print(*lst)