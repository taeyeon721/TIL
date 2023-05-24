def f():
    for i in range(2, N+1):
        d[i] = d[i-1]+d[i-2]


N = int(input())
d = [0]*(N+1)
d[1] = 1
if N > 1:
    f()
print(d[N])