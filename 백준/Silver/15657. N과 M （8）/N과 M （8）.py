def f(n, lst):
    if len(lst) == M:
        ans.append(lst)
        return
    else:
        for j in range(n, N):
            nlst = lst+[nums[j]]
            f(j, nlst)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []
for i in range(N):
    f(i, [nums[i]])
ans.sort()
for lst in ans:
    print(*lst)