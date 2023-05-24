import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sumL = 0
l = [0]
for num in lst:
    sumL += num
    l.append(sumL)
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    print(l[j]-l[i])