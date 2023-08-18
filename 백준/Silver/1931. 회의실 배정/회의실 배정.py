import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
t = sorted(arr, key=lambda x: (x[1], x[0]))
ans = 0
i = 0
for s, e in t:
    if i <= s:
        ans += 1
        i = e
print(ans)