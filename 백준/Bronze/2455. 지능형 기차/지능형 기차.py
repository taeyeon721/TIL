n = 0
maxV = 0
for _ in range(4):
    A, B = map(int, input().split())
    n = n - A + B
    if maxV < n:
        maxV = n
print(maxV)