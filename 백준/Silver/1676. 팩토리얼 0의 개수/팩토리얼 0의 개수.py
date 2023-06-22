import math
N = int(input())
F = math.factorial(N)
ans = 0
while F % 10 == 0:
    F //= 10
    ans += 1
print(ans)