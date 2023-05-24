N = int(input())
ans = 0
if N % 4 == 0:
    if N % 100 != 0 or N % 400 == 0:
        ans = 1
print(ans)