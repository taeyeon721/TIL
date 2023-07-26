import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += (arr[i][0]*arr[(i+1)%N][1]-arr[i][1]*arr[(i+1)%N][0])
ans = round(abs(ans)/2, 1)
print(ans)