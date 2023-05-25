n, m = map(int, input().split())
ans = 1
if m > (n//2):
    for i in range(n, m, -1):
        ans *= i
    for i in range(1, n-m+1):
        ans //= i
else:
    for i in range(n, n-m, -1):
        ans *= i
    for i in range(1, m+1):
        ans //= i
print(ans)