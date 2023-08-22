import sys
input = sys.stdin.readline
M = int(input())
S = 0
for _ in range(M):
    lst = input().split()
    if lst[0] == 'all':
        S = (1 << 20)-1
    elif lst[0] == 'empty':
        S = 0
    else:
        st = lst[0]
        n = int(lst[1])-1
        if st == 'add':
            S |= (1 << n)
        elif st == 'remove':
            S &= ~(1 << n)
        elif st == 'check':
            if S & (1 << n) == 0:
                print(0)
            else:
                print(1)
        elif st == 'toggle':
            S = S ^ (1 << n)