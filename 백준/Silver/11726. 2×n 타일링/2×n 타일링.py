n = int(input())
f = [0]*(1001)
f[1] = 1
f[2] = 2
if n > 2:
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
print(f[n] % 10007)