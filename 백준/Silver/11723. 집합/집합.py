import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    lst = list(input().split())
    if lst[0] == 'add':
        S.add(int(lst[1]))
    elif lst[0] == 'remove':
        if int(lst[1]) in S:
            S.remove(int(lst[1]))
    elif lst[0] == 'check':
        print(1 if int(lst[1]) in S else 0)
    elif lst[0] == 'toggle':
        if int(lst[1]) in S:
            S.remove(int(lst[1]))
        else:
            S.add(int(lst[1]))
    elif lst[0] == 'all':
        S = set(range(1, 21))
    else:
        S = set()