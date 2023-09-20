N = int(input())
ans = 1
while N > 1:
    N -= 6*ans
    ans += 1
print(ans)