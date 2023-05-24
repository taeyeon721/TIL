N = int(input())
M = 2
while N > 1:
    if N % M == 0:
        N //= M
        print(M)
    else:
        M += 1