import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    lst = list(input().rstrip().split())
    for w in lst:
        print(w[::-1], end=" ")
    print()