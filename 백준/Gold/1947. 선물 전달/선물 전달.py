N = int(input())
d = [0]*(N+1)
if N > 1:
    d[2] = 1
    for i in range(2, N):
        d[i+1] = (i*(d[i]+d[i-1])) % 1000000000
print(d[N])