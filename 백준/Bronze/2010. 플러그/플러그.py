import sys
N = int(sys.stdin.readline().rstrip())
sumV = 1
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    sumV += (x-1)
print(sumV)