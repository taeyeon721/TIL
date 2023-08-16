import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for _ in range(N):
    a = set()
    st = input()
    for i in range(len(st)):
        if st[i] in a and st[i] != st[i-1]:
            break
        a.add(st[i])
        if i == len(st)-1:
            ans += 1
print(ans)