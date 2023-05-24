lst = list(map(int, input().split()))
ans = 0
for num in lst:
    ans += num**2
    ans %= 10
print(ans)