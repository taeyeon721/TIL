T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    x, y = max(A, B), min(A, B)
    while True:
        if x % y == 0:
            break
        x, y = y, (x % y)
    print(A*B // y)