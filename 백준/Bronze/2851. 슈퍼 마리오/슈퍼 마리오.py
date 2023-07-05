ans = 0
minV = 100
for _ in range(10):
    m = int(input())
    ans += m
    if abs(100-ans) <= minV:
        minV = abs(100-ans)
    else:
        ans -= m
        break
print(ans)