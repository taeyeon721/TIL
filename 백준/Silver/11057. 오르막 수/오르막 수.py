N = int(input())
ans = 0
n = [1]*10
k = 1
while True:
    if k == N:
        break
    for i in range(9, -1, -1):
        n[i] = sum(n[0:i+1])
    k += 1
ans = sum(n)
print(ans%10007)