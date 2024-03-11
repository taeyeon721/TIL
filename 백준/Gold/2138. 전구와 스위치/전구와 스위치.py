import sys
input = sys.stdin.readline
N = int(input())
bulb = list(map(int, input().rstrip()))
res = list(map(int, input().rstrip()))


def change(A, B):
    A_copy = A[:]
    n = 0
    for i in range(1, N):
        if A_copy[i-1] == B[i-1]:
            continue
        n += 1
        for j in range(i-1, i+2):
            if j < N:
                A_copy[j] = 1-A_copy[j]
    if A_copy == B:
        return n
    else:
        return 1e9


cnt = change(bulb, res)
bulb[0] = 1-bulb[0]
bulb[1] = 1-bulb[1]
cnt = min(cnt, change(bulb, res)+1)
if cnt == 1e9:
    print(-1)
else:
    print(cnt)