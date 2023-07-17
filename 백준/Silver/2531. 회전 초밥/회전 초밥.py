import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
lst = [0]*N
for i in range(N):
    lst[i] = int(input())
lst = lst+lst[0:k-1]
ans = 0
for i in range(N):
    s = set(lst[i:i+k])
    s.add(c)
    if len(s) > ans:
        ans = len(s)
print(ans)