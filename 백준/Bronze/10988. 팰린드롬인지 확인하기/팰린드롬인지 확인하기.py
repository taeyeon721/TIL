W = input()
i = 0
ans = 1
while i < len(W)//2:
    if W[i] != W[-1-i]:
        ans = 0
        break
    i += 1
print(ans)