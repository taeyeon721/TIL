import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
lst = [0]*(N+1)
for _ in range(Q):
    i = int(input())
    n = i
    flag = 0
    while n > 1:
        if lst[n] == 1:
            flag = n
        n //= 2
    if flag == 0:
        lst[i] = 1
    print(flag)