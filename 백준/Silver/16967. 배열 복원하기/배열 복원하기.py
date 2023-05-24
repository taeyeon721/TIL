import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H+X)]
ans = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = arr[i][j]
for i in range(X, H):
    for j in range(Y, W):
        ans[i][j] -= ans[i-X][j-Y]
for i in range(H):
    print(*ans[i])