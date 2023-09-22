import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in range(N-1, -1, -1):
        if lst[i] > m:
            m = lst[i]
        else:
            ans += m - lst[i]
    print(ans)