M = int(input())
N = int(input())
lst = [1]*(N+1)
lst[0], lst[1] = 0, 0
p = []
for i in range(2, int(N*(1/2))+1):
    if lst[i] == 1:
        j = 2
        while i*j <= N:
            lst[i*j] = 0
            j += 1
for i in range(M, N+1):
    if lst[i] == 1:
        p.append(i)
if len(p):
    print(sum(p))
    print(min(p))
else:
    print(-1)