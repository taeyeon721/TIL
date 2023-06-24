import math
M, N = map(int, input().split())
lst = [1]*(N+1)
lst[1] = 0
for i in range(2, int(math.sqrt(N))+1):
    if lst[i]:
        j = 2
        while i*j <= N:
            lst[i*j] = 0
            j += 1
for i in range(M, N+1):
    if lst[i]:
        print(i)