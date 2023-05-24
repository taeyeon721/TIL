T = int(input())
for tc in range(T):
    lst = list(input().split())
    N = float(lst[0])
    for i in range(1, len(lst)):
        if lst[i] == '@':
            N *= 3
        elif lst[i] == '%':
            N += 5
        elif lst[i] == '#':
            N -= 7
    print(f'{N:.2f}')