def hanoi(n, s, e, a):
    if n == 1:
        res = []
        res.append([s, e])
        return res
    else:
        res = hanoi(n-1, s, a, e)
        res.append([s, e])
        res += hanoi(n-1, a, e, s)
        return res


N = int(input())
ans = hanoi(N, 1, 3, 2)
print(len(ans))
for lst in ans:
    print(*lst)