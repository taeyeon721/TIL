N, X = map(int, input().split())
lst = list(map(int, input().split()))
lower = []
for num in lst:
    if num < X:
        lower.append(num)
print(*lower)