N = int(input())
lst = [1]*(N+1)
for i in range(2, N+1):
    for j in range(2*i, N+1, i):
        lst[j] = 0
prime = []
for i in range(2, N+1):
    if lst[i]:
        prime.append(i)
ans = 0
s = 0
e = 0
while e <= len(prime):
    tmp = sum(prime[s:e])
    if tmp == N:
        ans += 1
        e += 1
    elif tmp > N:
        s += 1
    else:
        e += 1
print(ans)