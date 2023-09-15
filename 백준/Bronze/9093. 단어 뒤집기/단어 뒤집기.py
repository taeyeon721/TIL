import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    lst = list(input().rstrip().split())
    for w in lst:
        for i in range(1, len(w)+1):
            print(w[-i], end='')
        print(end=' ')
    print()