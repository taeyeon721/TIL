import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    ans = pow(a, b, 10)
    if ans == 0:
        ans = 10
    print(ans)