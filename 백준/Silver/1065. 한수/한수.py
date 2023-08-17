N = int(input())
ans = 0
if N < 100:
    ans = N
else:
    ans = 99
    for i in range(100, N+1):
        if i//100-i%100//10 == i%100//10-i%10:
            ans += 1
print(ans)