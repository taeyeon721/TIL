import sys
input = sys.stdin.readline
N, M = map(int, input().split())
n = {input().rstrip() for _ in range(N)}
m = {input().rstrip() for _ in range(M)}
ans = n - (n-m)
ans = sorted(list(ans))
print(len(ans))
for name in ans:
    print(name)