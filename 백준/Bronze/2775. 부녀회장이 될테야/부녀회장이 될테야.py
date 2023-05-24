import sys
input = sys.stdin.readline

T = int(input())
arr = [[0]*15 for _ in range(15)]
for i in range(1, 15):
    arr[0][i] = i
for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]
for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])