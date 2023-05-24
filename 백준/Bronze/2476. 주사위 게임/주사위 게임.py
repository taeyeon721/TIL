N = int(input())
price = []
for _ in range(N):
    d = list(map(int, input().split()))
    d.sort()
    if d[0] == d[1] and d[1] == d[2]:
        p = 10000 + d[0] * 1000
    elif d[0] == d[1] or d[1] == d[2]:
        p = 1000 + d[1] * 100
    else:
        p = d[2] * 100
    price.append(p)
print(max(price))