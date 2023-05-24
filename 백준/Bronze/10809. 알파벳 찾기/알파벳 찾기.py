s = list(input())
s = list(map(lambda x: ord(s[x]), range(len(s))))
l = [-1]*26
for i in range(97, 123):
    if i in s:
        l[i-97] = s.index(i)
print(*l)