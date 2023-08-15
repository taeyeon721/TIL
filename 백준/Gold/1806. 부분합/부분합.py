import sys
input = sys.stdin.readline
N, S = map(int,input().split())
lst = list(map(int, input().split()))
p = [0]*(N+1)
for i in range(N):
    p[i+1] = p[i]+lst[i]
ans = 100001
s, e = 0, 0
while e < N+1:
    if p[e]-p[s] >= S:
        if e-s < ans:
            ans = e-s
        s += 1
    else:
        e += 1
if ans == 100001:
    ans = 0
print(ans)