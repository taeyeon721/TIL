def f(x, y):
    global maxV
    if x == N:
        if maxV < y:
            maxV = y
    else:
        f(x+1, y)
        if x+T[x]<=N:
            f(x+T[x], y+P[x])


N = int(input())
T = [0]*N
P = [0]*N
maxV = 0
for i in range(N):
    t, p = map(int, input().split())
    T[i], P[i] = t, p
f(0, 0)
print(maxV)