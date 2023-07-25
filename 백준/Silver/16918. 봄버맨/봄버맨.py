import sys
input = sys.stdin.readline


def f(arr):
    res = [['O']*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                res[i][j] = '.'
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        res[ni][nj] = '.'
    return res


R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]
if N == 1:
    ans = board
elif N%4 == 1 or N%4 == 3:
    ans = f(board)
    if N%4 == 1:
        ans = f(ans)
else:
    ans = [['O']*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        print(ans[i][j], end='')
    print()