import sys
input = sys.stdin.readline

N = int(input())
arr = list(input())
sumV = 0
for i in range(N):
    sumV += int(arr[i])
print(sumV)