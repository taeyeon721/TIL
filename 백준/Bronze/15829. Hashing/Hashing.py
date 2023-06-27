L = int(input())
st = list(input())
ans = 0
for i in range(L):
    ans += (ord(st[i])-96)*pow(31, i)
print(ans)