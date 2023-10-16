import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
lst = sorted(list(map(int, input().split())))
if N <= K:
    print(0)
else:
    d = []
    for i in range(1, N):
        d.append(lst[i]-lst[i-1])
    d.sort()
    for _ in range(K-1):
        d.pop()
    print(sum(d))