import sys
input = sys.stdin.readline
N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)
ans = 0
for i in range(N):
    if K//lst[i] != 0:
        ans += K//lst[i]
        K %= lst[i]
print(ans)